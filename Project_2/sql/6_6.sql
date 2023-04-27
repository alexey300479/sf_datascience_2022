with ds_vacs as (
	select v.experience, v.salary_from, v.salary_to
	from vacancies v
	where (v.salary_from is not null or v.salary_to is not null) and
	  (lower(v.name) like '%data scientist%' or
	   lower(v.name) like '%data science%'  or
	   lower(v.name) like '%исследователь данных%' or
	   (v.name like '%ML%' and not v.name like '%HTML%') or
	   lower(v.name) like '%machine learning%' or
	   lower(v.name) like '%машинн%обучен%'))

select v.experience, AVG(COALESCE((v.salary_from + v.salary_to) / 2, v.salary_from, v.salary_to)) avg_salary
from ds_vacs v
group by v.experience