"""Un finto MetaTrader5, per provare il bot senza terminale (la libreria vera esiste solo su Windows)."""

import types

import numpy as np

mt5 = types.ModuleType("MetaTrader5")
for nome, valore in dict(TIMEFRAME_M5=5, TIMEFRAME_D1=1440, ORDER_TYPE_BUY=0, ORDER_TYPE_SELL=1,
                         TRADE_ACTION_DEAL=1, ORDER_TIME_GTC=0, ORDER_FILLING_FOK=0,
                         ORDER_FILLING_IOC=1, ORDER_FILLING_RETURN=2, TRADE_RETCODE_DONE=10009,
                         ACCOUNT_TRADE_MODE_DEMO=0, POSITION_TYPE_BUY=0).items():
    setattr(mt5, nome, valore)

TIPO_BARRE = [("time", "i8"), ("open", "f8"), ("high", "f8"), ("low", "f8"), ("close", "f8")]


class Stato:
    def __init__(self):
        self.demo = True
        self.equity = 100_000.0
        self.barre = {}          # timeframe -> array strutturato (dalla piu' vecchia)
        self.bid, self.ask = 4030.0, 4030.1
        self.ora_tick = 0        # secondi broker
        self.posizioni = []
        self.ordini = []
        self.prossimo_ticket = 1000


stato = Stato()
ns = types.SimpleNamespace

mt5.initialize = lambda **k: True
mt5.shutdown = lambda: None
mt5.last_error = lambda: (0, "ok")
mt5.terminal_info = lambda: ns(connected=True, trade_allowed=True)
mt5.account_info = lambda: ns(login=1, trade_mode=0 if stato.demo else 2, currency="EUR",
                              balance=stato.equity, equity=stato.equity)
mt5.symbol_info = lambda s: ns(name=s, digits=2, volume_min=0.01, volume_step=0.01, volume_max=20.0,
                               filling_mode=1, point=0.01) if s == "XAUUSD.r" else None
mt5.symbols_get = lambda pattern: [ns(name="XAUUSD.r")]
mt5.symbol_select = lambda s, v: True
mt5.symbol_info_tick = lambda s: ns(bid=stato.bid, ask=stato.ask, time=stato.ora_tick)


def copy_rates_from_pos(simbolo, tf, da, quante):
    a = stato.barre[tf]
    fine = len(a) - da
    return a[max(0, fine - quante):fine]


mt5.copy_rates_from_pos = copy_rates_from_pos
# 100 once a lotto, profitto in dollari = euro nel finto
mt5.order_calc_profit = lambda tipo, s, lotti, a, b: (b - a) * 100 * lotti * (1 if tipo == 0 else -1)


def order_send(r):
    stato.ordini.append(r)
    if "position" in r:
        stato.posizioni = [p for p in stato.posizioni if p.ticket != r["position"]]
        return ns(retcode=10009, order=r["position"], price=r["price"], comment="")
    stato.prossimo_ticket += 1
    stato.posizioni.append(ns(ticket=stato.prossimo_ticket, symbol=r["symbol"], volume=r["volume"],
                              type=r["type"], sl=r["sl"], magic=r["magic"], time=stato.ora_tick))
    return ns(retcode=10009, order=stato.prossimo_ticket, price=r["price"], comment="")


mt5.order_send = order_send
mt5.positions_get = lambda symbol=None: list(stato.posizioni)
mt5.history_deals_get = lambda position=None: [ns(profit=12.5, commission=-0.5, swap=0.0, fee=0.0)]
