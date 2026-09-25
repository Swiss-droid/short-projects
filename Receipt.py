print("<=== ABC Super Store ===>")
print("-------------------------")

print()
print("Address: 456 Avenue, Suite 789")
print("Tel:     012 345 6789")
print("Date:    22 September 2026")
print("Manager: Vicky Yardley")
print()

print("-------------------------")

print()

my_groceries = {
    "Pencil": 2.5,
    "Milk": 23,
    "Bread": 20.2,
    "Cheese": 15.5,
    "Pegs": 27,
    "Tomato": 15,
    "Potato": 16,
    "Onion": 16,
    "Cucumber": 19,
    "Juice": 30
}

# Alligns the key to the left and the value to the right
max_key = max(len(k) for k in my_groceries)
for key, value in my_groceries.items():
    print(f"{key:<{max_key}} {value}")
print()
print("---------------------------")

# Sum of the values 
sub_total = sum(my_groceries.values())
print("Sub Total:R", sub_total         )

pre_tax = sub_total
tax_rate = 0.15  # 15%

sub_total = pre_tax * (1 + tax_rate)
tax = sub_total - pre_tax

print(f"Sales Tax:R", round(tax, 2)     )  # rounds off tax to two decimal places
print("---------------------------")

total = sub_total + tax
print(f"TOTAl:R", round(total, 2)       ) # rounds off total to 2 decimal places

print("---------------------------")
print("Paid By:               Card")

print() # Skips a line

print("Transaction ID: 098-7654321")
print("Vendor ID:      123-4567890")

print() # Skips a line

print("     Thank You For     ")
print("     Your Purchase!     ")