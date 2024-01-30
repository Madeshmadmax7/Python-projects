def addition():
        n1=int(input("Enter number1 to be added : "))
        n2=int(input("Enter number2 to be added : "))
        print("The sum is :",n1+n2)
def subtraction():
        n1=int(input("Enter number1 to be subtracted : "))
        n2=int(input("Enter number2 to be subtracted : "))
        print("The sum is :",n1-n2)
def multiplication():
        n1=int(input("Enter number1 to be multiplied : "))
        n2=int(input("Enter number2 to be multiplied : "))
        print("The sum is :",n1*n2)
def division():
        n1=int(input("Enter number1 to be divided : "))
        n2=int(input("Enter number2 to be divided : "))
        print("The sum is :",n1/n2)
print("Simple Calculator")
print("-------------------------------------------")
print("Select which operation need to be done")
print("Addition : + ")
print("Subtraction : - ")
print("Multiplication : * ")
print("Division : / ")
print("Type 'END' if you are willing to terminate the Calculator")
print("-------------------------------------------")
while True:
    op=input("Enter any operator(symbol) : ")
    if(op=='+'):
        addition()
    elif(op=='-'):
        subtraction()
    elif(op=='*'):
        multiplication()
    elif(op=='/'):
        division()
    elif(op=="END"):
        break;
    else:
        print("Invalid Input")
        print("Enter valid input")
    
