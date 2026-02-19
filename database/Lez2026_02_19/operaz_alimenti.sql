select * 
from alimenti a
where
#proteine > 10 and proteine < 20;
a.proteine between 10 and 20
and lipidi between 10 and 20
order by energia desc
;

#select * from alimenti as a;
select * from alimenti
where 
prodotto like '%grissini%'
or
prodotto like '%tofu%';

select
(proteine * 0.9) as proteine_grissini,
(carboidrati * 0.9) as carboidrati_grissini,
(lipidi * 0.9) as energia_grissini

from alimenti 
where 
prodotto like '%grissini%'
;

select '90% di grissini' as prodotto,
(proteine * 0.9) as proteine_grissini,
(carboidrati * 0.9) as carboidrati_grissini,
(lipidi * 0.9) as _grissini
from alimenti 
where 
prodotto like '%grissini%'
;

select distinct categoria
from alimenti ;

select * from alimenti
where categoria in ('carne', 'pesce');

select * from alimenti
where categoria not in ('carne', 'pesce');

create table dolci as 
select * from alimenti 
where categoria = 'dolci';

create table dolci_esagerati as 
select * from alimenti
where
categoria = 'dolci'
order by energia desc
limit 10;

select * from alimenti
order by categoria
limit 10, 8;

select * from dolci d
union
select * from dolci_esagerati de;

select a.categoria, count(a.prodotto) as 'Num. Prodotti x Cat'
from alimenti a
group by a.categoria
order by 'Num. Prodotti x Cat' desc;

select a.categoria, count(a.prodotto) as 'Num. Prodotti x Cat',
avg(a.energia) as 'Valore energetico medio'
from alimenti a
group by a.categoria
order by 'AVG(a.energia)' desc;
