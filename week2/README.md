# Kliendiandmete puhastamise raport (Roll B)

**Autor:** Hannes Saarmets  
**Tabel:** `customers_test`  
**Kuupäev:** 08.10.2026  

---

## 1. Kokkuvõtlik audititabel

| Kategooria | Leitud probleeme | Kirjeldus |
| :--- | :--- | :--- |
| **Duplikaatsed e-mailid** | 128 | Korduvad e-posti aadressid tabelis |
| **NULL / tühi eesnimi** | [arv] | Puuduv kliendi eesnimi |
| **NULL / tühi perenimi** | [arv] | Puuduv kliendi perenimi |
| **Ebajärjekindlad linnanimed** | [arv] | Erinevad nimekujud (nt "tallinn" vs "Tallinn") |
| **Puuduv telefoninumber** | [arv] | Registreeritud ilma telefonita |
| **Puuduv e-mail** | [arv] | Registreeritud ilma e-mailita |

---

## 2. Peamised tähelepanekud ja järeldused
- **Duplikaadid:** Korduvaid e-posti aadresse oli kokku [arv], mis viitab topeltregistreerimistele e-poes.
- **Andmete täielikkus:** Puuduvaid nimesid/kontaktandmeid esines [arv] juhul.
- **Linnanimed:** Linnade puhul esines erinevaid kirjaviise ja tähesuurusi, mis vajavad ühtlustamist (`INITCAP` ja `TRIM`).

---

## 3. Soovitused juhtkonnale (Toomasele)
1. **Unikaalsuse kontroll:** Lisada e-poe registreerimisvormile e-posti unikaalsuse kontroll.
2. **Automaatne puhastus:** Rakendada andmebaasi sisestamisel automaatset tühikute eemaldamist ja esitähe suureks muutmist linnanimedes.
