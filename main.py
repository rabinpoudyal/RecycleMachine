from recycableitem import RecycableItem
from recycablemachine import RecycableMachine

import code

allitems = []
can = RecycableItem('Can', 0.2, 1, 0)
allitems.append(can)
bottle = RecycableItem('Bottle', 0.5, 2, 0)
allitems.append(bottle)
paper = RecycableItem('Paper', 0.1, 3, 0)
allitems.append(paper)

# Function to: Get valid integer value


def get_int(prompt):
    # Initializing with 0
    value = int(0)
    # Infinite loop
    while True:
        try:
            # Read input
            value = int(input(prompt))
            # Check for negative value
            if value < 0:
                print("We don't accept a negative number of items!")
                continue
            # Break on valid value
            break
        # Catch exceptions
        except ValueError:
            print('Please enter a valid integer value.')
    # Return the valid value
    return value


def bag_items(item_list):
    # Initial values
    machine_list = []
    non_accepted_items = []
    MAX_BAG_WEIGHT = 15.0

    # Loop through items
    for item in item_list:
        # Check if item weight is more than max weight
        if item.weight > MAX_BAG_WEIGHT:
            item_list.remove(item)
            non_accepted_items.append(item)

    # initialize current values
    current_contents = []
    current_weight = 0.0

    # Loop till all items processed
    while len(item_list) > 0:
        # Pick the first item
        temp_item = item_list[0]
        item_list.remove(temp_item)

        # Check if space available
        if current_weight + temp_item.weight < MAX_BAG_WEIGHT:
            # Add to current bag
            current_contents.append(temp_item)
            current_weight += temp_item.weight
            # If all items completed
            if (len(item_list) == 0):
                machine_list.append(current_contents)
        # Add current contents
        else:
            machine_list.append(current_contents)
            # Reset current bag
            current_contents = []
            current_weight = 0.0

    # Loop through all machines
    for index, bag in enumerate(machine_list):
        output = 'Machine ' + str(index + 1) + ' contains: '
        # Print all items in the machine
        for item in bag:
            output += item.name + '\t'
        print(output, '\n')

    # If there are any non accepted items
    if (len(non_accepted_items) > 0):
        output = 'Non-bagged items: '
        # Print all non accepted items
        for item in non_accepted_items:
            output += item + '\t'
        print(output, '\n')


def main():
    while True:
        recycableMachine = RecycableMachine()
        while True:
            print()
            name = input(
                "Balance: $%.2f. Please select a product: (Can, Bottle, Paper, Stop): " % (recycableMachine.total_balance))
            selected_item = None

            if name.lower() == 'stop':
                break
            for item in allitems:
                if item.name.lower() == name.lower():
                    selected_item = item
            if selected_item is None:
                print("Select an item from the given list.")
                continue
            recycableMachine.accept_product(selected_item)
        recycableMachine.print_receipt()
        bag_items(recycableMachine.item_list)
        nextCustomer = input("(N)ext customer, or (Q)uit? ")
        if nextCustomer.lower() == 'q':
            break


if __name__ == '__main__':
    main()
