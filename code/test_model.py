import joblib
import pandas as pd
import numpy as np
import os
from utils import MODEL_PATH, FEATURE_COLS_PATH

def test_model():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURE_COLS_PATH):
        print("Model or feature columns not found.")
        return

    model = joblib.load(MODEL_PATH)
    feature_cols = joblib.load(FEATURE_COLS_PATH)

    # 1. Create a "Stable" employee (Similar to Angular defaults)
    stable_emp = {
        'Age': 54, 'BusinessTravel': 'Travel_Rarely', 'DailyRate': 800, 'Department': 'Sales',
        'DistanceFromHome': 1, 'Education': 3, 'EducationField': 'Life Sciences',
        'EnvironmentSatisfaction': 4, 'Gender': 'Male', 'HourlyRate': 70, 'JobInvolvement': 3,
        'JobLevel': 2, 'JobRole': 'Sales Executive', 'JobSatisfaction': 4, 'MaritalStatus': 'Married',
        'MonthlyIncome': 5000, 'MonthlyRate': 10000, 'NumCompaniesWorked': 1, 'OverTime': 'No',
        'PercentSalaryHike': 15, 'PerformanceRating': 3, 'RelationshipSatisfaction': 3,
        'StockOptionLevel': 1, 'TotalWorkingYears': 10, 'TrainingTimesLastYear': 3,
        'WorkLifeBalance': 3, 'YearsAtCompany': 10, 'YearsInCurrentRole': 5,
        'YearsSinceLastPromotion': 1, 'YearsWithCurrManager': 5
    }

    # 2. Create an "Attriting" employee (Extreme values for attrition)
    attriting_emp = stable_emp.copy()
    attriting_emp.update({
        'Age': 20,
        'OverTime': 'Yes',
        'MonthlyIncome': 1000,
        'JobSatisfaction': 1,
        'EnvironmentSatisfaction': 1,
        'JobInvolvement': 1,
        'DistanceFromHome': 30,
        'TotalWorkingYears': 1,
        'YearsAtCompany': 1,
        'BusinessTravel': 'Travel_Frequently'
    })

    for name, emp in [("Stable", stable_emp), ("Attriting", attriting_emp)]:
        input_data = pd.DataFrame([emp])
        categorical_features = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
        
        input_encoded = pd.get_dummies(input_data, columns=categorical_features, drop_first=False)
        final_input = pd.DataFrame(columns=feature_cols)
        
        for col in feature_cols:
            if col in input_encoded.columns:
                final_input.loc[0, col] = input_encoded.loc[0, col]
            else:
                final_input.loc[0, col] = 0
        
        pred_prob = model.predict_proba(final_input)[0]
        pred_class = model.predict(final_input)[0]
        print(f"Employee: {name}")
        print(f"Prob(Stay): {pred_prob[0]:.4f}, Prob(Leave): {pred_prob[1]:.4f}")
        print(f"Verdict: {'Yes' if pred_class == 1 else 'No'}")
        print("-" * 20)

if __name__ == "__main__":
    test_model()
