import re


def extract_features(text: str):
    text = text.lower()

    # --------------------------------
    # Default values
    # --------------------------------
    features = {
        "EstimatedHours": 2,
        "DeadlineDays": 3,
        "Difficulty": 2,
        "EnergyLevel": 3,
        "ProcrastinationRisk": 2,

        "Category_Health": 0,
        "Category_Leisure": 0,
        "Category_Learning": 0,
        "Category_Personal": 0,
        "Category_School": 0
    }


    # --------------------------------
    # CATEGORY DETECTION
    # --------------------------------
    if any(word in text for word in ["study", "exam", "assignment", "homework", "cs", "code"]):
        features["Category_School"] = 1
        features["Difficulty"] = 4
        features["DeadlineDays"] = 2
        features["ProcrastinationRisk"] = 3

    elif any(word in text for word in ["gym", "workout", "run"]):
        features["Category_Health"] = 1
        features["Difficulty"] = 2
        features["EnergyLevel"] = 4

    elif any(word in text for word in ["netflix", "youtube", "game", "watch"]):
        features["Category_Leisure"] = 1
        features["Difficulty"] = 1
        features["ProcrastinationRisk"] = 5
        features["EnergyLevel"] = 4

    elif any(word in text for word in ["clean", "laundry", "room"]):
        features["Category_Personal"] = 1
        features["Difficulty"] = 2
        features["ProcrastinationRisk"] = 3

    elif any(word in text for word in ["read", "learn", "book"]):
        features["Category_Learning"] = 1
        features["Difficulty"] = 3


    # --------------------------------
    # TIME INTENT DETECTION
    # --------------------------------
    if "tonight" in text or "today" in text:
        features["DeadlineDays"] = 1

    if "tomorrow" in text:
        features["DeadlineDays"] = 1

    if "week" in text:
        features["DeadlineDays"] = 5


    # --------------------------------
    # DIFFICULTY INTENSITY DETECTION
    # --------------------------------
    if any(word in text for word in ["cram", "hard", "final", "important"]):
        features["Difficulty"] = 5

    if any(word in text for word in ["quick", "easy", "simple"]):
        features["Difficulty"] = 1


    # --------------------------------
    # ENERGY ESTIMATION
    # --------------------------------
    if any(word in text for word in ["tired", "late", "night"]):
        features["EnergyLevel"] = 2

    if any(word in text for word in ["motivated", "fresh", "morning"]):
        features["EnergyLevel"] = 4


    return features