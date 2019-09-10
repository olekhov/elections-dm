SELECT p.row_number, p.row_name, p.row_value, p.candidate_id FROM UIK_Protocol p, UIKS u
	WHERE
	u.uik_name LIKE '2424 %' AND
	p.uik_id = u.id
	ORDER BY p.row_order;
