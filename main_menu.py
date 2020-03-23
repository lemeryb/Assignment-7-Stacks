from Stack import Stack

stack = Stack()
profit = 0
item_quantity = 0
costs = 0

while True:
    user_selection = int(input("Please select an option below\n"
                               "Press 1 to check your profit\n"
                               "Press 2 to push items into stock\n"
                               "Press 3 to sell from your stock\n"
                               "Press a key (1-3): "))

    if user_selection == 1:
        print("You have made: " + "$" + str(profit))

    # Adds items into inventory
    elif user_selection == 2:
        # Pushes items into the stock
        user_input_quantity = int(input("Enter how many items are being added to the inventory: "))
        user_input_costs = int(input("Enter the costs of each item: $ "))

        item_quantity = stack.push(user_input_quantity)
        item_costs = stack.push(user_input_costs)

        costs += user_input_costs

        print("You have added " + str(user_input_quantity) + "items to inventory")
        print("Each item costs: $" + str(user_input_costs))

    # Sells items from inventory
    elif user_selection == 3:

        item_quantity_to_sell = int(input("Enter the quantity of items you are selling: "))
        stack.pop(item_quantity_to_sell)
        average_cost = int(costs * 1.1)
        profit += average_cost * item_quantity_to_sell
        stack.pop(costs)
        print("The average costs per item is: $" + str(average_cost))



