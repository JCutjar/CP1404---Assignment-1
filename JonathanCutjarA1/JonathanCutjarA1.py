import csv as csv


def main():
    print("Items for Hire - by Jonathan Cutjar")

    is_running = True
    rental_list = []
    with open("items.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\n')
        for row in reader:
            rental_list.append(row)
    print(str(len(rental_list)) + " items loaded from items.csv")
    while is_running:
        print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit")
        menu_choice = input()
        menu_choice = menu_choice.upper()
        if menu_choice == "L":
            choice_list_all_items(rental_list)
        elif menu_choice == "H":
            choice_hire_an_item(rental_list)
        elif menu_choice == "R":
            choice_return_an_item(rental_list)
        elif menu_choice == "A":
            choice_add_new_item(rental_list)
        elif menu_choice == "Q":
            is_running = choice_quit(rental_list)
        else:
            print("Incorrect input.")


def choice_list_all_items(rental_list):
    print("All items on file (* indicates item is currently out):")
    for row in rental_list:
        if row[3] == "out":
            print("{:20} = ${:8.2f} *".format(row[0], float(row[2])))
        else:
            print("{:20} = ${:8.2f}".format(row[0], float(row[2])))


def choice_hire_an_item(rental_list):
    index_tracker = 0
    nothing_to_hire_boolean = True
    for row in rental_list:
        if row[3] == "in":
            nothing_to_hire_boolean = False
            print("{:20} = ${:8.2f}".format(str(index_tracker) + " - " + row[0], float(row[2])))
        index_tracker += 1
    if nothing_to_hire_boolean:
        print("No items available for hire. Returning to main menu")
        return
    item_to_hire = error_check_input(rental_list)
    if item_to_hire.upper() == "Q":
        return
    else:
        rental_list[int(item_to_hire)][3] = "out"


def choice_return_an_item(rental_list):
    index_tracker = 0
    nothing_to_return_boolean = True
    for row in rental_list:
        if row[3] == "out":
            nothing_to_return_boolean = False
            print("{:20} = ${:8.2f}".format(str(index_tracker) + " - " + row[0], float(row[2])))
        index_tracker += 1
    if nothing_to_return_boolean:
        print("No items available for return. Returning to main menu")
        return
    item_to_return = error_check_input(rental_list)
    if item_to_return.upper() == "Q":
        return
    else:
        rental_list[int(item_to_return)][3] = "in"


def error_check_input(rental_list):
    valid_input_boolean = False
    input_to_be_checked = ""
    while not valid_input_boolean:
        input_to_be_checked = input("Which item would you like to hire? or Q to Quit")
        try:
            if input_to_be_checked.upper() == "Q":
                valid_input_boolean = True
            elif int(input_to_be_checked) <= len(rental_list) - 1:
                valid_input_boolean = True
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")
    return input_to_be_checked


def choice_add_new_item(rental_list):
    item_name = input("Item name: ")
    while item_name == "":
        print("Input cannot be blank")
        item_name = input("Item name: ")
    item_description = input("Description: ")
    while item_description == "":
        print("Input cannon be blank")
        item_description = input("Description: ")
    item_price_per_day = 0.0
    price_is_valid_boolean = False
    while not price_is_valid_boolean:
        item_price_per_day = input("Price per day: $")
        try:
            if item_price_per_day == "":
                print("Input cannon be blank")
            elif float(item_price_per_day) < 0.0:
                print("Price must be > or = $0")
                print("Invalid input; enter a valid number")
            else:
                price_is_valid_boolean = True
        except ValueError:
            print("Invalid input; enter a valid number")
    new_item = [item_name, item_description, item_price_per_day, "in"]
    print(new_item[0] + " (" + new_item[1] + "), $" + new_item[2] + " now available for hire.")
    rental_list.append(new_item)


def choice_quit(rental_list):
    program_boolean = False
    with open('items.csv', 'w', newline='\n') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(rental_list)
    print(str(len(rental_list)) + " items saved to items.csv")
    print("Have a nice day! :)")
    return program_boolean


main()
