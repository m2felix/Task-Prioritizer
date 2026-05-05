import random
import csv

tasks = [
    ("cram for exam", "School", 4, 1, 5),
    ("study machine learning", "School", 5, 5, 3),
    ("finish assignment", "School", 3, 1, 4),
    ("review lecture notes", "School", 2, 3, 2),
    ("work on group project", "School", 4, 3, 3),

    ("watch netflix", "Leisure", 3, 2, 5),
    ("play video games", "Leisure", 2, 1, 5),
    ("scroll tiktok", "Leisure", 2, 1, 5),
    ("watch youtube", "Leisure", 2, 2, 4),

    ("go to gym", "Health", 1, 3, 2),
    ("morning run", "Health", 1, 2, 2),
    ("cook meal", "Health", 1, 1, 2),
    ("sleep early", "Health", 0.5, 1, 2),

    ("clean room", "Personal", 1.5, 1, 3),
    ("do laundry", "Personal", 1, 2, 2),
    ("organize desk", "Personal", 1, 3, 2),

    ("learn python", "Learning", 3, 5, 3),
    ("read book", "Learning", 2, 4, 2),
    ("practice coding", "Learning", 3, 5, 3),
]


def label_completion(category, difficulty, deadline, procrastination):
    # simple realistic heuristic (keeps dataset consistent)
    score = (deadline + 5 - difficulty + (5 - procrastination)) / 10
    return 1 if score > 0.5 else 0


rows = []

# generate ~120 rows
for _ in range(120):
    task_name, category, hours, deadline, difficulty = random.choice(tasks)

    energy = random.randint(1, 5)
    procrastination = random.randint(1, 5)

    completed = label_completion(category, difficulty, deadline, procrastination)

    rows.append([
        task_name,
        hours,
        deadline,
        difficulty,
        energy,
        procrastination,
        category,
        completed
    ])


with open("data/tasks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "TaskName",
        "EstimatedHours",
        "DeadlineDays",
        "Difficulty",
        "EnergyLevel",
        "ProcrastinationRisk",
        "Category",
        "CompletedOnTime"
    ])
    writer.writerows(rows)

print("Generated 120+ dataset rows successfully!")