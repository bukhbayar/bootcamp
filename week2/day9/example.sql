select
	e.id as employee_id,
	e.name as employee_name,
	e.age,
	c.name as country_name,
	d.name as department_name,
	p.review_score,
	p.tenure_years,
	p.seniority
from employee as e
left join country c on c.country_id = e.country_id
left join department as d on d.department_id = e.department_id
left join performance p on p.employee_id = e.id
-- where c.name = 'Australia'
