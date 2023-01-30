elect count(v.id) vac_cnt
from vacancies v
where
	(lower(v.name) like '%data scientist%' or
	lower(v.name) like '%data science%'  or
	lower(v.name) like '%исследователь данных%' or
	(v.name like '%ML%' and not v.name like '%HTML%') or
	lower(v.name) like '%machine learning%' or
	lower(v.name) like '%машинн%обучен%') and
	(lower(v.key_skills) like '%python%')