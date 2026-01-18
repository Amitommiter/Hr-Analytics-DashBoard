import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AttritionPredictor:
    def __init__(self, df):
        self.df = df.copy()
        self.model = None
        self.label_encoders = {}
        self.feature_importance = None
        
    def prepare_data(self):
        df = self.df.copy()
        
        categorical_cols = ['gender', 'department', 'technical_background']
        if 'job_title' in df.columns:
            categorical_cols.append('job_title')
        
        for col in categorical_cols:
            if col in df.columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le
        
        df['attrition_binary'] = (df['attrition'] == 'Yes').astype(int)
        
        feature_cols = ['age', 'gender', 'department', 'experience_years', 
                       'salary', 'technical_background']
        
        if 'performance_rating' in df.columns:
            feature_cols.append('performance_rating')
        if 'work_life_balance' in df.columns:
            feature_cols.append('work_life_balance')
        
        available_cols = [col for col in feature_cols if col in df.columns]
        
        X = df[available_cols]
        y = df['attrition_binary']
        
        return X, y, available_cols
    
    def train_model(self):
        X, y, feature_cols = self.prepare_data()
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
        
        self.model.fit(X_train, y_train)
        
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        logger.info(f"Model trained with accuracy: {accuracy:.4f}")
        
        self.feature_importance = pd.DataFrame({
            'feature': feature_cols,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return accuracy, classification_report(y_test, y_pred)
    
    def predict_attrition(self, employee_data):
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        
        X, _, _ = self.prepare_data()
        
        for col, le in self.label_encoders.items():
            if col in employee_data:
                employee_data[col] = le.transform([str(employee_data[col])])[0]
        
        prediction = self.model.predict([list(employee_data.values())])[0]
        probability = self.model.predict_proba([list(employee_data.values())])[0]
        
        return {
            'prediction': 'Yes' if prediction == 1 else 'No',
            'probability': float(probability[1]) * 100
        }
    
    def get_feature_importance(self):
        return self.feature_importance
