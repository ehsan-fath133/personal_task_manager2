def add_task(tasks, task):
    tasks.append(task)


def show_tasks(tasks):
    print("Your tasks: ")

    for task in tasks:
        print(task)