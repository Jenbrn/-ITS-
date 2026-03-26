use magazzino;


# Selezionare tutti i prodotti.
select * from prodotti;

# Selezionare nome e prezzo dei prodotti con prezzo superiore a 100€.
select nome, prezzo_unitario from prodotti where prezzo_unitario > 200;

# Elencare i fornitori di Milano.
select * from fornitori;
select ragione_sociale, citta from fornitori where citta = 'Milano';

# Trovare i prodotti con quantità in stock pari a 0 (esauriti).
select nome, quantita_stock from prodotti where quantita_stock = 0;

# Selezionare i prodotti che contengono la parola 'Laptop' nel nome.
select * from prodotti where nome like '%laptop%';

# Elencare le categorie in ordine alfabetico.
select * from categorie;
select nome from categorie order by nome asc;

# Trovare i prodotti con prezzo compreso tra 50€ e 500€.
select nome, prezzo_unitario from prodotti where prezzo_unitario between 50 and 500 order by prezzo_unitario asc;

# Mostrare i fornitori che non hanno un'email specificata (se fosse NULL).
select ragione_sociale from fornitori where email is NULL;

# Selezionare i primi 3 prodotti più costosi.
select * from prodotti order by prezzo_unitario desc limit 3;

# Calcolare il valore totale della merce (prezzo * quantità) per ogni prodotto.
select nome, (prezzo_unitario * quantita_stock) as valore_totale from prodotti order by valore_totale desc;

# Query con Join (Relazioni tra tabelle)
# Visualizzare nome prodotto e nome della relativa categoria.
select prodotti.nome, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria;

# Elencare i prodotti insieme alla ragione sociale del loro fornitore.
select prodotti.nome, fornitori.ragione_sociale from prodotti join fornitori order by fornitori.ragione_sociale;

#### Trovare tutti i prodotti della categoria 'Elettronica'.
select prodotti.nome, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria where categorie.nome = 'elettronica'; 

# Mostrare i prodotti forniti da 'TechSpA'.
select prodotti.nome, fornitori.ragione_sociale from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore where fornitori.ragione_sociale = 'TechSpA';

# Elencare i nomi dei prodotti e le città dei loro fornitori.
select prodotti.nome, fornitori.citta from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore order by fornitori.citta;

# Visualizzare i prodotti della categoria 'Arredamento' con stock > 0.
select prodotti.nome, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria where prodotti.quantita_stock > 0 and categorie.nome = 'arredamento';

# Mostrare le categorie che hanno almeno un prodotto fornito da un fornitore di 'Torino'.
select categorie.nome, ( select prodotti.nome, prodotti.id_prodotto from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore where fornitori.citta = 'Torino') as torino from prodotti;


select prodotti.nome, prodotti.id_prodotto from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore where fornitori.citta = 'Torino';
# Visualizzare i prodotti (nome) e il fornitore, ma solo se il prezzo è > 200€.
# Lista completa: Nome Prodotto, Categoria, Fornitore.
# Trovare i nomi dei fornitori che forniscono prodotti nella categoria 'Elettronica'.
# Query di Aggregazione e Funzioni (Statistiche)
# Contare quanti prodotti ci sono in totale nel database.
# Calcolare il prezzo medio dei prodotti.
# Calcolare la somma totale degli articoli in magazzino.
# Trovare il prezzo massimo per ogni categoria.
# Contare quanti prodotti fornisce ogni fornitore.
# Calcolare il valore totale economico del magazzino intero.
# Mostrare le categorie che hanno più di 2 prodotti.
# Trovare il fornitore che ha il prodotto più economico.
# Calcolare la media dei prezzi dei prodotti per il fornitore 'TechSpA'.
# Visualizzare le categorie e il numero di pezzi totali (somma stock) per ognuna.
# Esempio di risoluzione (Query 25 & 27)
# Se vuoi testare la logica più complessa:
#
# -- Query 25: Numero prodotti per fornitore
# SELECT F.ragione_sociale, COUNT(P.id_prodotto) AS Totale_Prodotti
# FROM Fornitori F
# LEFT JOIN Prodotti P ON F.id_fornitore = P.id_fornitore
# GROUP BY F.ragione_sociale;
#
# -- Query 27: Categorie con più di 2 prodotti
# SELECT C.nome, COUNT(P.id_prodotto)
# FROM Categorie C
# JOIN Prodotti P ON C.id_categoria = P.id_categoria
# GROUP BY C.nome
# HAVING COUNT(P.id_prodotto) > 2;
