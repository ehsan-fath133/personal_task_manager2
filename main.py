name = input("What is your name: ")
print("Welcome")

tasks = []

while True:
    task = input("Enter a task (or type end to finish): ")



    if task == "end":
        break



    tasks.append(task)
    

print("Your tasks:")

for task in tasks:
    print(task)
    from tasks import add_task, show_tasks

name = input("What is your name: ")
print(f"Welcome, {name}")

tasks = []

while True:
    task = input("Enter a task (or type end to finish): ")

    if task == "end":
        break

    add_task(tasks, task)

show_tasks(tasks)