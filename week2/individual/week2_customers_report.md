# Kliendiandmete puhastamise raport (Roll B)

**Autor:** Hannes Saarmets  
**Tabel:** `customers_test`  
**Kuupäev:** 08.10.2026  

---

## 1. Kokkuvõtlik audititabel

---

## 1. Kokkuvõtlik audititabel

| Kategooria | Leitud probleeme | Kirjeldus |
| :--- | :--- | :--- |
| **Duplikaatsed e-mailid** | 128 | Korduvad e-posti aadressid tabelis |
| **NULL / tühi eesnimi** | 0 | Puuduv kliendi eesnimi |
| **NULL / tühi perenimi** | 0 | Puuduv kliendi perenimi |
| **Ebajärjekindlad linnanimed** | 43 | Erinevad nimekujud (nt "tallinn" vs "Tallinn") |
| **Puuduv telefoninumber** | 0 | Registreeritud ilma telefonita |
| **Puuduv e-mail** | 380 | Registreeritud ilma e-mailita |


---

1. **Duplikaatsed e-mailid (128):** 
   - Andmebaasis on korduvaid e-posti aadresse, mis viitab sellele, et kliendid on sooritanud mitu ostu või teinud uue konto ilma sisse logimata.
2. **Ebajärjekindlad linnanimed (43):**
   - Linnade sisestamisel esineb palju tüpoosi, peidetud algus-/lõputühikuid (nt `" Tallinn"`, `"Tallinn "`) ning erinevaid tähesuurusi (`tallinn`, `TALLINN`, `Tallinn`). See vajab ühtlustamist funktsioonidega `INITCAP` ja `TRIM`.
3. **Puuduvad e-mailid (380):**
   - 380 kliendi kirjel puudub e-posti aadress (või on see `NULL`). E-mailide asendamiseks raporteerimisel saab kasutada `COALESCE(email, 'puudub')`.


---
1. **Sisendväljade automatiseerimine:** E-poe registreerimisvormile tuleb lisada e-posti unikaalsuse kontroll ning linnade väljale rippmenüü (dropdown), et vältida tühikuid ja tähesuuruste erinevusi.
2. **Automaatne andmepuhastus:** Seadistada andmebaasi sissetulevate andmete automaatne puhastus (`TRIM` ja `INITCAP`), et hoida andmekvaliteeti tulevikus kõrgena.
