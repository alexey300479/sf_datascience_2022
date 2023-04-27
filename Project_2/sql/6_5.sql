with skills as (
select (char_length(v.key_skills) - char_length(replace(v.key_skills, chr(9), '')) + 1) skills_cnt
from vacancies v
where
	lower(v.name) like '%data scientist%' or
	lower(v.name) like '%data science%'  or
	lower(v.name) like '%исследователь данных%' or
	(v.name like '%ML%' and not v.name like '%HTML%') or
	lower(v.name) like '%machine learning%' or
	lower(v.name) like '%машинн%обучен%')

select avg(s.skills_cnt) from skills s