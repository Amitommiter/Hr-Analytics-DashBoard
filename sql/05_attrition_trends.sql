-- Attrition Trends by Department and Technical Background
-- Detailed analysis of attrition patterns

SELECT 
    department,
    technical_background,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage
FROM hr_analytics_data
GROUP BY department, technical_background
HAVING COUNT(*) >= 10
ORDER BY attrition_rate_percentage DESC;
