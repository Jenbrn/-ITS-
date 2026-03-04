use its2026;

#1
select * from its2026.games;
# FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
#2
select nome as Nome_gioco from games;

#3
select nome as Nome_gioco, `year` as anno_pubblicaz from games
where `year` = 2020
order by `year` desc;

#4
select nome nome_gioco, genere as genere
from games
where genere = 'Action'
order by nome;

select nome nome_gioco, genere as genere
from games
where genere like '%Action%'
order by nome;

#5
select nome nome_gioco, publisher editore
from games
where publisher = 'Nintendo'
order by nome;

select nome nome_gioco, publisher editore
from games
where publisher in ('Nintendo')
order by nome;

#6
select nome Nome_gioco, genere Genere, publisher Editore
from games
where genere = "Shoot 'em up" and publisher = 'Atari, Inc.'
order by nome, genere, publisher;

#7
select nome Nome_gioco, platform Piattaforma
from games
where platform like '%PlayStation%'
order by nome;

select nome Nome_gioco, platform Piattaforma
from games
where platform = 'PlayStation'
order by nome;

#8
select nome Nome_gioco, `year` Anno
from games
where `year` < 2000
order by `year` desc;

#9
select distinct genere Genere
from games
order by genere;

select genere Genere
from games
group by genere
order by genere;

#10
select nome Nome_gioco, `year` anno
from games
order by `year` desc;

#11 *
select nome Nome_gioco, genere Genere
from games
where genere not in ('Action', 'Adventure')
order by nome;

#12
select nome Nome_gioco, `year` anno
from games
where `year` between 2000 and 2010
order by `year` asc , nome;

#13
select nome Nome_gioco, publisher Editore, `year` anno
from games
where `year` > 2015
order by publisher, `year`
;

#14
select count(*) as Numero_giochi
from games;

#15
select distinct genere Genere,
	count(*) Giochi_per_genere
from games
group by genere
order by count(*) desc;

#16
select nome Nome_gioco, `year` anno
from games
where `year` = (select max(`year`) from games)
order by `year` desc, nome;

#17
select publisher Editore,
	count(*) as Numero_giochi
from games
group by publisher
order by count(*) desc;

#18
select genere Genere_top,
	count(*) Num_giochi
from games
group by genere
order by count(*) desc
limit 1;

#19
select `year` anno,
	count(*) Giochi_per_anno
from games
group by `year`
order by count(*) desc;

#20
select nome Nome_gioco, 
platform Lista_piattaforme,
( length(platform) - length(replace(platform, ',','' ) ) + 1 ) as Conteggio
from games
having Conteggio > 1
order by Conteggio desc
;

#21
select nome Nome_gioco, `year` anno, publisher Editore,
count(*) Conteggio
from games
group by nome, `year`, publisher
having count(*) > 1
;
select nome Nome_gioco, `year` anno,
count(distinct publisher) as Editori
from games
group by nome, `year`
having count(distinct publisher) > 1
;

#22
select publisher Editore,
count(distinct platform) as Piattaforme_usate
from games
group by publisher
having Piattaforme_usate > 3
order by Piattaforme_usate desc;

#23
select platform Piattaforma, `year` anno,
count(distinct nome) Numero_giochi
from games
group by platform, `year`
having count(distinct nome) > 5
order by count(distinct nome) desc;

#24
select nome Nome_gioco,
count(distinct genere) Num_genrei
from games
group by nome
having count(distinct genere) > 1
;

select nome, group_concat(distinct genere) as generi
from games
group by nome
order by nome;
#ma non c'è nulla :(

#25
select publisher Editore, genere Generi,
count(distinct nome) as numero_giochi
from games
group by publisher, genere
order by count(distinct nome) desc;

select publisher Editore, genere Genere,
count(distinct nome) as numero_giochi
from games
group by publisher, genere
#having ( max( select genere,  
count(distinct nome) as numero_giochi
from games
group by publisher, genere
)
order by count(distinct nome) desc
;

SELECT genere, Publisher, COUNT(*) AS TotalGames
FROM games
GROUP BY genere, Publisher
HAVING COUNT(*) = (
    SELECT MAX(PubCount)
    FROM (
        SELECT Publisher, genere, COUNT(*) AS PubCount
        FROM games
        GROUP BY genere, Publisher
    ) AS SubQuery
    WHERE SubQuery.genere = games.genere
);

select distinct genere, max(tot_giochi) as tot_giochi
from (select genere, publisher, count(*) as tot_giochi from games group by genere, publisher) as tempo
group by genere
order by tot_giochi desc ;


#26

select platform, nome, `year` as anno
from games
where ( platform, `year` )in (
	select platform, min(`year`)
    from games
    group by platform)
order by `year` asc;

#27
SELECT nome, count(*) as quantità
FROM games
GROUP BY nome
HAVING count(*) > 1;


select a.nome, a.genere, a.publisher
from games as a
join games as b on a.nome = b.nome
where a.game_id < b.game_id
and a.genere != b.genere or a.publisher <> b.publisher;

#28
select genere, round((count(*) / ( select count(*) from games) * 100 ), 2) as quant_perc
from games
group by genere
order by quant_perc desc;

#29
select rank() over (order by count(*) desc) as classifica, 
publisher, count(*) as conteggio
from games
group by publisher
order by conteggio desc;

#30
select distinct `year`, genere, max(top) as Lui,
rank() over (order by count(*) desc) as class
 from (select `year`, genere, count(*)as top
from games group by `year`, genere) as conteggio
group by genere, `year`
order by `year` asc
;


#scarabocchi------------------------------------------------------------
select distinct genere, max(top) as Lui
 from (select `year`, genere, count(*)as top
from games group by `year`, genere) as conteggio
group by genere
order by Lui desc
;


select distinct `year`, max(top) as Lui
 from (select `year`, genere, count(*)as top
from games group by `year`, genere) as conteggio
group by `year`
order by Lui desc
;
(select `year`, genere, count(*) as top
from game group by `year`, genere);