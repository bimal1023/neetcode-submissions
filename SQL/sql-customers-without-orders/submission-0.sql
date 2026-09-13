-- Write your query below
select name from customers where customers.id NOT in (select customer_id from orders);