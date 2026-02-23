use its2026;
#1
Select * from alimenti;

#2
select * from alimenti where categoria = 'carne';

#3
select count(*) as num_alimenti from alimenti;

#4
select * from alimenti where proteine > 10 order by proteine desc;

#5
select * from alimenti
order by energia desc
limit 10;

#6
select avg(proteine) as prot_medie 
from alimenti 
where categoria = 'carne';

#7
select * from alimenti where carboidrati = 0;

#8
select max(lipidi) as il_piu_grasso from alimenti;
select * from alimenti order by lipidi desc limit 1;

#9
select categoria, 
count(*) as quantita_sottogruppi
from alimenti
group by categoria;

#10
select * from alimenti where carboidrati between 10 and 30 order by carboidrati desc;


