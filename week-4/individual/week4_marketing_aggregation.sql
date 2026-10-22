# Nädal 4: SQL Agregatsioon — Turunduskampaaniate ROI

## Minu Roll
- **Domeen:** Roll D — Turunduskampaaniate ROI (*Marketing Campaign Effectiveness*)
- **Eesmärk:** Analüüsida turunduskanalite efektiivsust (`sales` + `web_logs`), puhastada kanalinimed ja koondada veebikülastused ostukäitumisega.

## Peamised Ärilised Leiud
1. **Mitmekanaliline klienditeekond:** Suurim osa käibest kuulub rühma "mitu kanalit", sest kliendid puutuvad enne ostu kokku mitme kampaania ja kanaliga.
2. **Parim individuaalne kanal:** Parima tulemusega individuaalne turunduskanal on `google_ads`.

## AI Kasutamine
Kasutasin AI-d `CASE WHEN` kanalinimede puhastusreeglite kontrollimiseks ja CTE struktureerimiseks, et vältida müügisummade mitmekordset korrutamist liitmisel.
