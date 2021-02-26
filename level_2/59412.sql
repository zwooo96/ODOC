select substr(datetime, 12, 2) HOUR, count(*) count
from animal_outs
group by HOUR
having HOUR between 09 and 19
order by HOUR