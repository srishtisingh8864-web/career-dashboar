import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("data.csv")

# Feature Engineering
df['PromotionGapRatio'] = df['YearsSinceLastPromotion'] / df['YearsAtCompany'].replace(0, 1)
df['RoleStagnationIndex'] = df['YearsInCurrentRole'] / df['YearsAtCompany'].replace(0, 1)
df['TrainingIntensity'] = df['TrainingTimesLastYear'] / df['YearsAtCompany'].replace(0, 1)

df.replace([np.inf, -np.inf], 0, inplace=True)
df.fillna(0, inplace=True)

# Clustering
features = ['PromotionGapRatio', 'RoleStagnationIndex', 'TrainingIntensity']
scaler = StandardScaler()
X = scaler.fit_transform(df[features])

kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Promotion Score
def gap_score(x):
    if x < 0.2:
        return "Low"
    elif x < 0.5:
        return "Medium"
    else:
        return "High"

df['PromotionGapScore'] = df['PromotionGapRatio'].apply(gap_score)

# Retention Risk
df['RetentionRisk'] = (
    (df['PromotionGapScore'] == "High") &
    (df['Attrition'] == 0)
)

# FINAL SAVE (IMPORTANT)
df.to_csv("final_output.csv", index=False)

print("✅ FINAL FILE READY")