import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from utils import get_logger, DATA_PATH

logger = get_logger("EDA")

def perform_eda():
    logger.info("Starting Exploratory Data Analysis...")
    
    # Load dataset
    data_path = DATA_PATH
    if not os.path.exists(data_path):
        logger.error(f"Dataset not found at {data_path}")
        return
        
    df = pd.read_csv(data_path)
    logger.info(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")

    # Creating visualizations directory
    viz_dir = os.path.join("..", "data")
    os.makedirs(viz_dir, exist_ok=True)

    # 1. Attrition Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Attrition', data=df, palette='viridis')
    plt.title('Employee Attrition Distribution')
    plt.savefig(os.path.join(viz_dir, 'attrition_distribution.png'))
    plt.close()

    # 2. Attrition by Monthly Income
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
    plt.title('Attrition by Monthly Income')
    plt.savefig(os.path.join(viz_dir, 'attrition_by_income.png'))
    plt.close()

    # 3. Correlation Heatmap (numerical)
    plt.figure(figsize=(15, 10))
    numerical_df = df.select_dtypes(include=['int64', 'float64'])
    sns.heatmap(numerical_df.corr(), annot=False, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.savefig(os.path.join(viz_dir, 'correlation_heatmap.png'))
    plt.close()

    logger.info(f"EDA complete. Visualizations saved to {viz_dir}/")

if __name__ == "__main__":
    perform_eda()
