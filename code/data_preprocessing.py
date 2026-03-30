import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.utils import resample
import os
import joblib
from utils import get_logger, DATA_PATH

logger = get_logger("Preprocessing")

class DataPreprocessor:
    def __init__(self, data_path=DATA_PATH):
        self.data_path = data_path
        self.scaler = StandardScaler()
        self.le = LabelEncoder()
        self.feature_columns = None
        self.categorical_cols = None
        self.numerical_cols = None

    def load_and_preprocess(self):
        logger.info(f"Loading data from {self.data_path}")
        df = pd.read_csv(self.data_path)

        # Drop columns with zero variance or irrelevant
        cols_to_drop = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']
        df = df.drop(columns=cols_to_drop)

        # Encode target
        df['Attrition'] = self.le.fit_transform(df['Attrition']) # Yes: 1, No: 0

        # One-Hot encoding for categorical variables
        categorical_features = df.select_dtypes(include=['object']).columns.tolist()
        self.categorical_cols = categorical_features
        df_encoded = pd.get_dummies(df, columns=categorical_features, drop_first=True)

        # Identify numerical columns for scaling
        self.numerical_cols = df.select_dtypes(include=['int64', 'float64']).drop(columns=['Attrition']).columns.tolist()

        return df_encoded

    def prepare_train_test(self, test_size=0.2):
        df_encoded = self.load_and_preprocess()

        X = df_encoded.drop(columns=['Attrition'])
        y = df_encoded['Attrition']

        # Handling imbalance (Oversampling 'Yes' cases)
        df_majority = df_encoded[df_encoded.Attrition == 0]
        df_minority = df_encoded[df_encoded.Attrition == 1]
        
        df_minority_upsampled = resample(df_minority, 
                                         replace=True,     
                                         n_samples=len(df_majority), 
                                         random_state=42) 
        
        df_upsampled = pd.concat([df_majority, df_minority_upsampled])
        
        X_upsampled = df_upsampled.drop('Attrition', axis=1)
        y_upsampled = df_upsampled.Attrition

        X_train, X_test, y_train, y_test = train_test_split(X_upsampled, y_upsampled, test_size=test_size, random_state=42)
        
        # Scale only numerical columns
        # Note: In a real scenario, we'd only scale training data and apply to test
        # Here we'll simplify and remember feature names for prediction
        self.feature_columns = X_train.columns.tolist()
        
        # Save feature column names for prediction later
        os.makedirs("models", exist_ok=True)
        joblib.dump(self.feature_columns, "models/feature_cols.joblib")
        joblib.dump(self.categorical_cols, "models/categorical_cols.joblib")
        joblib.dump(self.numerical_cols, "models/numerical_cols.joblib")

        return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.prepare_train_test()
    logger.info(f"Preprocessing completed. Features: {len(preprocessor.feature_columns)}")
