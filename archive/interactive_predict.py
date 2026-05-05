import pandas as pd
import joblib


# --------------------------------
# Load trained model + schema
# --------------------------------

model = joblib.load("models/task_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


# --------------------------------
# Get user input
# --------------------------------

print("\nAI Task Prioritizer\n")

hours = float(input("Estimated hours for task: "))
deadline = int(input("Days left until deadline: "))
difficulty = int(input("Task difficulty (1-5): "))
energy = int(input("Your energy level (1-5): "))
procrastination = int(input("Procrastination risk (1-5): "))

category = input(
    "Category (School/Health/Personal/Leisure/Learning): "
).strip().capitalize()


# --------------------------------
# Basic input validation
# --------------------------------

if not (1 <= difficulty <= 5):
    print("Invalid difficulty (must be 1-5).")
    exit()

if not (1 <= energy <= 5):
    print("Invalid energy level (must be 1-5).")
    exit()

if not (1 <= procrastination <= 5):
    print("Invalid procrastination risk (must be 1-5).")
    exit()


# --------------------------------
# Build feature dictionary
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


category_column = f"Category_{category}"

if category_column in task:
    task[category_column] = 1
else:
    print("Invalid category.")
    exit()


# --------------------------------
# Convert to dataframe
# --------------------------------

task_df = pd.DataFrame([task])


# Match training feature order
task_df = task_df.reindex(
    columns=feature_columns,
    fill_value=0
)


# --------------------------------
# Predict
# --------------------------------

score = model.predict_proba(task_df)[0][1]


# --------------------------------
# Display result
# --------------------------------

urgency = 1 / deadline  # smaller deadline = higher urgency

priority_score = (1 - score) + urgency

# --------------------------------
# EXPLANATION LAYER (WHY this score?)
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