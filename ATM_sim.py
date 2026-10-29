print("*"*4+"ATM SIMULATION USING FUNCTIONS"+"*"*4)
print("1. Check_balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

min_bal=10000
def check_bal():
    print("Balance: ",min_bal)
def deposit():
    global min_bal
    amount=int(input("Enter deposit amount: "))
    if amount>0:
        min_bal+=amount
        print("Deposit amount: ",min_bal)
    else:
        print("Invalid Amount")

def withdraw():
    global min_bal
    amount=int(input("Enter withdraw amount: "))
    if amount<=0:
        print("Invalid Amount")
    elif amount>min_bal:
        print("Inavalid Amount")
    else:
        min_bal-=amount
        print("Withdraw Amount: ",min_bal)

n=int(input("Enter Amount: "))
choice=input("choose options: ")
if choice=="1":
    check_bal()

elif choice=="2":
    deposit()
elif choice=="3":
    withdraw()
elif choice=="4":
    print("Exit")
else:
    print("Invalid choice")