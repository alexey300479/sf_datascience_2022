select count(v.id) vac_cnt
from vacancies v
where
	(lower(v.name) like '%data scientist%' or
	lower(v.name) like '%data science%'  or
	lower(v.name) like '%исследователь данных%' or
	(v.name like '%ML%' and v.name not like '%HTML%') or
	lower(v.name) like '%machine learning%' or
	lower(v.name) like '%машинн%обучен%') and
	(v.key_skills like '%SQL%' or
	 lower(v.key_skills) like '%postgres%')

