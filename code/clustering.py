import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os
from utils import get_logger, DATA_PATH

logger = get_logger("Clustering")

def cluster_employees():
    logger.info("Starting Employee Clustering for insights...")
    
    if not os.path.exists(DATA_PATH):
        logger.error("Dataset not found.")
        return

    df = pd.read_csv(DATA_PATH)
    
    # 1. Select features for clustering
    # We'll use Income and Working Years to see if there are distinct groups
    cluster_features = ['MonthlyIncome', 'TotalWorkingYears', 'YearsAtCompany']
    X = df[cluster_features]
    
    # 2. Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 3. K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # 4. Analyze Clusters
    cluster_summary = df.groupby('Cluster')[['MonthlyIncome', 'TotalWorkingYears', 'Attrition']].agg({
        'MonthlyIncome': 'mean',
        'TotalWorkingYears': 'mean',
        'Attrition': lambda x: (x == 'Yes').mean()
    })
    
    logger.info(f"Cluster Analysis:\n{cluster_summary}")
    
    # Save visualization
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TotalWorkingYears', y='MonthlyIncome', hue='Cluster', size='Attrition', data=df, palette='viridis')
    plt.title('Employee Clusters based on Income and Experience')
    
    viz_dir = os.path.join(os.path.dirname(DATA_PATH))
    plt.savefig(os.path.join(viz_dir, 'employee_clusters.png'))
    plt.close()
    
    logger.info(f"Clustering complete. Plot saved to data/employee_clusters.png")

if __name__ == "__main__":
    cluster_employees()
