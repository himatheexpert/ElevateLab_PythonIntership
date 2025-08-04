#<--------- Function Definition ---------->
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Divide by zero error"
    else:    
        return a/b

#<--------- Main Program ---------->
a = float(input("Enter the operand1 for operation : "))
b = float(input("Enter the operand2 for operation : "))

while(True):
    print("\n<------- CALCULATOR MENU ------->")
    print("\n1.Add\n2.Sub\n3.Multiply\n4.Division\n5.Exit")
    ch=int(input("\nEnter the operation you want(1/2/3/4/5) : "))
    if ch==1:
        Result = add(a,b)
        print(f"Result of {a} + {b} is : {Result}")
    elif ch==2:
        Result = sub(a,b)
        print(f"Result of {a} - {b} is : {Result}")
    elif ch==3:
        Result = mul(a,b)
        print(f"Result of {a} * {b} is : {Result}")
    elif ch==4:
        Result = div(a,b)
        print(f"Result of {a} / {b} is : {Result}")
    elif ch==5:
        print("\nExiting program.......")
        break
    else:
        print("Invalid option, Try again !!")
