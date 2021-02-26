with recursive
    cte as
    (select 0 as HOUR
    union all
    select HOUR + 1
    from cte
    where HOUR < 23)
select cte.hour, count(ao.animal_id) COUNT
from cte
left join animal_outs ao
on cte.hour = HOUR(ao.datetime)
group by cte.hour