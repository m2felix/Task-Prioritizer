import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset (FIXED PATH)
df = pd.read_csv("data/tasks.csv")

# Convert categories into numbers
df = pd.get_dummies(df, columns=["Category"])

# Split features and target
X = df.drop(["CompletedOnTime", "Task"], axis=1)
y = df["CompletedOnTime"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy check
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)

# Save model
joblib.dump(model, "models/task_model.pkl")
joblib.dump(list(X.columns), "models/feature_columns.pkl")

print("Model saved successfully!")