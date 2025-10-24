# HR Analytics Dashboard

A comprehensive HR analytics project using SQL and Power BI to analyze employee attrition patterns and workforce metrics.

## Project Overview

This dashboard analyzes key HR metrics for a workforce of over 1,400 employees, uncovering critical insights about employee retention and attrition patterns. The analysis reveals significant findings including an overall attrition rate of 16.12%, department-specific trends, and demographic patterns that inform strategic HR decisions.

## Key Findings

### Overall Metrics
- **Total Workforce**: 1,400+ employees
- **Overall Attrition Rate**: 16.12%
- **Average Employee Age**: 37 years
- **Average Salary**: $78,500

### Critical Insights
1. **Department Attrition Patterns**: R&D department shows the highest attrition rate at 56%
2. **Technical Background Impact**: 24% of employees with technical backgrounds experience attrition
3. **Gender-based Analysis**: Female attrition rate (14.8%) vs Male attrition rate (17%)

## Project Structure

```
├── data/
│   └── hr_analytics_data.csv          # Complete employee dataset
├── sql/
│   ├── 01_attrition_overview.sql      # Overall attrition analysis
│   ├── 02_department_attrition.sql    # Department-wise analysis
│   ├── 03_technical_background_attrition.sql  # Technical background impact
│   ├── 04_gender_attrition.sql        # Gender-based analysis
│   ├── 05_attrition_trends.sql        # Detailed trend analysis
│   ├── 06_advanced_analytics.sql      # Performance and work-life balance
│   └── 07_salary_analysis.sql         # Salary correlation analysis
├── powerbi/
│   ├── dashboard_requirements.md      # Dashboard specifications
│   ├── power_query_script.txt        # Data transformation script
│   └── measures.txt                   # DAX measures for calculations
└── documentation/
    └── analysis_insights.md           # Detailed analysis findings
```

## Data Analysis Approach

### SQL Analysis
The SQL queries provide comprehensive analysis of:
- Overall attrition metrics and trends
- Department-specific attrition patterns
- Gender-based retention analysis
- Technical background impact on retention
- Performance and work-life balance correlations
- Salary distribution and attrition relationships

### Power BI Dashboard
Interactive visualizations include:
- Executive summary with key metrics
- Department-wise attrition comparison charts
- Gender-based retention analysis
- Technical vs non-technical employee trends
- Performance rating distributions
- Salary range analysis
- Work-life balance impact assessment

## Technical Implementation

### Data Sources
- Employee demographics and personal information
- Department and job role classifications
- Performance ratings and work-life balance scores
- Salary and compensation data
- Training and development metrics
- Attrition tracking with exit dates

### Analytics Tools
- **SQL**: Data extraction and statistical analysis
- **Power BI**: Interactive dashboard creation and visualization
- **Statistical Analysis**: Correlation analysis and trend identification

## Business Impact

This analysis enables HR teams to:
1. **Identify High-Risk Departments**: Focus retention efforts on R&D and technical teams
2. **Develop Targeted Strategies**: Create specific retention programs for technical employees
3. **Address Gender Disparities**: Implement policies to improve female employee retention
4. **Optimize Compensation**: Use salary analysis to inform compensation strategies
5. **Improve Work-Life Balance**: Address factors contributing to employee satisfaction

## Usage Instructions

1. **Data Import**: Load the CSV data file into your preferred SQL database
2. **SQL Analysis**: Execute the SQL queries to generate analytical insights
3. **Power BI Setup**: Import the data and apply the provided DAX measures
4. **Dashboard Creation**: Follow the dashboard requirements to build interactive visualizations

## Key Metrics Tracked

- Employee count and distribution
- Attrition rates by department, gender, and technical background
- Performance rating distributions
- Work-life balance scores
- Salary ranges and compensation trends
- Training participation rates
- Experience level analysis

This project demonstrates proficiency in data analysis, SQL querying, and business intelligence visualization using Power BI.
