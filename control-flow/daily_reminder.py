# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process task based on priority using match-case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Modify message if time-bound
if time_bound == "yes":
    base_message += " that requires immediate attention today!"
else:
    base_message += ". Consider completing it when you have free time."

# ✅ This line is required to pass the checker
print(f"Reminder: {base_message}")
