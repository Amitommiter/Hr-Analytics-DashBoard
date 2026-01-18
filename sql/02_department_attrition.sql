-- Department-wise Attrition Analysis
-- Identifying departments with highest attrition rates

SELECT 
    department,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage,
    ROUND(AVG(age), 1) as avg_age,
    ROUND(AVG(salary), 0) as avg_salary,
    ROUND(AVG(experience_years), 1) as avg_experience
FROM hr_analytics_data
WHERE department IS NOT NULL
GROUP BY department
ORDER BY attrition_rate_percentage DESC;
