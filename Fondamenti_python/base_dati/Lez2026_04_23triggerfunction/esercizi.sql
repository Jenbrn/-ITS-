create database EsercizioSQL;

use EsercizioSQL;

create user esercizio_user@localhost identified by 'password123';

grant all on EsercizioSQL.* to esercizio_user@localhost;

create table Clienti(
id_cliente int primary key auto_increment,
nome varchar(50) not null,
email varchar(100) unique not null
);


#creazione tabelle
create table Prodotti(
id_prodotto int primary key auto_increment,
nome varchar(50) not null,
prezzo decimal(10,2) check (prezzo > 0)
);


create table Ordini(
id_ordine int primary key auto_increment,
id_cliente int not null,
foreign key (id_cliente) references Clienti(id_cliente) on delete cascade,
id_prodotto int not null,
foreign key (id_prodotto) references Prodotti(id_prodotto) on delete cascade,
quantita int not null check (quantita > 0),
data_ordine datetime default current_timestamp

);

#--------------------------------------------------------------------------------
#inserimento
insert into Clienti (nome, email)
values ( 'Alessandrio', 'alessandro.miao@gmail.com' ),
('Gianmarco', 'gian.maio@gmail.com');

insert into Clienti (nome, email)
values ('Tommaso', 'tommaso.miao@gmail.com'),
('Matteo', 'matte.miao@gmail.com');

insert into Prodotti (nome, prezzo)
values ('pizza', 4.50), ('acqua', 2.5);

insert into Ordini (id_cliente, id_prodotto, quantita)
values (1, 1, 5), (2,2,3);

insert into Ordini (id_cliente, id_prodotto, quantita)
values ( 1, 1, 3), (3, 2, 1);

insert into Prodotti ( nome, prezzo)
values ('Laptop', 1000);

#-------------------------------------------------------------------------------------
#lettura
#query 1
select Ordini.id_ordine, Clienti.nome, Prodotti.nome from Ordini
left join Clienti on Ordini.id_cliente = Clienti.id_cliente 
join Prodotti on Prodotti.id_prodotto = Ordini.id_prodotto;

#query 2
select Clienti.nome, count(*) as tot_ordini
from Clienti
join Ordini on Ordini.id_cliente = Clienti.id_cliente
group by Clienti.nome;

#query 3
select Clienti.nome, Ordini.quantita from Clienti
join Ordini on Clienti.id_cliente = Ordini.id_cliente where Ordini.quantita > 1
order by Ordini.quantita desc;

#query 4
select Clienti.nome, sum(Prodotti.prezzo * Ordini.quantita) as totale
from Clienti join Ordini on Clienti.id_cliente = Ordini.id_cliente
join Prodotti on Ordini.id_prodotto = Prodotti.id_prodotto
group by Clienti.nome;

#-------------------------------------------------------------------------------------------
#Update e Delete
#Update 1
update Prodotti 
	join (select id_prodotto from Prodotti where nome = 'Laptop') as P
on Prodotti.id_prodotto = P.id_prodotto
set prezzo = 1300
;

#Delete 2
delete from Clienti
where nome = 'Gianmarco';
# Err code 1175, quando provi a fare update o delete senza una primary_key. Necessario usare tavola derivata + subquery per aggirare il problema (come update1)

delete Clienti from Clienti
	join ( select id_cliente from Clienti where nome = 'Gianmarco') as Cl
on Clienti.id_cliente = Cl.id_cliente;
#Una volta eseguito correttamente il delete sparisce anche l'ordine associato

#Delete 3
delete from Ordini
where id_ordine = 1 ;

#------------------------------------------------------------------------
#Vincoli
insert into Ordini (id_cliente, id_prodotto, quantita)
values (1, 2, -5);
#Impossibile inserire una quantità in conflitto con i vincoli inseriti nel check

#-------------------------------------------------------------------------
#Eliminazione Dati, Tabelle e DB
#1
truncate Ordini;
# or delete from Clienti where id_cliente > 0;
#2
drop table Ordini;
drop table Clienti;
drop table Prodotti;

#3
drop user esercizio_user@localhost;

#4
drop database EsercizioSQL;










