select distinct a.cart_id
from cart_products a
join cart_products b
on a.cart_id = b.cart_id
where a.name = 'Milk' and b.name = 'Yogurt'
order by a.cart_id