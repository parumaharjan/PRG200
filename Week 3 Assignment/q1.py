# Paru Maharjan
# ATM Withdrawal Validator 

balance = int(input("Enter your current account balance (NPR): "))
daily_withdrawn = int(input("Enter the amount already withdrawn today (NPR): "))
amount = int(input("Enter the amount you want to withdraw (NPR): "))

daily_limit = 50000

if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

elif amount > balance:
    print("Insufficient balance.")

elif daily_withdrawn + amount > daily_limit:
    print("Daily withdrawal limit reached.")

else:
    balance = balance - amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {balance}")