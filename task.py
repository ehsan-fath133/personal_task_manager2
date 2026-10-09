def add_task(tasks, task, priority):
    tasks.append({
        "task": task,
        "priority": priority
    })


def show_tasks(tasks):
    print("Your tasks: ")

    for task in tasks:
        print(f"{task['task']} - priority: {task['priority']}")


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']} - priority: {task['priority']}\n")