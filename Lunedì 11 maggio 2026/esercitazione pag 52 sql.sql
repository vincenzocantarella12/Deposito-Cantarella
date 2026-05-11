
-- ESERCIZIO SQL - JOIN LIBRI E VENDITE



-- ESERCIZIO 1 – INNER JOIN + WHERE + LIKE
-- Libri venduti con autore che contiene "King"


SELECT 
    l.titolo,
    l.autore,
    v.data_vendita,
    v.negozio
FROM Libri l
INNER JOIN Vendite v 
    ON l.id = v.id_libro
WHERE LOWER(l.autore) LIKE '%king%';



-- ESERCIZIO 2 – LEFT JOIN + WHERE + BETWEEN
-- Tutti i libri pubblicati tra il 2000 e il 2010


SELECT 
    l.titolo,
    l.anno_pubblicazione,
    l.prezzo,
    v.data_vendita
FROM Libri l
LEFT JOIN Vendite v 
    ON l.id = v.id_libro
WHERE l.anno_pubblicazione BETWEEN 2000 AND 2010;



-- ESERCIZIO 3 – INNER JOIN + WHERE + IN
-- Vendite in negozi specifici + prezzo totale


SELECT 
    l.titolo,
    v.negozio,
    v.quantita,
    (v.quantita * l.prezzo) AS prezzo_totale
FROM Libri l
INNER JOIN Vendite v 
    ON l.id = v.id_libro
WHERE v.negozio IN (
    '9 Oriole Lane',
    '98558 Milwaukee Point',
    '98016 Esch Trail'
);



-- ESERCIZIO 4 – RIGHT JOIN + WHERE + LIKE + BETWEEN
-- Vendite anche senza libro corrispondente


SELECT 
    l.titolo,
    v.data_vendita,
    l.prezzo,
    v.quantita
FROM Libri l
RIGHT JOIN Vendite v 
    ON l.id = v.id_libro
WHERE v.data_vendita BETWEEN '2020-01-01' AND '2022-12-31'
  AND LOWER(v.negozio) LIKE '%drive%';



-- ESERCIZIO 5 – INNER JOIN + WHERE + ORDER BY
-- Libri Fantasy pubblicati dopo il 2015
-- venduti in negozi contenenti "Plaza"


SELECT 
    l.titolo,
    l.autore,
    l.prezzo,
    v.data_vendita,
    v.negozio
FROM Libri l
INNER JOIN Vendite v 
    ON l.id = v.id_libro
WHERE l.genere = 'Fantasy'
  AND l.anno_pubblicazione > 2015
  AND v.negozio LIKE '%Plaza%'
ORDER BY v.data_vendita DESC;