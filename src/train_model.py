import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack


# --------------------------------
# Load dataset
# --------------------------------

df = pd.read_csv("data/tasks.csv")


# --------------------------------
# TEXT FEATURE (NLP PART)
# --------------------------------

vectorizer = TfidfVectorizer(max_features=50)
X_text = vectorizer.fit_transform(df["TaskName"])


# --------------------------------
# NUMERIC FEATURES
# --------------------------------

X_numeric = df[[
    "EstimatedHours",
    "DeadlineDays",
    "Difficulty",
    "EnergyLevel",
    "ProcrastinationRisk"
]]


# --------------------------------
# COMBINE FEATURES
# --------------------------------

X = hstack([X_text, X_numeric])
y = df["CompletedOnTime"]


# --------------------------------
# TRAIN MODEL
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --------------------------------
# FEATURE IMPORTANCE ANALYSIS
# --------------------------------

import numpy as np

importances = model.feature_importances_

feature_names = X.columns if hasattr(X, "columns") else None

print("\n========================")
print("FEATURE IMPORTANCE")
print("========================")

if feature_names is not None:
    feature_importance = sorted(
        zip(feature_names, importances),
        key=lambda x: x[1],
        reverse=True
    )

    for name, score in feature_importance:
        print(f"{name}: {round(score, 4)}")

import matplotlib.pyplot as plt

names = [x[0] for x in feature_importance]
scores = [x[1] for x in feature_importance]

plt.figure(figsize=(10,5))
plt.bar(names, scores)
plt.xticks(rotation=45)
plt.title("Feature Importance")
plt.show()

# --------------------------------
# SAVE EVERYTHING
# --------------------------------

joblib.dump(model, "models/task_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained with NLP successfully!")