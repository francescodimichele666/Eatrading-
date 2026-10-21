"""Fase 0: controlla che Python, MT5 e il broker funzionino insieme.

Cosa fa, in ordine:
1. si collega al terminale MT5 e mostra i dati del conto;
2. legge le regole del simbolo (lotto minimo, valore di un punto, swap);
3. misura lo spread per qualche secondo;
4. solo su conto DEMO: apre e chiude 0,01 lotti per verificare esecuzione e commissione;
5. scrive tutto in logs/ e, se configurato, manda un riepilogo su Telegram.

Uso: doppio clic su avvia_controllo.bat (oppure: python fase0_controllo.py).
"""

import statistics
import sys
import time
import tomllib
from datetime import datetime
from pathlib import Path

import requests

try:
    import MetaTrader5 as mt5
except ImportError:
    print("ERRORE: libreria MetaTrader5 non installata. Esegui avvia_controllo.bat.")
    sys.exit(1)

CARTELLA = Path(__file__).resolve().parent
MAGIC = 260001  # identifica gli ordini aperti da questo programma

righe_rapporto = []


def scrivi(testo=""):
    print(testo)
    righe_rapporto.append(testo)


def carica_config():
    file = CARTELLA / "config.toml"
    if not file.exists():
        file = CARTELLA / "config.example.toml"
        scrivi("Nota: config.toml non trovato, uso le impostazioni di esempio.")
    with open(file, "rb") as f:
        return tomllib.load(f)


def collega(cfg_mt5):
    argomenti = {}
    if cfg_mt5.get("path"):
        argomenti["path"] = cfg_mt5["path"]
    if cfg_mt5.get("login"):
        argomenti["login"] = int(cfg_mt5["login"])
        argomenti["password"] = cfg_mt5.get("password", "")
        argomenti["server"] = cfg_mt5.get("server", "")
    if not mt5.initialize(**argomenti):
        scrivi(f"ERRORE: collegamento a MT5 fallito: {mt5.last_error()}")
        scrivi("Controlla che MT5 sia installato, aperto e collegato al conto.")
        return None
    conto = mt5.account_info()
    if conto is None:
        scrivi(f"ERRORE: MT5 aperto ma nessun conto collegato: {mt5.last_error()}")
        return None
    return conto


def trova_simbolo(nome):
    if mt5.symbol_info(nome) is not None:
        return nome
    candidati = [s.name for s in (mt5.symbols_get("*XAU*") or []) if "USD" in s.name]
    if candidati:
        scrivi(f"Simbolo '{nome}' non trovato, uso '{candidati[0]}' (trovati: {candidati}).")
        return candidati[0]
    return None


def misura_spread(simbolo, secondi):
    valori = []
    fine = time.time() + secondi
    while time.time() < fine:
        tick = mt5.symbol_info_tick(simbolo)
        if tick and tick.ask > 0 and tick.bid > 0:
            valori.append(tick.ask - tick.bid)
        time.sleep(1)
    if not valori:
        return None
    return {
        "minimo": min(valori),
        "mediano": statistics.median(valori),
        "massimo": max(valori),
        "campioni": len(valori),
    }


def tipo_riempimento(info):
    # filling_mode e' una maschera di bit: 1 = FOK, 2 = IOC
    if info.filling_mode & 1:
        return mt5.ORDER_FILLING_FOK
    if info.filling_mode & 2:
        return mt5.ORDER_FILLING_IOC
    return mt5.ORDER_FILLING_RETURN


def ordine_di_prova(simbolo, info):
    tick = mt5.symbol_info_tick(simbolo)
    volume = info.volume_min
    # Stop loss di sicurezza a 10 $ (o piu' se il broker richiede una distanza minima)
    distanza_sl = max(10.0, info.trade_stops_level * info.point * 2)
    apertura = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": simbolo,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY,
        "price": tick.ask,
        "sl": round(tick.ask - distanza_sl, info.digits),
        "deviation": 50,
        "magic": MAGIC,
        "comment": "fase0 prova",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": tipo_riempimento(info),
    }
    inizio = time.perf_counter()
    risultato = mt5.order_send(apertura)
    ms_apertura = (time.perf_counter() - inizio) * 1000
    if risultato is None or risultato.retcode != mt5.TRADE_RETCODE_DONE:
        codice = risultato.retcode if risultato else mt5.last_error()
        commento = risultato.comment if risultato else ""
        scrivi(f"ERRORE: apertura rifiutata ({codice}) {commento}")
        return False
    scrivi(f"Apertura: {volume} lotti a {risultato.price} in {ms_apertura:.0f} ms "
           f"(prezzo richiesto {tick.ask}, slippage {risultato.price - tick.ask:+.2f})")

    time.sleep(2)
    posizioni = [p for p in (mt5.positions_get(symbol=simbolo) or []) if p.magic == MAGIC]
    if not posizioni:
        scrivi("ERRORE: posizione di prova non trovata dopo l'apertura. Controlla MT5.")
        return False
    posizione = posizioni[0]
    tick = mt5.symbol_info_tick(simbolo)
    chiusura = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": simbolo,
        "volume": posizione.volume,
        "type": mt5.ORDER_TYPE_SELL,
        "position": posizione.ticket,
        "price": tick.bid,
        "deviation": 50,
        "magic": MAGIC,
        "comment": "fase0 chiusura",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": tipo_riempimento(info),
    }
    inizio = time.perf_counter()
    risultato = mt5.order_send(chiusura)
    ms_chiusura = (time.perf_counter() - inizio) * 1000
    if risultato is None or risultato.retcode != mt5.TRADE_RETCODE_DONE:
        codice = risultato.retcode if risultato else mt5.last_error()
        scrivi(f"ERRORE: chiusura rifiutata ({codice}). CHIUDI A MANO la posizione in MT5!")
        return False
    scrivi(f"Chiusura: a {risultato.price} in {ms_chiusura:.0f} ms")

    time.sleep(1)
    operazioni = mt5.history_deals_get(position=posizione.ticket) or []
    commissione = sum(d.commission for d in operazioni)
    risultato_netto = sum(d.profit + d.commission + d.swap + getattr(d, "fee", 0.0) for d in operazioni)
    scrivi(f"Commissione andata e ritorno per {volume} lotti: {commissione:.2f}")
    scrivi(f"Risultato netto del trade di prova: {risultato_netto:.2f} (costo di un trade)")
    return True


