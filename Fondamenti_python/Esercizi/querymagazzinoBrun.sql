use magazzino;


#1 Selezionare tutti i prodotti.
select * from prodotti;

#2 Selezionare nome e prezzo dei prodotti con prezzo superiore a 100€.
select nome, prezzo_unitario from prodotti where prezzo_unitario > 200;

#3 Elencare i fornitori di Milano.
select ragione_sociale, citta from fornitori where citta = 'Milano';

#4 Trovare i prodotti con quantità in stock pari a 0 (esauriti).
select nome, quantita_stock from prodotti where quantita_stock = 0;

#5 Selezionare i prodotti che contengono la parola 'Laptop' nel nome.
select * from prodotti where nome like '%laptop%';

#6 Elencare le categorie in ordine alfabetico.
select nome from categorie order by nome asc;

#7 Trovare i prodotti con prezzo compreso tra 50€ e 500€.
select nome, prezzo_unitario from prodotti where prezzo_unitario between 50 and 500 order by prezzo_unitario asc;

#8 Mostrare i fornitori che non hanno un'email specificata (se fosse NULL).
select ragione_sociale from fornitori where email is NULL;

#9 Selezionare i primi 3 prodotti più costosi.
select * from prodotti order by prezzo_unitario desc limit 3;

#10 Calcolare il valore totale della merce (prezzo * quantità) per ogni prodotto.
select nome, (prezzo_unitario * quantita_stock) as valore_totale from prodotti order by valore_totale desc;

#Query con Join (Relazioni tra tabelle)

#11 Visualizzare nome prodotto e nome della relativa categoria.
select prodotti.nome, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria;

#12 Elencare i prodotti insieme alla ragione sociale del loro fornitore.
select prodotti.nome, fornitori.ragione_sociale from prodotti join fornitori order by fornitori.ragione_sociale;

#13 Trovare tutti i prodotti della categoria 'Elettronica'.
select prodotti.nome, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria where categorie.nome = 'elettronica'; 

#14 Mostrare i prodotti forniti da 'TechSpA'.
select prodotti.nome, fornitori.ragione_sociale from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore where fornitori.ragione_sociale = 'TechSpA';

#15 Elencare i nomi dei prodotti e le città dei loro fornitori.
select prodotti.nome, fornitori.citta from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore order by fornitori.citta;

#16 Visualizzare i prodotti della categoria 'Arredamento' con stock > 0.
select prodotti.nome, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria where prodotti.quantita_stock > 0 and categorie.nome = 'arredamento';

#17 Mostrare le categorie che hanno almeno un prodotto fornito da un fornitore di 'Torino'.
select categorie.nome from categorie
join (select prodotti.id_categoria, fornitori.ragione_sociale from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore
	where fornitori.citta = 'Torino') as torino on categorie.id_categoria = torino.id_categoria ;

#18 Visualizzare i prodotti (nome) e il fornitore, ma solo se il prezzo è > 200€.
select prodotti.nome, fornitori.ragione_sociale from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore where prodotti.prezzo_unitario > 200;

#19 Lista completa: Nome Prodotto, Categoria, Fornitore.
select prodotti.nome, categorie.nome, fornitori.ragione_sociale from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria 
join fornitori on fornitori.id_fornitore = prodotti.id_fornitore
order by categorie.nome, fornitori.ragione_sociale
;

#20 Trovare i nomi dei fornitori che forniscono prodotti nella categoria 'Elettronica'.
select distinct fornitori.ragione_sociale as fornitore from fornitori join 
	(select prodotti.id_fornitore, categorie.nome from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria 
    where categorie.nome = 'Elettronica') as elettronica on elettronica.id_fornitore = fornitori.id_fornitore
;

# Query di Aggregazione e Funzioni (Statistiche)

#21 Contare quanti prodotti ci sono in totale nel database.
select count(*) as totale_prodotti from prodotti;

#22 Calcolare il prezzo medio dei prodotti.
select avg(prezzo_unitario) as prezzo_medio from prodotti;

#23 Calcolare la somma totale degli articoli in magazzino.
select sum(quantita_stock) as num_tot_prodotti from prodotti;

#24 Trovare il prezzo massimo per ogni categoria.
select categorie.nome , max(prodotti.prezzo_unitario) as prezzo_max from prodotti join categorie 
on prodotti.id_categoria = categorie.id_categoria
group by categorie.nome
order by prezzo_max asc
;

#25 Contare quanti prodotti fornisce ogni fornitore.
select fornitori.ragione_sociale as nome_fornitore, count(prodotti.quantita_stock) as pezzi_forniti
from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore
group by fornitori.ragione_sociale
order by pezzi_forniti asc
;

#26 Calcolare il valore totale economico del magazzino intero.
select sum(prezzo_unitario) as totale from prodotti;

#27 Mostrare le categorie che hanno più di 2 prodotti.
select categorie.nome from categorie join prodotti on prodotti.id_categoria = categorie.id_categoria 
group by categorie.nome
having count(*) > 2;

#28 Trovare il fornitore che ha il prodotto più economico.
select fornitori.ragione_sociale, min(prodotti.prezzo_unitario) as prezzo_minimo from prodotti
join fornitori on prodotti.id_fornitore = fornitori.id_fornitore
group by fornitori.ragione_sociale
order by prezzo_minimo asc limit 1
;

#29 Calcolare la media dei prezzi dei prodotti per il fornitore 'TechSpA'.
select  fornitori.ragione_sociale, avg(prodotti.prezzo_unitario) as media_prezzo
from prodotti join fornitori on prodotti.id_fornitore = fornitori.id_fornitore
where fornitori.ragione_sociale = 'TechSpA'
;

#30 Visualizzare le categorie e il numero di pezzi totali (somma stock) per ognuna.
select categorie.nome, sum(prodotti.prezzo_unitario) as valore_tot
from prodotti join categorie on prodotti.id_categoria = categorie.id_categoria
group by categorie.nome
order by valore_tot asc;

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
 SELECT C.nome, COUNT(P.id_prodotto)
 FROM Categorie C
 JOIN Prodotti P ON C.id_categoria = P.id_categoria
 GROUP BY C.nome
 HAVING COUNT(P.id_prodotto) > 2;
#27 Mostrare le categorie che hanno più di 2 prodotti.
select categorie.nome from categorie join prodotti on prodotti.id_categoria = categorie.id_categoria 
group by categorie.nome
having count(*) > 2;






