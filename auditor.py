inventory = 0
user_input = ''
rejected = 0

while user_input != 'quit':
    user_input = input("Enter stock quantity: ")

    if user_input == 'quit':
        break

    if user_input.isdigit():
        inventory += int(user_input)
        if inventory > 500:
            print("Inventory has exceeded 500 units")
            print("Total Units Processed ", inventory)
            print("Number of Failed/Rejected Entries ", rejected)
            break
    else:
        rejected += 1
        print("Error: this input is not valid")