def manda_telegram(cfg_tg, testo):
    if not cfg_tg.get("token") or not cfg_tg.get("chat_id"):
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{cfg_tg['token']}/sendMessage",
            data={"chat_id": cfg_tg["chat_id"], "text": testo[:4000]},
            timeout=10,
        )
        print("Riepilogo inviato su Telegram.")
    except requests.RequestException as errore:
        print(f"Telegram non raggiungibile: {errore}")


def salva_rapporto():
    cartella_log = CARTELLA / "logs"
    cartella_log.mkdir(exist_ok=True)
    file = cartella_log / f"fase0_{datetime.now():%Y%m%d_%H%M%S}.txt"
    file.write_text("\n".join(righe_rapporto), encoding="utf-8")
    print(f"\nRapporto salvato in: {file}")
    print("Copia il contenuto di questo file e mandalo a Claude.")


def main():
    cfg = carica_config()
    scrivi(f"=== Controllo Fase 0 - {datetime.now():%d/%m/%Y %H:%M} ===")
    scrivi(f"Python {sys.version.split()[0]}, libreria MetaTrader5 {mt5.__version__}")

    conto = collega(cfg.get("mt5", {}))
    if conto is None:
        return 1
    demo = conto.trade_mode == mt5.ACCOUNT_TRADE_MODE_DEMO
    scrivi()
    scrivi("--- Conto ---")
    scrivi(f"Broker: {conto.company} | Server: {conto.server} | Conto: {conto.login}")
    scrivi(f"Tipo: {'DEMO' if demo else 'REALE'} | Valuta: {conto.currency} | Leva: 1:{conto.leverage}")
    scrivi(f"Saldo: {conto.balance:.2f} | Equity: {conto.equity:.2f}")
    scrivi(f"Trading automatico consentito: {'si' if mt5.terminal_info().trade_allowed else 'NO'}")

    ctrl = cfg.get("controllo", {})
    simbolo = trova_simbolo(ctrl.get("simbolo", "XAUUSD"))
    if simbolo is None:
        scrivi("ERRORE: nessun simbolo dell'oro trovato su questo conto.")
        mt5.shutdown()
        return 1
    mt5.symbol_select(simbolo, True)
    info = mt5.symbol_info(simbolo)
    valore_1_dollaro = info.trade_contract_size * info.volume_min  # in valuta di profitto
    scrivi()
    scrivi(f"--- Regole di {simbolo} ---")
    scrivi(f"Cifre decimali: {info.digits} | Punto: {info.point}")
    scrivi(f"Contratto per 1 lotto: {info.trade_contract_size} | Valuta profitto: {info.currency_profit}")
    scrivi(f"Lotto minimo: {info.volume_min} | Passo: {info.volume_step} | Massimo: {info.volume_max}")
    scrivi(f"Con {info.volume_min} lotti, 1 dollaro di movimento vale {valore_1_dollaro:.2f} {info.currency_profit}")
    scrivi(f"Distanza minima stop: {info.trade_stops_level} punti")
    scrivi(f"Swap long: {info.swap_long} | Swap short: {info.swap_short} (tipo {info.swap_mode})")

    secondi = int(ctrl.get("secondi_misura_spread", 60))
    scrivi()
    scrivi(f"--- Spread misurato per {secondi} secondi ---")
    spread = misura_spread(simbolo, secondi)
    if spread is None:
        scrivi("Nessun prezzo ricevuto: il mercato potrebbe essere chiuso (weekend?).")
    else:
        scrivi(f"Minimo {spread['minimo']:.2f} $ | Mediano {spread['mediano']:.2f} $ | "
               f"Massimo {spread['massimo']:.2f} $ ({spread['campioni']} campioni)")
        scrivi(f"Costo dello spread mediano con {info.volume_min} lotti: "
               f"{spread['mediano'] * valore_1_dollaro:.2f} {info.currency_profit}")

    scrivi()
    scrivi("--- Ordine di prova ---")
    if not ctrl.get("ordine_di_prova", True):
        scrivi("Saltato (disattivato in config.toml).")
    elif not demo:
        scrivi("Saltato: questo e' un conto REALE. Il test si fa solo su demo.")
    elif spread is None:
        scrivi("Saltato: mercato chiuso.")
    else:
        ordine_di_prova(simbolo, info)

    mt5.shutdown()
    scrivi()
    scrivi("=== Controllo finito ===")
    manda_telegram(cfg.get("telegram", {}), "\n".join(righe_rapporto))
    salva_rapporto()
    return 0


if __name__ == "__main__":
    codice = main()
    if codice and righe_rapporto:
        salva_rapporto()
    sys.exit(codice)
