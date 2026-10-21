"""Tutto quello che parla con MT5: collegamento, prezzi, ordini, posizioni."""

import math
from dataclasses import dataclass

import MetaTrader5 as mt5

from .orari import broker_a_utc

MAGIC = 260002  # identifica gli ordini del bot (la Fase 0 usava 260001)


class ErroreBroker(Exception):
    pass


@dataclass
class Conto:
    login: int
    demo: bool
    valuta: str
    saldo: float
    equity: float


def collega(cfg_mt5: dict) -> None:
    argomenti = {}
    if cfg_mt5.get("path"):
        argomenti["path"] = cfg_mt5["path"]
    if cfg_mt5.get("login"):
        argomenti.update(login=int(cfg_mt5["login"]), password=cfg_mt5.get("password", ""),
                         server=cfg_mt5.get("server", ""))
    if not mt5.initialize(**argomenti):
        raise ErroreBroker(f"collegamento a MT5 fallito: {mt5.last_error()}")


def collegato() -> bool:
    info = mt5.terminal_info()
    return bool(info and info.connected and mt5.account_info())


def scollega() -> None:
    mt5.shutdown()


def conto() -> Conto:
    a = mt5.account_info()
    if a is None:
        raise ErroreBroker(f"conto non disponibile: {mt5.last_error()}")
    return Conto(a.login, a.trade_mode == mt5.ACCOUNT_TRADE_MODE_DEMO, a.currency, a.balance, a.equity)


def trading_consentito() -> bool:
    info = mt5.terminal_info()
    return bool(info and info.trade_allowed)


def trova_simbolo(nome: str) -> str:
    if mt5.symbol_info(nome) is None:
        candidati = [s.name for s in (mt5.symbols_get(f"{nome}*") or [])]
        if not candidati:
            raise ErroreBroker(f"simbolo {nome} non trovato")
        nome = candidati[0]
    mt5.symbol_select(nome, True)
    return nome


def barre(simbolo: str, timeframe: str, quante: int, da_posizione: int = 0) -> list[dict]:
    """Ultime barre, dalla piu' vecchia alla piu' recente, con orario in UTC."""
    tf = {"M5": mt5.TIMEFRAME_M5, "D1": mt5.TIMEFRAME_D1}[timeframe]
    dati = mt5.copy_rates_from_pos(simbolo, tf, da_posizione, quante)
    if dati is None:
        raise ErroreBroker(f"barre {timeframe} di {simbolo} non disponibili: {mt5.last_error()}")
    return [{"utc": broker_a_utc(b["time"]), "open": float(b["open"]), "high": float(b["high"]),
             "low": float(b["low"]), "close": float(b["close"])} for b in dati]


def prezzo(simbolo: str):
    """(bid, ask, orario UTC dell'ultimo tick)"""
    tick = mt5.symbol_info_tick(simbolo)
    if tick is None or tick.bid <= 0:
        raise ErroreBroker(f"nessun prezzo per {simbolo}")
    return tick.bid, tick.ask, broker_a_utc(tick.time)


def lotti_per_rischio(simbolo: str, direzione: int, entrata: float, stop: float,
                      rischio_valuta_conto: float) -> float:
    """Lotti tali che, se scatta lo stop, si perda al massimo il rischio indicato.
    Arrotonda per difetto al passo del broker; 0 se anche il lotto minimo rischia troppo."""
    info = mt5.symbol_info(simbolo)
    tipo = mt5.ORDER_TYPE_BUY if direzione == 1 else mt5.ORDER_TYPE_SELL
    perdita_un_lotto = mt5.order_calc_profit(tipo, simbolo, 1.0, entrata, stop)
    if perdita_un_lotto is None or perdita_un_lotto >= 0:
        raise ErroreBroker(f"calcolo del rischio fallito: {mt5.last_error()}")
    lotti = math.floor(rischio_valuta_conto / -perdita_un_lotto / info.volume_step) * info.volume_step
    lotti = min(round(lotti, 2), info.volume_max)
    return lotti if lotti >= info.volume_min else 0.0


def _riempimento(simbolo: str):
    modo = mt5.symbol_info(simbolo).filling_mode
    if modo & 1:
        return mt5.ORDER_FILLING_FOK
    if modo & 2:
        return mt5.ORDER_FILLING_IOC
    return mt5.ORDER_FILLING_RETURN


def apri(simbolo: str, direzione: int, lotti: float, distanza_stop: float, commento: str):
    """Ordine a mercato con stop loss sul server del broker. Restituisce (ticket, prezzo, stop)."""
    info = mt5.symbol_info(simbolo)
    bid, ask, _ = prezzo(simbolo)
    entrata = ask if direzione == 1 else bid
    stop = round(entrata - direzione * distanza_stop, info.digits)
    richiesta = {
        "action": mt5.TRADE_ACTION_DEAL, "symbol": simbolo, "volume": lotti,
        "type": mt5.ORDER_TYPE_BUY if direzione == 1 else mt5.ORDER_TYPE_SELL,
        "price": entrata, "sl": stop, "deviation": 50, "magic": MAGIC,
        "comment": commento[:31], "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": _riempimento(simbolo),
    }
    esito = mt5.order_send(richiesta)
    if esito is None or esito.retcode != mt5.TRADE_RETCODE_DONE:
        raise ErroreBroker(f"apertura rifiutata: {esito.retcode if esito else mt5.last_error()} "
                           f"{esito.comment if esito else ''}")
    return esito.order, esito.price, stop


def posizioni_del_bot(simbolo: str) -> list:
    return [p for p in (mt5.positions_get(symbol=simbolo) or []) if p.magic == MAGIC]


def chiudi(posizione, commento: str) -> float:
    bid, ask, _ = prezzo(posizione.symbol)
    long = posizione.type == mt5.POSITION_TYPE_BUY
    richiesta = {
        "action": mt5.TRADE_ACTION_DEAL, "symbol": posizione.symbol, "volume": posizione.volume,
        "type": mt5.ORDER_TYPE_SELL if long else mt5.ORDER_TYPE_BUY,
        "position": posizione.ticket, "price": bid if long else ask, "deviation": 50,
        "magic": MAGIC, "comment": commento[:31], "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": _riempimento(posizione.symbol),
    }
    esito = mt5.order_send(richiesta)
    if esito is None or esito.retcode != mt5.TRADE_RETCODE_DONE:
        raise ErroreBroker(f"chiusura rifiutata: {esito.retcode if esito else mt5.last_error()}")
    return esito.price


def risultato_posizione(ticket: int) -> float:
    """Profitto netto (con commissioni e swap) di una posizione chiusa, in valuta del conto."""
    operazioni = mt5.history_deals_get(position=ticket) or []
    return sum(d.profit + d.commission + d.swap + getattr(d, "fee", 0.0) for d in operazioni)
