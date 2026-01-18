-- HR Analytics Dashboard - Overall Attrition Analysis
-- Key Metrics: Total employees, attrition rate, average age

SELECT 
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage,
    ROUND(AVG(age), 0) as average_age,
    ROUND(AVG(salary), 0) as average_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary,
    STDDEV(salary) as salary_stddev
FROM hr_analytics_data
WHERE employee_id IS NOT NULL;
