"""Conversione tra ora del broker, UTC, New York e Italia.

MT5 restituisce gli orari come "secondi" nell'ora del server del broker.
FP Markets usa l'ora di New York + 7 ore (verificato il 21/10/2026).
"""

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NEW_YORK = ZoneInfo("America/New_York")
ITALIA = ZoneInfo("Europe/Rome")
ORE_BROKER_SU_NEW_YORK = 7


def broker_a_utc(secondi_broker: int) -> datetime:
    ora_ny = datetime(1970, 1, 1) + timedelta(seconds=int(secondi_broker)) \
        - timedelta(hours=ORE_BROKER_SU_NEW_YORK)
    return ora_ny.replace(tzinfo=NEW_YORK).astimezone(timezone.utc)


def adesso_utc() -> datetime:
    return datetime.now(timezone.utc)


def a_new_york(t: datetime) -> datetime:
    return t.astimezone(NEW_YORK)


def a_italia(t: datetime) -> datetime:
    return t.astimezone(ITALIA)


def new_york(giorno, ora: int, minuto: int = 0) -> datetime:
    """Un orario di New York in un certo giorno, in UTC."""
    return datetime(giorno.year, giorno.month, giorno.day, ora, minuto,
                    tzinfo=NEW_YORK).astimezone(timezone.utc)
