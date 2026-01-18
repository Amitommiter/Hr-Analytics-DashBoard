import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Data loaded successfully: {len(self.df)} records")
            return self.df
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def validate_data(self):
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        required_columns = ['employee_id', 'attrition', 'age', 'salary', 'department', 
                          'gender', 'technical_background']
        missing_columns = [col for col in required_columns if col not in self.df.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        if self.df.empty:
            raise ValueError("Dataset is empty")
        
        logger.info("Data validation passed")
        return True
    
    def get_basic_stats(self):
        if self.df is None:
            self.load_data()
        
        stats = {
            'total_employees': len(self.df),
            'attrition_rate': (self.df['attrition'] == 'Yes').mean() * 100,
            'average_age': self.df['age'].mean(),
            'average_salary': self.df['salary'].mean()
        }
        return stats
    
    def get_department_attrition(self):
        dept_attrition = self.df.groupby('department').agg({
            'employee_id': 'count',
            'attrition': lambda x: (x == 'Yes').sum()
        }).rename(columns={'employee_id': 'total_employees', 'attrition': 'employees_left'})
        
        dept_attrition['attrition_rate'] = (
            dept_attrition['employees_left'] / dept_attrition['total_employees'] * 100
        ).round(2)
        
        return dept_attrition.sort_values('attrition_rate', ascending=False)
    
    def get_gender_attrition(self):
        gender_attrition = self.df.groupby('gender').agg({
            'employee_id': 'count',
            'attrition': lambda x: (x == 'Yes').sum()
        }).rename(columns={'employee_id': 'total_employees', 'attrition': 'employees_left'})
        
        gender_attrition['attrition_rate'] = (
            gender_attrition['employees_left'] / gender_attrition['total_employees'] * 100
        ).round(2)
        
        return gender_attrition
    
    def get_technical_attrition(self):
        tech_attrition = self.df.groupby('technical_background').agg({
            'employee_id': 'count',
            'attrition': lambda x: (x == 'Yes').sum()
        }).rename(columns={'employee_id': 'total_employees', 'attrition': 'employees_left'})
        
        tech_attrition['attrition_rate'] = (
            tech_attrition['employees_left'] / tech_attrition['total_employees'] * 100
        ).round(2)
        
        return tech_attrition
    
    def get_salary_analysis(self):
        salary_stats = {
            'mean': self.df['salary'].mean(),
            'median': self.df['salary'].median(),
            'min': self.df['salary'].min(),
            'max': self.df['salary'].max(),
            'std': self.df['salary'].std()
        }
        
        salary_by_attrition = self.df.groupby('attrition')['salary'].agg(['mean', 'median', 'count'])
        
        return salary_stats, salary_by_attrition
    
    def get_performance_analysis(self):
        if 'performance_rating' not in self.df.columns:
            return None
        
        perf_attrition = self.df.groupby('performance_rating').agg({
            'employee_id': 'count',
            'attrition': lambda x: (x == 'Yes').sum()
        }).rename(columns={'employee_id': 'total_employees', 'attrition': 'employees_left'})
        
        perf_attrition['attrition_rate'] = (
            perf_attrition['employees_left'] / perf_attrition['total_employees'] * 100
        ).round(2)
        
        return perf_attrition.sort_index()
    
    def get_worklife_balance_analysis(self):
        if 'work_life_balance' not in self.df.columns:
            return None
        
        wlb_attrition = self.df.groupby('work_life_balance').agg({
            'employee_id': 'count',
            'attrition': lambda x: (x == 'Yes').sum()
        }).rename(columns={'employee_id': 'total_employees', 'attrition': 'employees_left'})
        
        wlb_attrition['attrition_rate'] = (
            wlb_attrition['employees_left'] / wlb_attrition['total_employees'] * 100
        ).round(2)
        
        return wlb_attrition.sort_index()
