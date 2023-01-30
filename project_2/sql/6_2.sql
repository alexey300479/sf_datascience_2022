select count(v.id) vac_cnt
from vacancies v
where
	(lower(v.name) like '%data scientist%' or
	lower(v.name) like '%data science%'  or
	lower(v.name) like '%исследователь данных%' or
	(lower(v.name) like '%ml%' and lower(v.name) not like '%html%') or
	lower(v.name) like '%machine learning%' or
	lower(v.name) like '%машинн%обучен%') and
	(lower(v.name) like '%junior%' or
	 v.experience = 'Нет опыта' or
	 v.employment = 'Стажировка')

