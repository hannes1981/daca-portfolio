{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red36\green36\blue36;\red239\green236\blue236;}
{\*\expandedcolortbl;;\cssrgb\c18824\c18824\c18824;\cssrgb\c94902\c94118\c94118;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28260\viewh14180\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\pard\pardeftab720\partightenfactor0

\f1\fs28 \cf \cb3 \expnd0\expndtw0\kerning0
-- =====================================================\
-- DACA N\'e4dal 1: Sales Data Explorer (Roll A)\
-- Fail: week1_sales_exploration.sql\
-- =====================================================\
\
-- 1. Mitu rida on sales tabelis kokku?\
SELECT COUNT(*) AS ridade_arv \
FROM sales;\
\
-- 2. Tallinna kaupluse viimased m\'fc\'fcgid\
SELECT sale_id, invoice_id, sale_date, total_price, store_location \
FROM sales \
WHERE store_location = 'Tallinn' \
ORDER BY sale_date DESC \
LIMIT 15;\
\
-- 3. Suurimad m\'fc\'fcgitehingud\
SELECT sale_id, invoice_id, total_price, sale_date \
FROM sales \
ORDER BY total_price DESC \
LIMIT 10;\
\
-- 4. V\'e4ikseimad ja negatiivsed tehingud (tagastused)\
SELECT sale_id, invoice_id, total_price, sale_date \
FROM sales \
ORDER BY total_price ASC \
LIMIT 10;\
\
-- 5. Ilma kliendita m\'fc\'fcgid (puuduv customer_id)\
SELECT COUNT(*) AS ilma_kliendita_muugid \
FROM sales \
WHERE customer_id IS NULL;}