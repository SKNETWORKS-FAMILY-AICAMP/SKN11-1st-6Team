SELECT 
    c.city_id,
    c.city_name,
    c.density,
    c.car_amount,
    c.license_population,
    c.population,
	CASE 
        WHEN c.license = 1 THEN '운전면허 필요'
        WHEN c.license = 0 THEN '운전면허 불필요'
        ELSE '알 수 없음'
    END AS license_status,
    v.vehicle_name,
    f.company_name,
    f.question,
    f.answer,
    (c.car_amount / NULLIF(c.density, 0)) AS car_density_ratio
FROM license l
LEFT JOIN city c ON l.is_license = c.license
LEFT JOIN vehicle v ON v.need_license = l.is_license
LEFT JOIN faq f ON v.vehicle_id = f.vehicle_id
ORDER BY car_density_ratio ASC;