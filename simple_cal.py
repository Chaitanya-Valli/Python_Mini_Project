print("*"*6+"Sample Calculator"+"*"*6)
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
# Add Function
def add(n1,n2):
    return n1+n2

# Sub Funtion
def sub(n1,n2):
    return n1-n2

# Mul Function 
def mul(n1,n2):
    return n1*n2

# Div Function
def div(n1,n2):
    if n2==0:
        return "Division by zero"
    return n1/n2

n1=int(input("Enter Num 1: "))
n2=int(input("Enter Nume 2: "))
choice=input("Enter option from 1-5: ")
if choice=="1":
    print("Result: ",add(n1,n2))
elif choice=="2":
    print("Result: ",sub(n1,n2))
elif choice=="3":
    print("Result: ",mul(n1,n2))
elif choice=="4":
    print("Result: ",div(n1,n2))
elif choice=="5":
    print("Exit")
else:
    print("Invalid Choice")















