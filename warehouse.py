# imports
from menu import print_menu, print_header, clear, print_line, print_product
from product import Product
from homework import calculate_age, calculate_tip_tax

# global vars
catalog = []
next_id = 1

# functions

def register_product():
    global next_id
    try:
        print_header("Register a new Product")
        title = input("Please provide the Title: ")
        category = input("Please provide the Category: ")
        stock = int(input("Please provide the Stock: "))
        price = float(input("Please provide the Price: "))

        # create obj
        the_product = Product(next_id, title, category, stock, price)
        next_id = next_id + 1

        # add obj to a list
        catalog.append(the_product)

        print_line()
        print("** Product Registered!!")

    except: 
        print_line()
        print("** Error: verify values and try again!")

def print_catalog():
    print_header("Updated Catalog")

    for prod in catalog: 
        print_product(prod)

def print_tos():
    print_header("Temporarily Out of Stock")

    for prod in catalog:
        if(prod.stock == 0):
            print_product(prod)

def total_value():
    print_header("Total Stock Value")

    total = 0.0
    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print("The total is: " + str(total))

def cheapest_product():
    print_header("Cheapest price")

    prices = []
    for prod in catalog:
        prices.append(prod.price)

    cheapest = min(prices)
    print("The cheapest is: "  + str(cheapest))

def cheapest_product_adv():
    print_header(" Cheapest price advance")

    if(len(catalog) < 1):
        print("** Error, empty catalog. Register prods first.")
        return

    cheapest = catalog[0]
    # check if prod is cheaper than cheapest, if it is, then prod is my new cheapest
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod

    print_product(cheapest)

def delete_product():
    print_header("Delete a product")

    print_catalog()
    id = input("Please select the id to delete: ")
    found = False
    for prod in catalog:
        if(str(prod.id) == id):
            found = True
            catalog.remove(prod)

    if(found):
        print(" ** Product removed!")
    else:
        print(" ** Error: Invalid ID")

def update_price():
    print_header(" Update Product Price")

    print_catalog()
    id = input("Please select the id to update: ")
    found = False

    for prod in catalog:
        if(str(prod.id) == id):
            found = True

            price = float(input("Please provide the new price $: "))
            prod.price = price

    if(found):
        print(" ** Price updated!")
    else:
        print(" ** Error: Invalid ID")


def update_stock():
    print_header(" Update Product Price")

    print_catalog()
    id = input("Please select the id to update: ")
    found = False

    for prod in catalog:
        if(str(prod.id) == id):
            found = True

            stock = int(input("Please provide the new stock: "))
            prod.stock = stock

    if(found):
        print(" ** Stock updated!")
    else:
        print(" ** Error: Invalid ID")


    






    # instructions

opc = " "
while(opc != "x"):
    clear()
    print_menu()
    opc = input("Please choose an option: ")

    if(opc == "1"):
        register_product()
    elif(opc == "2"):
        print_catalog()

    elif(opc == "3"):
        print_tos()

    elif(opc == "4"):
        total_value()

    elif(opc == "5"):
        cheapest_product_adv()

    elif(opc == "6"):
        delete_product()

    elif(opc == "7"):
        update_price()

    elif(opc == "8"):
        update_stock()

    elif(opc == "a"):
        calculate_age()
    elif(opc == "b"):
        calculate_tip_tax()

    input("Press Enter to continue...")

print("Good byte!")