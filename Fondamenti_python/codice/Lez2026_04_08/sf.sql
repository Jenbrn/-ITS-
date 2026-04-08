select * from employee e;

select 
	a.EmployeeId, a.FirstName, a.LastName, a.Title, 
    concat(b.FirstName, ' ', b.LastName) as responsaile
from employee a
left join employee b on a.ReportsTo = b.EmployeeId
where a.ReportsTo is null
;