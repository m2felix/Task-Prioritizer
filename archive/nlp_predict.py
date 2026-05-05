import pandas as pd
import joblib


# --------------------------------
# Load model + schema
# --------------------------------

model = joblib.load("models/task_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


# --------------------------------
# INPUT: natural language task
# --------------------------------

print("\nAI Task Prioritizer (NLP MODE)\n")

task_text = input("Enter your task: ").lower()


# --------------------------------
# SIMPLE NLP FEATURE ENGINEERING
# --------------------------------

# Default values
hours = 2
deadline = 3
difficulty = 2
energy = 3
procrastination = 2
category = "Personal"


# Keyword-based logic
if "study" in task_text or "exam" in task_text:
    category = "School"
    difficulty = 4
    deadline = 2
    procrastination = 3

elif "watch" in task_text or "netflix" in task_text or "youtube" in task_text:
    category = "Leisure"
    difficulty = 1
    procrastination = 5
    energy = 4

elif "gym" in task_text or "workout" in task_text:
    category = "Health"
    difficulty = 2
    energy = 3
    procrastination = 2

elif "clean" in task_text or "laundry" in task_text:
    category = "Personal"
    difficulty = 2
    procrastination = 3

elif "code" in task_text or "project" in task_text:
    category = "School"
    difficulty = 5
    deadline = 1
    procrastination = 4


# --------------------------------
# BUILD FEATURE VECTOR
# --------------------------------

task = {
    "EstimatedHours": hours,
    "DeadlineDays": deadline,
    "Difficulty": difficulty,
    "EnergyLevel": energy,
    "ProcrastinationRisk": procrastination,

    "Category_Health": 0,
    "Category_Leisure": 0,
    "Category_Learning": 0,
    "Category_Personal": 0,
    "Category_School": 0
}

task[f"Category_{category}"] = 1


# --------------------------------
# FORMAT FOR MODEL
# --------------------------------

task_df = pd.DataFrame([task])
task_df = task_df.reindex(columns=feature_columns, fill_value=0)


# --------------------------------
# PREDICT
# --------------------------------

score = model.predict_proba(task_df)[0][1]

urgency = 1 / deadline
priority_score = (1 - score) + urgency

# --------------------------------
# OUTPUT
# --------------------------------

print("\n========================")
print("AI TASK PRIORITY RESULT")
print("========================")

print("\nAdjusted Priority Score:", round(priority_score, 2))

if priority_score > 1.5:
    print("🚨 DO THIS NOW")
    print("Reason: High risk of not finishing + urgent deadline.")

elif priority_score > 1.0:
    print("⚡ IMPORTANT")
    print("Reason: Either urgent or likely to be delayed.")

else:
    print("🕒 CAN WAIT")
    print("Reason: Lower urgency and manageable risk.")

print("\n--- Why this decision? ---")

if deadline <= 1:
    print("- Deadline is very close")

if procrastination >= 4:
    print("- High procrastination risk")

if energy <= 2:
    print("- Low energy may slow you down")