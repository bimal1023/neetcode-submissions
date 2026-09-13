-- Write your query below
select employee_id, CASE when employee_id%2!=0 and name NOT LIKE 'M%'
then salary else 0 end as bonus
from employees order by
employee_id;