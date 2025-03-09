tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' append to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Here are the tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()

    try:
        taskToDelete = int(input("Choose the # of the task you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input. Try again.")



if __name__ == "__main__":
    #create a loop to run the app
    print("Welcome to the to do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Lists tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. PLease try again.")

    print("Goodbye :))")
