select 
	`year` as 'Anno pubblicazione',
	count(nome) 'Numero giochi'
from games g
group by `year`
order by `year`;

select 
	`year` as 'Anno pubblicazione',
	count(nome) 'Numero giochi'
from games g
group by `year`
order by count(nome) desc
limit 10, 10;

select 
	publisher as 'Publisher',
	count(nome) 'Numero giochi'
from games g
group by publisher
order by count(nome) desc
limit 100;

select 
	platform as 'Platform',
    publisher as 'Publisher',
	count(nome) 'Numero giochi'
from games g
group by platform, publisher
order by count(nome) desc, platform
limit 100;