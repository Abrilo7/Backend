from task_manager import task_add, task_view, task_delete
while True:
    print("""press:
          1.Add Task
          2.View Task
          3.Delete Task
          4.Exit
          """)
    try:
        option = int(input("Enter Your Option: \n>> "))
    except ValueError:
        print("Please, Enter valid number! ")
        continue
    if option == 1:
        task_add()
    elif option == 2:
        task_view()
    elif option == 3:
        task_delete()
    elif option == 4:
        print("Goodbye! ")
        break
    else:
            print("Enter valid Number! ")
        
