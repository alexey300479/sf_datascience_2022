SELECT COUNT(DISTINCT empl_ind.empl)
FROM
	(SELECT
		ei.employer_id empl,
		i.name ind
	FROM
		employers_industries ei
	JOIN
		industries i ON ei.industry_id = i.id
	WHERE i.name='Разработка программного обеспечения') as empl_ind
