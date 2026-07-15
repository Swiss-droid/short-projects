bank_balance = 500
withdraw = float(input("How much do you wish to withdraw? "))

if withdraw <= bank_balance:
    remaining_balance = bank_balance - withdraw
    print(f"Withdrawal successful! Remaining balance: {remaining_balance}")
elif withdraw <= 0:
    print("Invalid amount. You must withdraw more than R0.")
else:
    print("Declined. Insufficient funds.")