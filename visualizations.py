import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import config

sns.set_style("whitegrid")
plt.style.use(config.CHART_STYLE["style"])

class Visualizations:
    def __init__(self):
        self.colors = config.COLORS
    
    def create_kpi_cards(self, stats):
        fig, axes = plt.subplots(1, 4, figsize=(20, 6))
        fig.suptitle('Key Performance Indicators', fontsize=16, fontweight='bold')
        
        kpis = [
            ('Total Employees', stats['total_employees'], f"{stats['total_employees']:,}", self.colors['primary']),
            ('Attrition Rate', stats['attrition_rate'], f"{stats['attrition_rate']:.2f}%", self.colors['secondary']),
            ('Average Age', stats['average_age'], f"{stats['average_age']:.1f}", self.colors['success']),
            ('Average Salary', stats['average_salary'], f"${stats['average_salary']:,.0f}", self.colors['warning'])
        ]
        
        for idx, (title, value, display, color) in enumerate(kpis):
            axes[idx].text(0.5, 0.5, display, ha='center', va='center', 
                          fontsize=24, fontweight='bold', color=color)
            axes[idx].text(0.5, 0.2, title, ha='center', va='center', 
                          fontsize=12, color='gray')
            axes[idx].set_xlim(0, 1)
            axes[idx].set_ylim(0, 1)
            axes[idx].axis('off')
        
        plt.tight_layout()
        return fig
    
    def plot_department_attrition(self, dept_data):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        dept_data_sorted = dept_data.sort_values('attrition_rate', ascending=True)
        bars = ax.barh(dept_data_sorted.index, dept_data_sorted['attrition_rate'], 
                       color=self.colors['primary'], alpha=0.7)
        
        for i, (idx, row) in enumerate(dept_data_sorted.iterrows()):
            ax.text(row['attrition_rate'] + 0.5, i, f"{row['attrition_rate']:.1f}%", 
                   va='center', fontweight='bold')
        
        ax.set_title('Attrition Rate by Department', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Attrition Rate (%)', fontsize=12)
        ax.set_ylabel('Department', fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    def plot_gender_attrition(self, gender_data, gender_dist):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        colors = ['#ff9999', '#66b3ff']
        ax1.pie(gender_dist.values, labels=gender_dist.index, autopct='%1.1f%%', 
               colors=colors, startangle=90)
        ax1.set_title('Gender Distribution', fontsize=14, fontweight='bold')
        
        bars = ax2.bar(gender_data.index, gender_data['attrition_rate'], 
                      color=colors, alpha=0.7)
        ax2.set_title('Attrition Rate by Gender', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Attrition Rate (%)')
        ax2.set_ylim(0, max(gender_data['attrition_rate']) * 1.2)
        
        for i, (idx, row) in enumerate(gender_data.iterrows()):
            ax2.text(i, row['attrition_rate'] + 0.2, f"{row['attrition_rate']:.1f}%", 
                    ha='center', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def plot_technical_attrition(self, tech_data, tech_dist):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        colors = ['#ff9999', '#66b3ff']
        ax1.pie(tech_dist.values, labels=tech_dist.index, autopct='%1.1f%%', 
               colors=colors, startangle=90)
        ax1.set_title('Technical Background Distribution', fontsize=14, fontweight='bold')
        
        bars = ax2.bar(tech_data.index, tech_data['attrition_rate'], 
                      color=colors, alpha=0.7)
        ax2.set_title('Attrition Rate by Technical Background', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Attrition Rate (%)')
        ax2.set_ylim(0, max(tech_data['attrition_rate']) * 1.2)
        
        for i, (idx, row) in enumerate(tech_data.iterrows()):
            ax2.text(i, row['attrition_rate'] + 0.5, f"{row['attrition_rate']:.1f}%", 
                    ha='center', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def plot_salary_distribution(self, df):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.hist(df['salary'], bins=20, color=self.colors['success'], alpha=0.7, edgecolor='black')
        mean_salary = df['salary'].mean()
        ax.axvline(mean_salary, color='red', linestyle='--', linewidth=2, 
                  label=f'Mean: ${mean_salary:,.0f}')
        
        ax.set_title('Salary Distribution', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Salary ($)', fontsize=12)
        ax.set_ylabel('Number of Employees', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        ax.legend()
        
        plt.tight_layout()
        return fig
    
    def create_interactive_dashboard(self, df, stats, dept_data, gender_data, tech_data):
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=('Department Attrition Rate', 'Gender Attrition Comparison',
                          'Technical Background Attrition', 'Salary Distribution',
                          'Age Distribution', 'Performance Rating Distribution'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "histogram"}],
                   [{"type": "histogram"}, {"type": "bar"}]]
        )
        
        dept_data_sorted = dept_data.sort_values('attrition_rate', ascending=True)
        fig.add_trace(
            go.Bar(x=dept_data_sorted['attrition_rate'], y=dept_data_sorted.index,
                  orientation='h', name='Department', marker_color=self.colors['primary']),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(x=gender_data.index, y=gender_data['attrition_rate'],
                  name='Gender', marker_color=['#ff9999', '#66b3ff']),
            row=1, col=2
        )
        
        fig.add_trace(
            go.Bar(x=tech_data.index, y=tech_data['attrition_rate'],
                  name='Technical', marker_color=['#ff9999', '#66b3ff']),
            row=2, col=1
        )
        
        fig.add_trace(
            go.Histogram(x=df['salary'], nbinsx=20, name='Salary',
                        marker_color=self.colors['success']),
            row=2, col=2
        )
        
        fig.add_trace(
            go.Histogram(x=df['age'], nbinsx=15, name='Age',
                        marker_color=self.colors['warning']),
            row=3, col=1
        )
        
        if 'performance_rating' in df.columns:
            perf_dist = df['performance_rating'].value_counts().sort_index()
            fig.add_trace(
                go.Bar(x=perf_dist.index, y=perf_dist.values, name='Performance',
                      marker_color=self.colors['info']),
                row=3, col=2
            )
        
        fig.update_layout(
            height=1200,
            title_text="HR Analytics Dashboard - Interactive Overview",
            showlegend=False
        )
        
        return fig
