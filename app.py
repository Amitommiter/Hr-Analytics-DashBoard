import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from data_processor import DataProcessor
from predictive_analytics import AttritionPredictor
import config

st.set_page_config(
    page_title=config.DASHBOARD_TITLE,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    processor = DataProcessor(config.DATA_PATH)
    df = processor.load_data()
    processor.validate_data()
    return processor, df

def main():
    st.title(config.DASHBOARD_TITLE)
    st.markdown(f"### {config.DASHBOARD_SUBTITLE}")
    
    try:
        processor, df = load_data()
        
        stats = processor.get_basic_stats()
        dept_attrition = processor.get_department_attrition()
        gender_attrition = processor.get_gender_attrition()
        tech_attrition = processor.get_technical_attrition()
        salary_stats, salary_by_attrition = processor.get_salary_analysis()
        
        st.sidebar.header("Filters")
        departments = st.sidebar.multiselect(
            "Select Departments",
            options=df['department'].unique(),
            default=df['department'].unique()
        )
        
        genders = st.sidebar.multiselect(
            "Select Gender",
            options=df['gender'].unique(),
            default=df['gender'].unique()
        )
        
        age_range = st.sidebar.slider(
            "Age Range",
            min_value=int(df['age'].min()),
            max_value=int(df['age'].max()),
            value=(int(df['age'].min()), int(df['age'].max()))
        )
        
        filtered_df = df[
            (df['department'].isin(departments)) &
            (df['gender'].isin(genders)) &
            (df['age'] >= age_range[0]) &
            (df['age'] <= age_range[1])
        ]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Employees", f"{stats['total_employees']:,}")
        
        with col2:
            st.metric("Attrition Rate", f"{stats['attrition_rate']:.2f}%")
        
        with col3:
            st.metric("Average Age", f"{stats['average_age']:.1f} years")
        
        with col4:
            st.metric("Average Salary", f"${stats['average_salary']:,.0f}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Attrition Rate by Department")
            fig_dept = px.bar(
                dept_attrition.reset_index(),
                x='attrition_rate',
                y='department',
                orientation='h',
                labels={'attrition_rate': 'Attrition Rate (%)', 'department': 'Department'},
                color='attrition_rate',
                color_continuous_scale='Reds'
            )
            fig_dept.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_dept, use_container_width=True)
        
        with col2:
            st.subheader("Gender Attrition Comparison")
            fig_gender = px.bar(
                gender_attrition.reset_index(),
                x='gender',
                y='attrition_rate',
                labels={'attrition_rate': 'Attrition Rate (%)', 'gender': 'Gender'},
                color='gender',
                color_discrete_map={'Male': '#66b3ff', 'Female': '#ff9999'}
            )
            fig_gender.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_gender, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Technical Background Attrition")
            fig_tech = px.bar(
                tech_attrition.reset_index(),
                x='technical_background',
                y='attrition_rate',
                labels={'attrition_rate': 'Attrition Rate (%)', 'technical_background': 'Technical Background'},
                color='technical_background',
                color_discrete_map={'Yes': '#66b3ff', 'No': '#ff9999'}
            )
            fig_tech.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_tech, use_container_width=True)
        
        with col2:
            st.subheader("Salary Distribution")
            fig_salary = px.histogram(
                filtered_df,
                x='salary',
                nbins=20,
                labels={'salary': 'Salary ($)', 'count': 'Number of Employees'},
                color_discrete_sequence=[config.COLORS['success']]
            )
            fig_salary.add_vline(
                x=stats['average_salary'],
                line_dash="dash",
                line_color="red",
                annotation_text=f"Mean: ${stats['average_salary']:,.0f}"
            )
            fig_salary.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_salary, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Age Distribution")
            fig_age = px.histogram(
                filtered_df,
                x='age',
                nbins=15,
                labels={'age': 'Age', 'count': 'Number of Employees'},
                color_discrete_sequence=[config.COLORS['warning']]
            )
            fig_age.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_age, use_container_width=True)
        
        with col2:
            if 'performance_rating' in df.columns:
                st.subheader("Performance Rating Distribution")
                perf_dist = filtered_df['performance_rating'].value_counts().sort_index()
                fig_perf = px.bar(
                    x=perf_dist.index,
                    y=perf_dist.values,
                    labels={'x': 'Performance Rating', 'y': 'Number of Employees'},
                    color_discrete_sequence=[config.COLORS['info']]
                )
                fig_perf.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig_perf, use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("Detailed Analysis Table")
        display_cols = ['employee_id', 'department', 'gender', 'age', 'salary', 
                       'attrition', 'technical_background']
        if 'performance_rating' in df.columns:
            display_cols.append('performance_rating')
        
        st.dataframe(
            filtered_df[display_cols],
            use_container_width=True,
            height=300
        )
        
        st.markdown("---")
        
        st.subheader("Key Insights")
        insights = f"""
        **Overall Metrics:**
        - Total Employees: {stats['total_employees']:,}
        - Overall Attrition Rate: {stats['attrition_rate']:.2f}%
        - Average Employee Age: {stats['average_age']:.1f} years
        - Average Salary: ${stats['average_salary']:,.0f}
        
        **Department Analysis:**
        - Highest Attrition: {dept_attrition.index[0]} ({dept_attrition.iloc[0]['attrition_rate']:.1f}%)
        - Lowest Attrition: {dept_attrition.index[-1]} ({dept_attrition.iloc[-1]['attrition_rate']:.1f}%)
        
        **Gender Analysis:**
        - Female Attrition: {gender_attrition.loc['Female', 'attrition_rate']:.1f}%
        - Male Attrition: {gender_attrition.loc['Male', 'attrition_rate']:.1f}%
        
        **Technical Background:**
        - Technical Employees Attrition: {tech_attrition.loc['Yes', 'attrition_rate']:.1f}%
        - Non-Technical Employees Attrition: {tech_attrition.loc['No', 'attrition_rate']:.1f}%
        """
        st.markdown(insights)
        
        st.markdown("---")
        
        st.subheader("Predictive Analytics - Attrition Risk Prediction")
        
        with st.expander("Train & View Model Performance"):
            if st.button("Train Attrition Prediction Model"):
                with st.spinner("Training model..."):
                    predictor = AttritionPredictor(df)
                    accuracy, report = predictor.train_model()
                    st.session_state['predictor'] = predictor
                    st.success(f"Model trained successfully! Accuracy: {accuracy:.2%}")
                    st.text(report)
                    
                    if predictor.feature_importance is not None:
                        st.subheader("Feature Importance")
                        fig_importance = px.bar(
                            predictor.feature_importance,
                            x='importance',
                            y='feature',
                            orientation='h',
                            labels={'importance': 'Importance Score', 'feature': 'Feature'},
                            color='importance',
                            color_continuous_scale='Blues'
                        )
                        fig_importance.update_layout(height=300, showlegend=False)
                        st.plotly_chart(fig_importance, use_container_width=True)
        
        if 'predictor' in st.session_state:
            st.subheader("Predict Attrition for New Employee")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                pred_age = st.number_input("Age", min_value=18, max_value=70, value=35)
                pred_gender = st.selectbox("Gender", options=df['gender'].unique())
                pred_dept = st.selectbox("Department", options=df['department'].unique())
            
            with col2:
                pred_experience = st.number_input("Experience Years", min_value=0, max_value=50, value=5)
                pred_salary = st.number_input("Salary", min_value=0, max_value=200000, value=75000)
                pred_technical = st.selectbox("Technical Background", options=['Yes', 'No'])
            
            with col3:
                if 'performance_rating' in df.columns:
                    pred_performance = st.number_input("Performance Rating", min_value=1, max_value=5, value=3)
                else:
                    pred_performance = 3
                
                if 'work_life_balance' in df.columns:
                    pred_wlb = st.number_input("Work-Life Balance", min_value=1, max_value=5, value=3)
                else:
                    pred_wlb = 3
            
            if st.button("Predict Attrition Risk"):
                employee_data = {
                    'age': pred_age,
                    'gender': pred_gender,
                    'department': pred_dept,
                    'experience_years': pred_experience,
                    'salary': pred_salary,
                    'technical_background': pred_technical
                }
                
                if 'performance_rating' in df.columns:
                    employee_data['performance_rating'] = pred_performance
                if 'work_life_balance' in df.columns:
                    employee_data['work_life_balance'] = pred_wlb
                
                try:
                    result = st.session_state['predictor'].predict_attrition(employee_data)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Predicted Attrition", result['prediction'])
                    with col2:
                        risk_color = "🔴" if result['probability'] > 50 else "🟡" if result['probability'] > 25 else "🟢"
                        st.metric("Risk Probability", f"{result['probability']:.1f}%", delta=None)
                        st.markdown(f"**Risk Level:** {risk_color}")
                except Exception as e:
                    st.error(f"Prediction error: {str(e)}")
        
    except Exception as e:
        st.error(f"Error loading dashboard: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main()
