-- Gender-based Attrition Analysis
-- Comparing attrition rates between male and female employees

SELECT 
    gender,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage,
    ROUND(AVG(age), 1) as avg_age,
    ROUND(AVG(salary), 0) as avg_salary
FROM hr_analytics_data
GROUP BY gender
ORDER BY attrition_rate_percentage DESC;
