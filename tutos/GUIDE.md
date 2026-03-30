# Employee Attrition Prediction System - Project Guide

This project predicts if an employee will leave based on IBM HR features.

## Project Structure
- `data/`: Original CSV and generated visualizations (e.g., `attrition_distribution.png`).
- `code/`: Backend (FastAPI + ML code).
  - `data_preprocessing.py`: Cleans and prepares data.
  - `model_training.py`: Trains Random Forest.
  - `predict.py`: API endpoints.
  - `eda.py`: Initial analysis.
- `app/`: Frontend (Angular).
- `Docker/`: Container definitions.
- `tutos/`: This guide.

## Getting Started

### 1. Requirements
Ensure you have Python 3.9+ and Node.js 18+ installed.

### 2. Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r code/requirements.txt
   ```
3. Train the model:
   ```bash
   python code/model_training.py
   ```
4. Start the API server:
   ```bash
   python -m uvicorn predict:app --reload --host 0.0.0.0 --port 8000
   ```

### 3. Frontend Setup
1. Enter the app directory:
   ```bash
   cd app
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm start
   ```
4. Access the app at `http://localhost:4200`.

### 4. Machine Learning Approach
- **Dataset**: IBM HR Analytics (Cleaned, balanced with oversampling).
- **Model**: Random Forest Classifier (100 estimators, max-depth 10).
- **Features**: Encode categorical vars (OHE) and numerical features.

## Prediction Endpoint
- **URL**: `http://localhost:8000/predict`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "Age": 35,
    "BusinessTravel": "Travel_Rarely",
    "DailyRate": 800,
    ...
  }
  ```
- **Response**:
  ```json
  {
    "attrition": "No",
    "probability": 0.12,
    "prediction_class": 0
  }
  ```
