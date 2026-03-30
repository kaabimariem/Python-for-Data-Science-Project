# Employee Attrition Prediction System

A full-stack machine learning application that predicts whether an employee will leave the company based on IBM HR features.

## Architecture
- **Backend**: FastAPI (Python)
- **Frontend**: Angular 18+ (Standalone Components)
- **Machine Learning**: Random Forest Classifier (Scikit-Learn)
- **Containerization**: Docker

## Quick Start
1. **Train Model**:
   ```bash
   cd code
   pip install -r requirements.txt
   python model_training.py
   ```
2. **Start Backend**:
   ```bash
   python -m uvicorn predict:app --reload
   ```
3. **Start Frontend**:
   ```bash
   cd ../app
   npm install
   npm start
   ```

## Features
- **Predictive Analytics**: Input employee data to get attrition probability.
- **EDA & Clustering**: Integrated scripts for data exploration (`eda.py`, `clustering.py`).
- **Premium UI**: Modern dark-themed dashboard with glassmorphism effects.
- **Input Validation**: Pydantic for API and ReactiveForms for Angular.

## Structure
- `/data`: CSV dataset and analytics plots.
- `/code`: API and ML logic.
- `/app`: Angular source code.
- `/Docker`: Deployment configurations.
- `/tutos`: Comprehensive guides.
