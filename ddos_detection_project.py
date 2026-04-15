# ===============================
# IoT DDoS Detection Project
# ===============================

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 2. Load dataset
df = pd.read_csv("MQTT/UL-ECE-MQTT-DDoS-H-IoT2025.csv")

print("\n===== DATA PREVIEW =====")
print(df.head())

print("\n===== DATA INFO =====")
print(df.info())

# 3. Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 4. Identify target column (auto-detect)
target_col = "outcome"
for col in df.columns:
    if 'label' in col.lower() or 'attack' in col.lower():
        target_col = col
        break

print(f"\nDetected Target Column: {target_col}")

# 5. Encode categorical columns
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# 6. Split features & target
X = df.drop(target_col, axis=1)
y = df[target_col]

# 7. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 8. Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 9. Predictions
y_pred = model.predict(X_test)

# 10. Results
print("\n===== MODEL PERFORMANCE =====")
print("Accuracy:", model.score(X_test, y_test))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 11. Confusion Matrix
plt.figure()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.show()

# 12. Feature Importance
importance = model.feature_importances_
features = X.columns

plt.figure()
plt.barh(features, importance)
plt.title("Feature Importance")
plt.show()

# 13. Target distribution
plt.figure()
sns.countplot(x=y)
plt.title("Attack vs Normal Distribution")
plt.show()

print("\nCOMPLETED SUCCESSFULLY")