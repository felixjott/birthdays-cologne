# Geburtstagskalender

Abonniere den Kalender, um die Geburtstage automatisch in deinen Kalender zu bekommen.

## Abonnieren

**Kalender-URL:**
```
https://felixjott.github.io/birthday-calendar/birthdays.ics
```

### Google Calendar
Einstellungen → Weitere Kalender → Per URL hinzufügen → URL einfügen

### Apple Calendar
Ablage → Neues Kalenderabonnement → URL einfügen

### Outlook
Kalender hinzufügen → Aus dem Internet → URL einfügen

---

## Daten aktualisieren

```bash
python3 generate.py
git add birthdays.csv birthdays.ics
git commit -m "update birthdays"
git push
```
