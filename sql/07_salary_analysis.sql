-- Salary Analysis and Attrition Correlation
-- Analyzing salary distribution and its impact on employee retention

-- Salary Ranges vs Attrition
SELECT 
    CASE 
        WHEN salary < 60000 THEN 'Under 60K'
        WHEN salary BETWEEN 60000 AND 80000 THEN '60K-80K'
        WHEN salary BETWEEN 80000 AND 100000 THEN '80K-100K'
        WHEN salary BETWEEN 100000 AND 120000 THEN '100K-120K'
        ELSE 'Over 120K'
    END as salary_range,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage,
    ROUND(AVG(salary), 0) as avg_salary_in_range
FROM hr_analytics_data
GROUP BY 
    CASE 
        WHEN salary < 60000 THEN 'Under 60K'
        WHEN salary BETWEEN 60000 AND 80000 THEN '60K-80K'
        WHEN salary BETWEEN 80000 AND 100000 THEN '80K-100K'
        WHEN salary BETWEEN 100000 AND 120000 THEN '100K-120K'
        ELSE 'Over 120K'
    END
ORDER BY avg_salary_in_range;
