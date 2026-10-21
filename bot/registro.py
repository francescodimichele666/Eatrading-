"""Registro di tutto quello che il bot vede e decide, piu' gli avvisi Telegram.

- logs/bot.log: testo leggibile, una riga per evento;
- logs/bot.sqlite: eventi e trade in tabelle, per le analisi e per lo stato
  del kill switch (sopravvive ai riavvii).
"""

import json
import logging
import sqlite3
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path

import requests


class Registro:
    def __init__(self, cartella: Path, telegram: dict):
        cartella.mkdir(exist_ok=True)
        self.log = logging.getLogger("bot")
        self.log.setLevel(logging.INFO)
        if not self.log.handlers:
            formato = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
            file = RotatingFileHandler(cartella / "bot.log", maxBytes=5_000_000, backupCount=10,
                                       encoding="utf-8")
            file.setFormatter(formato)
            schermo = logging.StreamHandler()
            schermo.setFormatter(formato)
            self.log.addHandler(file)
            self.log.addHandler(schermo)
        self.db = sqlite3.connect(cartella / "bot.sqlite")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS eventi (utc TEXT, tipo TEXT, testo TEXT, dati TEXT);
            CREATE TABLE IF NOT EXISTS trade (ticket INTEGER PRIMARY KEY, apertura_utc TEXT,
                direzione INTEGER, lotti REAL, prezzo_entrata REAL, stop REAL, chiusura_utc TEXT,
                prezzo_uscita REAL, risultato REAL, motivo TEXT);
            CREATE TABLE IF NOT EXISTS stato (chiave TEXT PRIMARY KEY, valore TEXT);
        """)
        self.telegram = telegram

    def evento(self, tipo: str, testo: str, avvisa: bool = False, **dati):
        livello = logging.WARNING if tipo in ("errore", "blocco") else logging.INFO
        self.log.log(livello, f"[{tipo}] {testo}")
        self.db.execute("INSERT INTO eventi VALUES (?, ?, ?, ?)",
                        (datetime.now(timezone.utc).isoformat(), tipo, testo,
                         json.dumps(dati, default=str)))
        self.db.commit()
        if avvisa:
            self.avvisa(f"{tipo.upper()}: {testo}")

    def avvisa(self, testo: str):
        token, chat = self.telegram.get("token"), self.telegram.get("chat_id")
        if not token or not chat:
            return
        try:
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                          data={"chat_id": chat, "text": f"[Bot oro DEMO] {testo}"[:4000]}, timeout=10)
        except requests.RequestException as errore:
            self.log.warning(f"Telegram non raggiungibile: {errore}")

    def trade_aperto(self, ticket, direzione, lotti, prezzo, stop):
        self.db.execute("INSERT OR REPLACE INTO trade (ticket, apertura_utc, direzione, lotti, "
                        "prezzo_entrata, stop) VALUES (?, ?, ?, ?, ?, ?)",
                        (ticket, datetime.now(timezone.utc).isoformat(), direzione, lotti, prezzo, stop))
        self.db.commit()

    def trade_chiuso(self, ticket, prezzo, risultato, motivo):
        self.db.execute("UPDATE trade SET chiusura_utc=?, prezzo_uscita=?, risultato=?, motivo=? "
                        "WHERE ticket=?",
                        (datetime.now(timezone.utc).isoformat(), prezzo, risultato, motivo, ticket))
        self.db.commit()

    def trade_aperti_registrati(self) -> list[int]:
        return [r[0] for r in self.db.execute("SELECT ticket FROM trade WHERE chiusura_utc IS NULL")]

    def leggi(self, chiave: str, predefinito=None):
        riga = self.db.execute("SELECT valore FROM stato WHERE chiave=?", (chiave,)).fetchone()
        return json.loads(riga[0]) if riga else predefinito

    def scrivi(self, chiave: str, valore):
        self.db.execute("INSERT OR REPLACE INTO stato VALUES (?, ?)", (chiave, json.dumps(valore)))
        self.db.commit()
