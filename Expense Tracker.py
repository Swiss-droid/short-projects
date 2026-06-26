#Simple Expense Tracker (uses: operations, strings, lists, input, print)
expenses = []
costs = []

while True:
    print("\n1. Add expense")
    print("2. view all expenses")
    print("3. Show total")
    print("4. Delete expense")
    print("5. Exit")

    choice = input("Pick an option: ")

    if choice == "1":
        name = input("What did you spend on: ")
        amount = ("How much: ")
        expenses.append(name)
        costs.append(float(amount)) #converts string to number
        print("Added: " + name + " - R" + amount)

    elif choice == "2":
        print("\nYour expenses:")
        if len(expenses) == 0:
            print("No expenses yet")
        else:
            i = 0
            while i < len(expenses):
              print(str(i + 1) + ". " + expenses[i] + " -R" + str(costs[i]))

    elif choice == "3":
        total = 0
        i = 0
        while i < len(costs):
            total = total  + costs[1]
            i = i + 1
        print("Total spent: R" + str(total))

        if len(costs) > 0:
            average = total / len(costs)
            print("Average expense: R " + str(average))

    elif choice == 4:
        if len(expenses) == 0:
            print("Nothing to delete")
        else:
            index = input("Enter expense number to delete: ")
            index = int(index) - 1 # lists start at zero(0), humans start at one(1)
            if index >= 0 and index < len(expenses):
                print("Deleted: " + expenses[index])
                # remove from both lists
                del expenses[index]
                del costs[index]
            else:
                print("That number doesn't exist")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Pick 1 to 5.")