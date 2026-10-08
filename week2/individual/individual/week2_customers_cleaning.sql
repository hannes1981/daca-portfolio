-- ======================================================
-- DACA Nädal 2 - Grupitöö
-- Roll B: Kliendiandmete puhastaja (Customer Data Cleaner)
-- Autor: [Sinu Nimi]
-- Tabel: customers_test
-- ======================================================

-- 1. Testtabeli loomine (turvaline töökeskkond)
CREATE TABLE IF NOT EXISTS customers_test AS 
SELECT * FROM customers;

-- Kontrollime ridade koguarvu testtabelis
SELECT COUNT(*) AS ridade_kokku 
FROM customers_test;


-- 2. Duplikaatsete e-mailide tuvastamine
SELECT 
    email, 
    COUNT(*) AS koopiate_arv
FROM customers_test
WHERE email IS NOT NULL
GROUP BY email
HAVING COUNT(*) > 1
ORDER BY koopiate_arv DESC;


-- 3. Puuduvate nimede tuvastamine (NULL ja tühjad tekstid)
SELECT 
    COUNT(*) FILTER (WHERE first_name IS NULL OR first_name = '') AS null_eesnimi,
    COUNT(*) FILTER (WHERE last_name IS NULL OR last_name = '') AS null_perenimi
FROM customers_test;


-- 4. Ebajärjekindlate linnanimede tuvastamine
SELECT 
    city AS algne_linnanimi, 
    COUNT(*) AS klientide_arv
FROM customers_test
GROUP BY city
ORDER BY city;


-- 5. Puuduvate kontaktandmete kontroll (email ja telefon)
SELECT 
    COUNT(*) FILTER (WHERE phone IS NULL OR phone = '') AS null_telefon,
    COUNT(*) FILTER (WHERE email IS NULL OR email = '') AS null_email
FROM customers_test;


-- 6. Puhastatud vaade raporteerimiseks (asendused ja ühtlustamine)
SELECT 
    customer_id,
    COALESCE(first_name, 'Tundmatu') AS first_name,
    COALESCE(last_name, '') AS last_name,
    COALESCE(email, 'puudub') AS email,
    COALESCE(phone, 'puudub') AS phone,
    INITCAP(TRIM(city)) AS clean_city
FROM customers_test;
