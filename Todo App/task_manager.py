def task_add():
    task = input("Enter the Task you want to add: \n>> ")
    with open("task.txt","a") as f:
        f.write(f"{task}\n")
    print("Task added successfully! ")


def task_view():
    with open("task.txt","r") as f:
       task = f.readlines()
    for i,t in enumerate(task, start=1):
        print(f"{i}.{t.strip()}")


def task_delete():
    with open("task.txt", "r") as f:
        tasks = f.readlines()
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t.strip()}")
    try:
        delete_num = int(input("Enter the task number to delete:\n>> "))
    except ValueError:
        print("Enter valid number,please!")
        return
    with open("task.txt", "w") as f:
        for i, t in enumerate(tasks, start=1):
            if i != delete_num:
                f.write(t)
    print("Task removed successfully!")
