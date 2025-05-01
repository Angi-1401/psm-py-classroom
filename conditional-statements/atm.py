balance = 1000.00  # Initial balance

print("Welcome to the ATM!")
print("Your current balance is: $", balance)

print("Would you like to deposit funds? (y/n): ")
choose = input()

if choose == "y" or choose == "Y":
    print("Enter the amount to deposit: $")
    deposit_amount = float(input())
    balance += deposit_amount
    print("Your new balance is: $", balance)

print("Would you like to withdraw funds? (y/n): ")
choose = input()

if choose == "y" or choose == "Y":
    print("Enter the amount to withdraw: $")
    withdraw_amount = float(input())

    if withdraw_amount > balance:
        print("Insufficient funds!")
    else:
        balance -= withdraw_amount
        print("Your new balance is: $", balance)

print("Your final balance is: $", balance)
print("Thank you for using the ATM!")
