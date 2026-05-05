import pandas as pd
import joblib


# --------------------------------
# Load model + vectorizer
# --------------------------------

model = joblib.load("models/task_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


# --------------------------------
# INPUT
# --------------------------------

print("\nAI TASK PRIORITY SYSTEM (REAL NLP MODE)\n")

task_text = input("Enter your task: ")


print("\nEstimated hours:")
hours = float(input())

print("Deadline days:")
deadline = int(input())

print("Difficulty (1-5):")
difficulty = int(input())

print("Energy level (1-5):")
energy = int(input())

print("Procrastination risk (1-5):")
procrastination = int(input())


# --------------------------------
# NLP VECTOR
# --------------------------------

text_vec = vectorizer.transform([task_text])


# --------------------------------
# COMBINE WITH NUMERIC FEATURES
# --------------------------------

import numpy as np
from scipy.sparse import hstack

numeric = np.array([[hours, deadline, difficulty, energy, procrastination]])

X = hstack([text_vec, numeric])


# --------------------------------
# PREDICT
# --------------------------------

score = model.predict_proba(X)[0][1]


# --------------------------------
# OUTPUT
# --------------------------------

print("\n========================")
print("AI TASK PRIORITY RESULT")
print("========================")

print("Task:", task_text)
print("Priority Score:", round(score, 2))


if score > 0.8:
    print("🚨 DO THIS NOW")
elif score > 0.6:
    print("⚡ IMPORTANT")
else:
    print("🕒 CAN WAIT")