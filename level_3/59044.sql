select name, datetime
from(select ai.name, ai.datetime, row_number() over(order by ai.datetime) rnum
    from animal_ins ai
    left join animal_outs ao
    on ai.animal_id = ao.animal_id
    where ao.animal_id is null) sub
where rnum < 4