with city_vac_cnt as (
select a.name, COUNT(v.id) cnt
from vacancies v
join areas a on a.id = v.area_id
where v.employer_id in
	(select e.id
	from employers e
	where e.name = 'Яндекс')
	and
	v.area_id in
	(SELECT a.id
	 FROM areas a
	 where a.name in (VALUES
	 ('Москва'),
	 ('Санкт-Петербург'),
	 ('Новосибирск'),
	 ('Екатеринбург'),
	 ('Казань'),
	 ('Нижний Новгород'),
	 ('Челябинск'),
	 ('Красноярск'),
	 ('Самара'),
	 ('Уфа'),
	 ('Ростов-на-Дону'),
	 ('Омск'),
	 ('Краснодар'),
	 ('Воронеж'),
	 ('Пермь'),
	 ('Волгоград')))
group by a.name)

(select * from city_vac_cnt)
union
(select 'Total', sum(city_vac_cnt.cnt) from city_vac_cnt)
order by 2