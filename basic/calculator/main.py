num1=int(input("Enter first number: "))
operation=input("Enter operation (+, -, *, /): ")
num2=int(input("Enter second number: "))
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Error! Division by zero."
if operation=='+':
    print("Result:", add(num1,num2))
elif operation=='-':
    print("Result:", subtract(num1,num2))
elif operation=='*':
    print("Result:", multiply(num1,num2))
elif operation=='/':
    print("Result:", divide(num1,num2))
else:
    print("Invalid operation!")
