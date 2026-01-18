CREATE TABLE IF NOT EXISTS hr_analytics_data (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    department VARCHAR(50),
    job_title VARCHAR(100),
    education VARCHAR(50),
    experience_years INT,
    salary DECIMAL(10, 2),
    attrition VARCHAR(3),
    attrition_date DATE,
    hire_date DATE,
    technical_background VARCHAR(3),
    performance_rating INT,
    work_life_balance INT,
    overtime VARCHAR(3),
    travel_frequently VARCHAR(3),
    training_times_last_year INT
);

CREATE INDEX idx_department ON hr_analytics_data(department);
CREATE INDEX idx_attrition ON hr_analytics_data(attrition);
CREATE INDEX idx_gender ON hr_analytics_data(gender);
CREATE INDEX idx_technical_background ON hr_analytics_data(technical_background);
CREATE INDEX idx_department_attrition ON hr_analytics_data(department, attrition);
CREATE INDEX idx_salary ON hr_analytics_data(salary);
