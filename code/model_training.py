import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from data_preprocessing import DataPreprocessor
from utils import get_logger, MODEL_PATH
import os

logger = get_logger("Model Training")

def train_model():
    logger.info("Initializing model training pipeline...")
    
    # 1. Preprocess data
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.prepare_train_test()

    # 2. Train Model
    logger.info("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
    model.fit(X_train, y_train)

    # 3. Evaluate Model
    logger.info("Evaluating model performance...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logger.info(f"Test Accuracy: {accuracy:.4f}")
    
    # Classification Report
    report = classification_report(y_test, y_pred)
    logger.info(f"Classification Report:\n{report}")

    # 4. Save Model
    joblib.dump(model, MODEL_PATH)
    logger.info(f"Model saved to {MODEL_PATH}")

    return model

if __name__ == "__main__":
    train_model()
