select name
from (select name, row_number() over(order by datetime) num
    from animal_ins) sub
where num = 1