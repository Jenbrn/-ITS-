use its2026;

#1
select count(*) as tot_alimenti from alimenti;
select count(*) from alimenti;

#2
select avg(proteine) as media_prot
from alimenti;

#3
select max(energia) as energia_max, min(energia) as energia_min 
from alimenti;

#4
select sum(lipidi) as lipidi_tot from alimenti;

#5
select categoria,
count(*) as num_alimeti
from alimenti
group by categoria;

#6
select categoria,
avg(carboidrati) as media_carb from alimenti
group by categoria;

#7
select categoria,
avg(energia) as energia_media from alimenti
group by categoria
order by energia_media desc
limit 1;

#select categoria, 
#from alimenti 
#where energia = (select max(avg(energia))from alimenti)
#group by categoria

#;
 #select categoria from alimenti where max((select avg(energia) from alimenti));

#8
select * from alimenti
order by proteine desc
limit 1;

select prodotto, proteine
from alimenti
where proteine = (select max(proteine) from alimenti);

#9
select categoria,
sum(energia) as energia_tot
from alimenti
group by categoria;

#10
select categoria, count(*) as alimenti_pro from alimenti where proteine > 10 group by categoria;
#come mai?

select count(*) as alimenti_pro
from alimenti
where proteine > 10;

select categoria, max(energia) 
from( select categoria, avg(energia) as energia from alimenti group by categoria)
as miao 
group by categoria
order by energia desc
limit 1;

