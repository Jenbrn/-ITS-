use its2026;

#1
select * from games ;

#2
select nome as 'Nome'
from games;

#3
select nome as 'Game anno 2000',
year as 'anno'
from games
where year = 2000
;

#4
select nome as 'Nome gioco',
genere as 'genere'
from games
where genere = 'action'
order by nome
;

#5
select nome as 'Nome gioco',
publisher as 'Editore'
from games 
where publisher = 'nintendo'
order by nome
;

#6
select nome as  'Nome gioco',
genere as 'Genere',
publisher as 'Editore'
from games
where genere = "Shoot 'em up" and publisher = 'Atari, Inc.'
order by nome, genere, publisher;

#7
select * from games
where platform like '%playstation%'
order by nome
;

select * from games
where platform = 'playstation'
order by nome
;

#8
select * from games
where `year` < 2000
order by `year` desc
;

#9
select genere as 'Genere',
	count(*) 'Quantita'
from games
	group by genere
order by count(genere) desc;

select genere as 'Genere',
	count(*) 'Quantita'
from games
	group by genere
order by count('Quantita') desc;

select genere as 'Genere',
	count(*) 'Generi Top'    
from games
	group by genere
    having count(genere) > 10
order by count('Generi Top') desc;

#10
select nome as 'Nome gioco',
	`year` as 'Anno produzione'
from games
order by `year` asc;
    
#11
select nome as 'Nome gioco',
	genere as 'Genere',
    publisher as 'Produttore'
from games
where genere not in('Action', 'Adventure')
order by nome, genere, publisher
;

#12
select nome as 'Nome gioco',
	`year` as 'Anno produzione'
from games
where `year` between 2000 and 2010
order by `year` asc;

#13
select nome as 'Nome gioco',
	publisher as 'Editore'
from games
where `year` > 2015
order by publisher;

#14
select count(*) from games;

#15
select genere as 'Genere',
	count(genere)
from games
group by genere
order by count(genere)desc;

#16
select nome as 'Nome gioco',
	`year` as 'I giochi più recenti'
from games
where `year` = (select max(`year`) from games);
    
#17
select publisher as 'Editore',
	count(publisher)
from games
group by publisher
order by count(publisher) desc;

#18
select genere as 'Genere top',
count(genere) as 'quantita'
from games
group by genere
order by count(genere) desc
limit 1;

#19
select `year` as 'Anno produzione',
count(*) as 'quant'
from games
group by `year`
order by count(`year`) desc;

#20
select nome as 'Nome Gioco',
platform as 'Lista Piattaforme'
from games
where platform like '%,%'
;

select nome as 'Nome gioco',
platform as 'Lista piattaforme',
( length(platform) - length(replace(platform, ',','') ) + 1 ) as 'Conteggio'
from games
order by Conteggio Desc
;
    
#21
select a.nome, b.nome, a.`year`, b.`year`, a.publisher, b.publisher
from games as a , games as b
where a.nome = b.nome and a.`year` =  b.`year` and a.publisher < b.publisher
;

#22
select publisher as 'editore',
platform as 'Lista piattaforme',
( length(platform) - 
length(replace(platform, ',','') ) + 1 ) as 'Conteggio'
from games
where ( length(platform) - 
length(replace(platform, ',','') ) + 1 ) >= 3
order by Conteggio Desc;
    
#23
select platform as 'piattaforma',
	count(*) as 'giochi per piattaforma',
    `year` as 'anno'
from games
group by platform, `year`
having count(*) > 5
order by platform
;

#24 !!!!!!!
select a.nome, b.nome , a.genere, b.genere
from games as a, games as b
where a.nome = b.nome and a.genere < b.genere
;

select nome as 'nome gioco'
from games
where genere like '%,%'
;

#25
select publisher as 'top',
	genere as 'Tipo di gioco',
	count(*) as 'Giochi pubblicati'
from games
group by publisher, genere
order by genere, count(*) desc, publisher
;

#26

