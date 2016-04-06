
import csv as csv





def main():
    print("Items for Hire - by Jonathan Cutjar")
    is_running = True
    rental_list = []
    with open("rental_list.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar='\n')
        for row in reader:
            rental_list.append(row)
    while is_running:
        print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit")
        menu_choice = input()
        menu_choice = menu_choice.upper()
        if menu_choice == "L":
            print("choice L")
            choice_list_all_items(rental_list)

        elif menu_choice == "H":
            print("choice H")
            choice_hire_an_item(rental_list)

        elif menu_choice == "R":
            print("choice R")
            choice_return_an_item(rental_list)

        elif menu_choice == "A":
            print("choice A")
            choice_add_new_item(rental_list)

        elif menu_choice == "Q":
            print("choice Q")
            choice_quit()

        else:
            print("incorrect input")

def choice_list_all_items(rental_list):
    print("Any item marked with an astrix (*) next to it's price, is currently hired out and unavailable for hire.")
    for row in rental_list:
        if row[3] == "out":
            print("{:20} = ${:8.2f} *".format(row[0], float(row[2])))
        else:
            print("{:20} = ${:8.2f}".format(row[0], float(row[2])))

def choice_hire_an_item(rental_list):
    print("Hello H")
    for row in rental_list:
        if row[3] == "in":
            print("{:20} = ${:8.2f}".format(row[0], float(row[2])))
        else:
            print("There are currently no items available for hire.")

def choice_return_an_item(rental_list):
    print("Hello R")
    for row in rental_list:
        if row[3] == "out":
            print("{:20} = ${:8.2f}".format(row[0], float(row[2])))
        else:
            print("There are currently no items available to return.")

def choice_add_new_item(rental_list):
    print("Hello A")

def choice_quit():
    print("Hello Q")
    is_running = False

main()
