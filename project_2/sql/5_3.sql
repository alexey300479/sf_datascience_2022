SELECT
	e.name empl,
	COUNT(DISTINCT v.area_id) ar_cnt
FROM
	employers e
JOIN
	vacancies v ON e.id = v.employer_id
GROUP BY e.id
ORDER BY ar_cnt DESC