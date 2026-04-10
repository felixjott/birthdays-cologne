# 🎂 Geburtstage Köln & Co.

Ahüüüt & Families – alle Geburtstage inklusive Kids, ob in Rösrath, Aachen, Wolfsburg, Köln, Bremen, Brühl, München oder Düsseldorf.

👉 **https://felixjott.github.io/birthdays-cologne**

---

## Abonnieren

Seite öffnen und auf „Kalender abonnieren" klicken – öffnet direkt in der Kalender-App. Updates kommen automatisch.

**iPhone & Mac** – Link tippen, Kalender-App fragt direkt nach dem Abonnement.

**Google Kalender** – „Weitere Kalender" → „Per URL hinzufügen":
```
https://felixjott.github.io/birthdays-cologne/birthdays.ics
```

**Outlook** – Kalender hinzufügen → Aus dem Internet → URL einfügen.

Bitte nicht als Datei importieren – dann gibt's keine automatischen Updates.

---

## Daten aktualisieren

Geburtstage werden aus einem Google Sheet geladen. Täglich um 07:00 Uhr prüft GitHub Actions auf Änderungen und aktualisiert die ICS-Datei automatisch.

```bash
python3 generate.py  # lokal generieren
git add birthdays.ics && git commit -m "update" && git push
```
