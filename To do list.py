def addatask():
    n=int(input("How many tasks are to be added"))
    for i in range(0,n):
        task=input("Enter task: ")
        tasklist.append(task)
        print("Task is added !")

def deletetask():
    t=input("Which task is to be deleted ? : ")
    if t in tasklist:
        tasklist.remove(t)
        print("The task ",t," is removed ! ")
    elif t not in tasklist:
        print("The task is not present ... ")
        print("Enter correct Name of the task\n\n")

def displaytasks():
    n=len(tasklist)
    for i in range(n):
        print(tasklist[i],"\n")


print("\n\nTo do list")
tasklist=[]
while True:
    print("Please check out the options...")
    print("------------------------------------------------------")
    print("1.Add task")
    print("2.Delete task")
    print("3.Show tasks")
    print("4.Quit")
    i=int(input("Enter a valid option: "))
    if(i==1):
        addatask()
    elif(i==2):
        deletetask()
    elif(i==3):
        displaytasks()
    elif(i==4):
        print("\nThe program is about to end. Bye!!!")
        break;
    else:
        print("\nThe option is invalid Enter a valid option!")
