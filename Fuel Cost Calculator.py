kilometres = float(input("Enter the number of kilometres: "))
petrol_price = float(input("Enter the petrol price: ")) # petrol per liter
litres_needed = kilometres / 10  # 1 litre for every 10 kilometre
total_cost = litres_needed * petrol_price

print(kilometres)
print(petrol_price)
print(litres_needed)
print(round(total_cost, 2)) # round off to teo decimal places
