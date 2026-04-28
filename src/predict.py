import pandas as pd
import joblib



# ----------------------------
# Load trained model
# ----------------------------
model = joblib.load("models/task_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

# ----------------------------
# New tasks to prioritize
# ----------------------------
tasks = pd.DataFrame([
    {
        "EstimatedHours": 2,
        "DeadlineDays": 1,
        "Category_Health": 0,
        "Category_Leisure": 0,
        "Category_Learning": 0,
        "Category_Personal": 0,
        "Category_School": 1
    },

    {
        "EstimatedHours": 1,
        "DeadlineDays": 3,
        "Category_Health": 1,
        "Category_Leisure": 0,
        "Category_Learning": 0,
        "Category_Personal": 0,
        "Category_School": 0
    },

    {
        "EstimatedHours": 3,
        "DeadlineDays": 2,
        "Category_Health": 0,
        "Category_Leisure": 0,
        "Category_Learning": 0,
        "Category_Personal": 1,
        "Category_School": 0
    }
])

tasks = tasks.reindex(columns=feature_columns, fill_value=0)
# ----------------------------
# Predict priority probabilities
# ----------------------------

tasks["PriorityScore"] = model.predict_proba(tasks)[:,1]


# ----------------------------
# Rank highest priority first
# ----------------------------

tasks = tasks.sort_values(
    by="PriorityScore",
    ascending=False
)

print("\nRanked Tasks:\n")
print(tasks)