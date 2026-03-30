from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
import os
from typing import Optional
from utils import get_logger

logger = get_logger("API")

app = FastAPI(title="Employee Attrition Prediction System")

# Enable CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and features
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "attrition_model.joblib")
FEATURE_COLS_PATH = os.path.join(BASE_DIR, "models", "feature_cols.joblib")

if not os.path.exists(MODEL_PATH):
    logger.warning("Model not found. You must run model_training.py before using /predict.")
    model = None
else:
    model = joblib.load(MODEL_PATH)

if not os.path.exists(FEATURE_COLS_PATH):
    logger.warning("Feature list not found.")
    feature_cols = []
else:
    feature_cols = joblib.load(FEATURE_COLS_PATH)

class EmployeeInfo(BaseModel):
    Age: int = Field(..., example=35)
    BusinessTravel: str = Field(..., example="Travel_Rarely")
    DailyRate: int = Field(..., example=800)
    Department: str = Field(..., example="Sales")
    DistanceFromHome: int = Field(..., example=5)
    Education: int = Field(..., example=3)
    EducationField: str = Field(..., example="Life Sciences")
    EnvironmentSatisfaction: int = Field(..., example=4)
    Gender: str = Field(..., example="Male")
    HourlyRate: int = Field(..., example=70)
    JobInvolvement: int = Field(..., example=3)
    JobLevel: int = Field(..., example=2)
    JobRole: str = Field(..., example="Sales Executive")
    JobSatisfaction: int = Field(..., example=4)
    MaritalStatus: str = Field(..., example="Married")
    MonthlyIncome: int = Field(..., example=5000)
    MonthlyRate: int = Field(..., example=10000)
    NumCompaniesWorked: int = Field(..., example=1)
    OverTime: str = Field(..., example="No")
    PercentSalaryHike: int = Field(..., example=15)
    PerformanceRating: int = Field(..., example=3)
    RelationshipSatisfaction: int = Field(..., example=3)
    StockOptionLevel: int = Field(..., example=1)
    TotalWorkingYears: int = Field(..., example=10)
    TrainingTimesLastYear: int = Field(..., example=3)
    WorkLifeBalance: int = Field(..., example=3)
    YearsAtCompany: int = Field(..., example=5)
    YearsInCurrentRole: int = Field(..., example=2)
    YearsSinceLastPromotion: int = Field(..., example=1)
    YearsWithCurrManager: int = Field(..., example=2)

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": (model is not None)}

@app.post("/predict")
def predict_attrition(employee: EmployeeInfo):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Train the model first.")

    try:
        # 1. Convert input to DataFrame
        input_data = pd.DataFrame([employee.dict()])
        
        # 2. Replicate OHE preprocessing
        # Identify categorical columns (must match training encoding)
        categorical_features = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
        
        # We need to ensure we have all dummy columns expected by the model
        input_encoded = pd.get_dummies(input_data, columns=categorical_features, drop_first=False)
        
        # Align with model feature columns
        final_input = pd.DataFrame(columns=feature_cols)
        
        # Insert shared columns from dummy columns
        for col in feature_cols:
            if col in input_encoded.columns:
                final_input.loc[0, col] = input_encoded.loc[0, col]
            else:
                final_input.loc[0, col] = 0 # Feature not present for this sample

        # 3. Predict
        prediction_prob = model.predict_proba(final_input)[0]
        prediction_class = int(model.predict(final_input)[0])
        
        attrition_probability = float(prediction_prob[1]) # Probability of Attrition: Yes (1)
        attrition_result = "Yes" if prediction_class == 1 else "No"

        return {
            "attrition": attrition_result,
            "probability": attrition_probability,
            "prediction_class": prediction_class
        }
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
