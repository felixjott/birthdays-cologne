---
title: birthdays-cologne
type: project
description: Geburtstags-Kalender als ICS-Abo – gespeist aus Google Sheet, deployed via GitHub Pages
trigger: Whenever working in this project or adding/updating birthdays
---

## Wie Geburtstage hinzugefügt werden

**Niemals** direkt über die Google Calendar API oder manuell in die .ics schreiben.

1. Namen ins Google Sheet eintragen (Spalten: Name, Geburtstag im Format `DD.MM.`)
2. `python3 generate.py` ausführen – lädt Sheet, schreibt `birthdays.ics`
3. Committen und pushen:
   ```bash
   git add birthdays.ics && git commit -m "update birthdays.ics – add [Name]" && git push
   ```

GitHub Actions aktualisiert die .ics täglich um 07:00 automatisch – manueller Push nur nötig wenn sofortige Verfügbarkeit gewünscht.

## Event-Format (wird vom Script generiert)

- Titel: `🎂 [Vorname] hat Geburtstag`
- Ganztägig, jährlich wiederkehrend
- Erinnerung: `TRIGGER:PT9H` = 09:00 Uhr am Ereignistag

## Deployment

ICS wird über GitHub Pages ausgeliefert: `https://felixjott.github.io/birthdays-cologne/birthdays.ics`
