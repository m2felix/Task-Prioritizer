# AI Task Prioritization System

## Project Description
This project builds a machine learning system that predicts which task a user should prioritize based on features such as deadline, estimated effort, and task category.

Instead of relying on fixed rules (like sorting by deadline), this system learns patterns from past task data to estimate the likelihood of completing each task on time. Tasks are then ranked based on this prediction to help users decide what to work on next.

## Example Input
A list of tasks with attributes:

| Task | EstimatedHours | DeadlineDays | Category |
|------|----------------|--------------|----------|
| Finish homework | 2 | 1 | School |
| Go to gym | 1 | 3 | Health |
| Clean room | 1.5 | 2 | Personal |

## Example Output
The system assigns a priority score and ranks tasks:

| Task | Priority Score | Rank |
|------|---------------|------|
| Finish homework | 0.91 | 1 |
| Clean room | 0.75 | 2 |
| Go to gym | 0.60 | 3 |

Higher scores indicate tasks that should be prioritized first.

## Goal
To build a complete machine learning pipeline including:
- Data collection and preprocessing
- Model training and evaluation
- Task ranking prediction system
- (Optional) Interactive interface for users
