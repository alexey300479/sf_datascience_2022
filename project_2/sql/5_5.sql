SELECT
	e.name empl,
	COUNT(DISTINCT i.industry_id) ind_cnt
FROM
	employers e
LEFT JOIN
	employers_industries i ON e.id = i.employer_id
GROUP BY e.id
HAVING COUNT(DISTINCT i.industry_id) = 4
ORDER BY empl
OFFSET 2
LIMIT 1