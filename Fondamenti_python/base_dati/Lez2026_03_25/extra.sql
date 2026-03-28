#1 Selezionare tutti i fornitori.
 
#2 Mostrare nome e descrizione di tutte le categorie.
 
#3 Trovare i prodotti con quantità in stock maggiore di 50.
 
#4 Elencare i fornitori in ordine alfabetico per ragione sociale.
 
#5 Selezionare i prodotti con prezzo inferiore a 20€.
 
#6 Trovare tutti i fornitori che hanno un'email specificata (non NULL).
 
#7 Mostrare i prodotti il cui nome inizia con la lettera 'S'.
 
#8 Selezionare i 5 prodotti con la quantità in stock più alta.
 
#9 Trovare i prodotti con prezzo unitario superiore alla media dei prezzi.
-- Hint: puoi usare una subquery nella WHERE
 
#10 Calcolare il valore economico di ogni prodotto (prezzo * quantità)
--  e mostrare solo quelli con valore superiore a 1000€, ordinati dal più alto.
 
 
-- ============================================================
-- PARTE 2 — QUERY CON JOIN (Relazioni tra tabelle)
-- ============================================================
 
#11 Visualizzare nome prodotto, nome categoria e città del fornitore
--  per tutti i prodotti.
 
#12 Elencare i prodotti forniti da fornitori di 'Roma'.
 
#13 Mostrare nome prodotto e ragione sociale del fornitore
--  solo per i prodotti esauriti (stock = 0).
 
#14 Trovare i prodotti della categoria 'Abbigliamento'
--  con prezzo inferiore a 50€.
 
#15 Visualizzare nome prodotto, categoria e prezzo
--  ordinati per categoria e poi per prezzo decrescente.
 
#16 Mostrare i fornitori che hanno almeno un prodotto
--  con stock superiore a 100 pezzi.
 
#17 Elencare nome prodotto e ragione sociale del fornitore
--  per i prodotti con prezzo tra 100€ e 300€,
--  ordinati per prezzo crescente.
 
#18 Trovare le categorie che NON hanno nessun prodotto associato.
-- Hint: pensa a quale tipo di JOIN restituisce anche le righe senza corrispondenza.
 
#19 Mostrare nome prodotto, nome categoria e ragione sociale fornitore
--  solo per i prodotti con quantità in stock compresa tra 10 e 50.
 
#20 Trovare i fornitori che forniscono prodotti in più di una categoria.
-- Hint: raggruppa per fornitore e conta le categorie distinte.
 
 
-- ============================================================
-- PARTE 3 — QUERY AVANZATE (Aggregazioni, subquery, logica complessa)
-- ============================================================
 
#21 Calcolare il prezzo medio dei prodotti per ogni fornitore,
--  mostrando solo i fornitori con prezzo medio superiore a 150€.
 
#22 Trovare la categoria con il maggior valore totale di magazzino
--  (somma di prezzo * quantità per ogni categoria).
 
#23 Mostrare per ogni fornitore:
--  ragione sociale, numero di prodotti forniti, prezzo minimo e prezzo massimo.
 
#24 Trovare i prodotti che hanno un prezzo superiore
--  alla media dei prezzi della loro categoria.
-- Hint: subquery correlata nella WHERE.
 
#25 Elencare le categorie e il numero di fornitori distinti
--  che le riforniscono, ordinati per numero di fornitori decrescente.
 
#26 Trovare il prodotto più costoso per ogni fornitore.
-- Hint: stessa logica del "massimo per gruppo" già vista.
 
#27 Mostrare i fornitori che forniscono prodotti in tutte e sole
--  le categorie che hanno almeno 3 prodotti.
-- Hint: prima trova le categorie con almeno 3 prodotti, poi filtra.
 
#28 Calcolare per ogni categoria:
--  nome categoria, numero prodotti, prezzo medio, valore totale magazzino.
--  Mostrare solo le categorie con valore totale superiore a 5000€.
 
#29 Trovare i prodotti che hanno lo stesso prezzo unitario
--  ma appartengono a categorie diverse.
 
#30 Creare una classifica dei fornitori per fatturato potenziale
--  (somma di prezzo * quantità di tutti i loro prodotti),
--  mostrando posizione, ragione sociale e fatturato,
--  ordinati dal più alto al più basso.
-- Hint: usa una subquery o direttamente GROUP BY con ORDER BY.