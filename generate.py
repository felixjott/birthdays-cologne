#!/usr/bin/env python3
"""Generate birthdays.ics from Google Sheet – no external dependencies."""

import csv
import uuid
import urllib.request
import io
from datetime import date

SHEET_ID = "1hbfYdkWaotfH0qGEd_BCVPWZ8xcaWggPP31Yqm7aHJU"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
OUTPUT_FILE = "birthdays.ics"


def load_birthdays():
    print(f"Fetching data from Google Sheet...")
    with urllib.request.urlopen(SHEET_URL) as response:
        content = response.read().decode("utf-8")

    entries = []
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        name = row["Name"].strip()
        raw = row["Geburtstag"].strip()
        if name and raw:
            day, month = raw.rstrip(".").split(".")
            entries.append({"name": name, "month": int(month), "day": int(day)})
    return entries


def make_event(name, month, day):
    uid = str(uuid.uuid4())
    # Base date for the recurring event
    dtstart = f"{date.today().year}{month:02d}{day:02d}"
    dtend_date = date(date.today().year, month, day)

    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"SUMMARY:🎂 {name} hat Geburtstag",
        f"DTSTART;VALUE=DATE:{dtstart}",
        f"DTEND;VALUE=DATE:{dtstart}",
        "RRULE:FREQ=YEARLY",
        "BEGIN:VALARM",
        "TRIGGER:PT9H",
        "ACTION:DISPLAY",
        f"DESCRIPTION:🎂 {name} hat heute Geburtstag!",
        "END:VALARM",
        "END:VEVENT",
    ]
    return "\r\n".join(lines)


def main():
    birthdays = load_birthdays()

    header = "\r\n".join([
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Birthday Calendar//felixjott//DE",
        "X-WR-CALNAME:🎂 Geburtstage Köln & Co.",
        "X-WR-TIMEZONE:Europe/Berlin",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ])

    events = "\r\n".join(make_event(b["name"], b["month"], b["day"]) for b in birthdays)

    ics_content = header + "\r\n" + events + "\r\nEND:VCALENDAR\r\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ics_content)

    print(f"✓ {OUTPUT_FILE} generated with {len(birthdays)} birthdays.")


if __name__ == "__main__":
    main()
