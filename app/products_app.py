
menu = """
    Hi.

    Welcome to the products app.

    There are 100 products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

"""


chosen_operation = input(menu)

if chosen_operation.title() == "List":
    print("LISTING PRODUCTS")
elif chosen_operation.title() == "Show":
    print("SHOWING A PRODUCT")
elif chosen_operation.title() == "Create":
    print("CREATING A PRODUCT")
elif chosen_operation.title() == "Update":
    print("UPDATING A PRODUCT")
elif chosen_operation.title() == "Destroy":
    print("DESTROYING A PRODUCT")
else:
    print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
