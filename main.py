from dotenv import load_dotenv
import os
from tasks import add_task, show_tasks, save_tasks

load_dotenv()

name = input("What is your name: ")

print(f"Welcome, {name}")

admin = input("Do you want to enter Admin Mode? ")

if admin == "yes":
    password = input("Enter admin password: ")

    if password == os.getenv("TASK_MANAGER_ADMIN_PASSWORD"):
        print("Admin Mode")
    else:
        print("Wrong password")

tasks = []

while True:
    task = input("Enter a task (or type end to finish): ")

    if task == "end":
        break

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority, please choose low or medium or high.")
        priority = input("Enter priority (low/medium/high): ").lower()

    add_task(tasks, task, priority)

save_tasks(tasks)
show_tasks(tasks)