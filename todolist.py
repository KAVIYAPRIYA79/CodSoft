def main():
    tasks=[]

    while True:
        print("\n******TO-DO LIST******")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice=input("Enter your choice:")

        if choice == '1':
            print()
            n_tasks=int(input("how many task you want to add:"))

            for i in range(n_tasks):
                task=input("Enter the task:")
                tasks.append({"task": task,"done": False})
                print("Task added")

        elif choice == '2':
            print("\nTasks:")
            for index,task in enumerate(tasks):
                status = "Done" if task["done"]else "Not Done"
                print(f"{index+1}.{task['task']}-{status}")       

      
        elif choice == '3':
            task_index=int(input("Enter the task number  to mark as done:"))
            if 0<=task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("task mark as done!")
            else:
                print("invalid task number")

        elif choice == '4':
            print("exiting the To-Do List")
            break

        else:
            print("invalid choice.please try again")

if __name__ == "__main__":
    main()                        