SELECT empl.area area, empl.empl_cnt empl_cnt, vac.vac_cnt vac_cnt FROM

	(SELECT
		ar.name area,
		COUNT (DISTINCT e.id) empl_cnt
	FROM areas ar
		LEFT JOIN employers e ON ar.id = e.area
	GROUP BY ar.id) as empl
	JOIN
	(SELECT
		ar.name area,
		COUNT (DISTINCT v.id) vac_cnt
	FROM areas ar
		LEFT JOIN vacancies v ON ar.id = v.area_id
	GROUP BY ar.id) as vac
ON empl.area = vac.area
WHERE vac_cnt = 0
ORDER BY empl_cnt DESC
LIMIT 1