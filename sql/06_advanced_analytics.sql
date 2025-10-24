-- Advanced HR Analytics Queries
-- Performance, work-life balance, and other factors affecting attrition

-- Performance Rating vs Attrition
SELECT 
    performance_rating,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage
FROM hr_analytics_data
GROUP BY performance_rating
ORDER BY performance_rating;

-- Work-Life Balance vs Attrition
SELECT 
    work_life_balance,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage
FROM hr_analytics_data
GROUP BY work_life_balance
ORDER BY work_life_balance;

-- Overtime and Travel Impact on Attrition
SELECT 
    overtime,
    travel_frequently,
    COUNT(*) as total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) as employees_left,
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as attrition_rate_percentage
FROM hr_analytics_data
GROUP BY overtime, travel_frequently
ORDER BY attrition_rate_percentage DESC;
