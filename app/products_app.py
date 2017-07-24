import csv

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    return matching_products[0]
    product = lookup_product_by_id(product_id)

def valid_id(id):
    ids = []
    for product in products:
        ids.append(product["id"])
    while(id not in ids):
        id = input("WRONG PRODUCT INDENTIFIER! Please try again: ")
    return id

#Opening Code

menu = """
    Hi.

    Welcome to the products app.

    There are {0} products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

#Handle User Inputs

def list_products():
    print("LISTING PRODUCTS")
    with open(csv_file_path, "r") as csv_file:
        contents = csv_file.read()
    print(contents)


def show_product():
    product_id = input("Please input a valid product identifier. ")
    product_id = valid_id(product_id)
    for product in products:
        product_show = lookup_product_by_id(product_id)
    print("SHOW PRODUCT HERE: ", dict(product_show))


def create_product():
    print("CREATING A PRODUCT")
    product_id = input("ID is?")
    product_name = input("What do you want to name the new product?")
    product_aisle = input("What aisle does this product go in?")
    product_department = input("What department does this product go in?")
    product_price = input("What is this item's price?")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)


def update_product():
    print("UPDATING A PRODUCT")
    update_product_id = input("Please input a valid product identifier. ")
    product = [i for i in products if i["id"]==update_product_id]
    if product:
        product = product[0]
        print(dict(product))
        update_product_name = input("What should we change the NAME to?: ")
        update_product_aisle = input ("What should we change the AISLE to?: ")
        update_product_department= input("What should we change DEPARTMENT to?: ")
        update_product_price = input("What should we change PRICE to?: ")
        updated_product = {
        "name":update_product_name,
        "aisle":update_product_aisle,
        "department":update_product_department,
        "price":update_product_price
        }
        print("We will update to ",dict(updated_product) )
        confirmation = input("Please type Y if its okay to update: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            product["name"] = update_product_name
            product["aisle"]= update_product_aisle
            product["department"]=update_product_department
            product["price"]=update_product_price
            print("Updated product")
        else:
            print("Try again")
    else:
            print("Not a valid ID, please try again")


def destroy_product():
    print("DESTROYING A PRODUCT")
    destroy_product = input("Please input a valid product identifier. ")
    product = [i for i in products if i["id"] == destroy_product]
    if product:
        product = product[0]
        print("I am destroying the following product: ")
        print(dict(product))
        confirmation = input("Please type Y if its okay to destroy: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            del products[products.index(product)]
            print("Updated product list")
        else:
            print("Try again")


if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")


#overwriting inventory file
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
