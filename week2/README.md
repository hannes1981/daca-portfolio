# Nädal 2: SQL andmete puhastamine

Selle kausta materjalid kajastavad DACA programmi 2. nädala grupitööd ning minu rolli analüüsitulemusi.

## Roll B: Kliendiandmete puhastaja

Auditeerisin ja puhastasin tabelit `customers_test`.

### Peamised tulemused:
- **Duplikaatsed e-mailid:** 128 korduvat aadressi.
- **Ebajärjekindlad linnanimed:** 43 ebakorrektset nimekuju (tühikud ja tähesuuruste erinevused).
- **Puuduvad e-mailid:** 380 kirjet ilma e-posti aadressita.

## Kausta sisu
- [`individual/week2_customers_report.md`](week2_customers_report.md) – Kliendiandmete auditiraport.
- [`individual/week2_customers_cleaning.sql`](week2_customers_cleaning.sql) – SQL-päringud andmete kontrolliks ja puhastamiseks.
- `team/` – Meeskonna ühine koondraport.
