task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Step 2: Process the task based on priority using match-case
match priority:
    case "high":
        priority_message = "This task has high priority."
    case "medium":
        priority_message = "This task has medium priority."
    case "low":
        priority_message = "This task has low priority."
    case _:
        priority_message = "Unknown priority level."

# Step 3: Modify the reminder based on time-sensitivity
if time_bound == "yes":
    time_bound_message = "This task requires immediate attention today!"
else:
    time_bound_message = "This task is not time-sensitive."

# Step 4: Provide a customized reminder
print(f"Reminder: {task}")
print(f"Priority: {priority_message}")
print(f"{time_bound_message}")
