import uuid

from IPython.display import clear_output
productList = []

def main():
    while True:
        # clear_output(wait=True)
        print_menu()
        choice = input("Enter your choice: ")
        clear_output(wait=True)
        if choice == '0':
            break
        menu_chosen(choice)
        
funcs = {}
def menu_item(item_func):
    funcs[len(funcs)] = [item_func, item_func.__doc__]

@menu_item
def exit():
    """Exit"""
    pass

@menu_item
def AddProduct():
    """Add a product"""
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    productId = uuid.uuid4()
    productList.append([productId, name, price])
    print("Product added successfully")

@menu_item
def ProductList():
    """Product list"""
    for product in productList:
        print(f'Name: {product[1]} \n Price: {product[2]} \n ID: {product[0]}')

@menu_item
def FindProductByName():
    """Find product by name"""
    name = input("Enter product name: ")
    for product in productList:
        if product[1] == name:
            print(f'Name: {product[1]} \n Price: {product[2]} \n ID: {product[0]}')
            return
    print("Product not found")

@menu_item
def FindProductByPrice():
    """Find product by price"""
    print("1. Less than",
          "2. Greater than",
          sep='\n')
    choice = input("Enter your choice: ")
    if choice == '1':
        price = input("Enter price: ")
        for product in productList:
            if product[2] <= price:
                print(f'Name: {product[1]} \n Price: {product[2]} \n ID: {product[0]}')
    elif choice == '2':
        price = input("Enter price: ")
        for product in productList:
            if product[2] >= price:
                print(f'Name: {product[1]} \n Price: {product[2]} \n ID: {product[0]}')
    else:
        print("Invalid choice")

@menu_item
def ChangeProductPrice():
    """Change product price"""
    productId = input("Enter product ID: ")
    for product in productList:
        if str(product[0]) == productId:
            product[2] = input("Enter new price: ")
            print("Price changed successfully")
            return
    print("Product not found")

@menu_item
def DeleteProduct():
    """Delete product"""
    productId = input("Enter product ID: ")
    for product in productList:
        if product[0] == productId:
            productList.remove(product)
            print("Product deleted successfully")
            return
    print("Product not found")


def print_menu():
    for item in funcs:
        print(f'{item}. {funcs[item][1]}')

def menu_chosen(choice):
    if choice not in funcs:
        print("Invalid choice")
        return False
    funcs[choice][0]()




main()
