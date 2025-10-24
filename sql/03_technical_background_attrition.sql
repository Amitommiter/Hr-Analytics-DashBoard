-- Technical Background vs Attrition Analysis
-- Analyzing attrition patterns for employees with technical backgrounds

SELECT 
    technical_background,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage
FROM hr_analytics_data
GROUP BY technical_background
ORDER BY attrition_rate_percentage DESC;
