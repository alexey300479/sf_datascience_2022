select count(v.id) vac_cnt
from vacancies v
where lower(v.name) like '%data%' or lower(v.name) like '%данн%'
