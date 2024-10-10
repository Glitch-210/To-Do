def task():
    tasks = []
    print("---Welcome to To do App---")

    total_tasks = int(input("Enter number of tasks: "))

    for i in range(1,total_tasks+1):
        task_name = input(f"Enter Task {i}: ") #Enter task
        tasks.append(task_name)

    print(f"Today's Tasks are \n{tasks}")
    
    while True:
        op = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))

        if op == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been added successfully!")
            
        elif op == 2:
            update = input("Enter task you want to update: ")
            if(update in tasks):
                up = input("Enter new Task: ")
                ind = tasks.index(update) #This will return index value of task you want to update 
                tasks[ind] = up
                print(f"Updated Task {up}")
            else:
                print("Sorry,this task is not present in the list")

        elif op == 3:
            delete = input("Enter task you want to delete: ")
            if(delete in tasks):
                ind = tasks.index(delete)
                del tasks[ind]
                print(F"Task {delete} has been deleted")
            else:
                print("Sorry,this task is not present in the list")
                
        elif op == 4:
            print(f"Total Tasks: {tasks}")
            
        elif op == 5:
            print("Closing Program...")
            break
        
        else:
            print("Invalid Input")
task()