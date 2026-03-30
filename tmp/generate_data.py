import pandas as pd
import numpy as np

# Create a dummy dataset resembling IBM HR Analytics
np.random.seed(42)
n = 1000

data = {
    'Age': np.random.randint(18, 60, n),
    'Attrition': np.random.choice(['Yes', 'No'], n, p=[0.16, 0.84]),
    'BusinessTravel': np.random.choice(['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'], n),
    'DailyRate': np.random.randint(100, 1500, n),
    'Department': np.random.choice(['Sales', 'Research & Development', 'Human Resources'], n),
    'DistanceFromHome': np.random.randint(1, 30, n),
    'Education': np.random.randint(1, 6, n),
    'EducationField': np.random.choice(['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'], n),
    'EmployeeCount': [1] * n,
    'EmployeeNumber': range(1, n + 1),
    'EnvironmentSatisfaction': np.random.randint(1, 5, n),
    'Gender': np.random.choice(['Male', 'Female'], n),
    'HourlyRate': np.random.randint(30, 100, n),
    'JobInvolvement': np.random.randint(1, 5, n),
    'JobLevel': np.random.randint(1, 6, n),
    'JobRole': np.random.choice(['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'], n),
    'JobSatisfaction': np.random.randint(1, 5, n),
    'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced'], n),
    'MonthlyIncome': np.random.randint(2000, 20000, n),
    'MonthlyRate': np.random.randint(2000, 25000, n),
    'NumCompaniesWorked': np.random.randint(0, 10, n),
    'Over18': ['Y'] * n,
    'OverTime': np.random.choice(['Yes', 'No'], n),
    'PercentSalaryHike': np.random.randint(11, 26, n),
    'PerformanceRating': np.random.choice([3, 4], n),
    'RelationshipSatisfaction': np.random.randint(1, 5, n),
    'StandardHours': [80] * n,
    'StockOptionLevel': np.random.randint(0, 4, n),
    'TotalWorkingYears': np.random.randint(0, 40, n),
    'TrainingTimesLastYear': np.random.randint(0, 7, n),
    'WorkLifeBalance': np.random.randint(1, 5, n),
    'YearsAtCompany': np.random.randint(0, 40, n),
    'YearsInCurrentRole': np.random.randint(0, 20, n),
    'YearsSinceLastPromotion': np.random.randint(0, 16, n),
    'YearsWithCurrManager': np.random.randint(0, 18, n)
}

df = pd.DataFrame(data)
df.to_csv('data/HR-Employee-Attrition.csv', index=False)
print("Dummy dataset created at data/HR-Employee-Attrition.csv")
