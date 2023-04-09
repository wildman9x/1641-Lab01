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

def AddProduct():
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    productId = uuid.uuid4()
    productList.append([productId, name, price])
    print("Product added successfully")

def ProductList():
    for product in productList:
        print(f'Name: {product[1]} \n Price: {product[2]} \n ID: {product[0]}')
        
def FindProductByName():
    name = input("Enter product name: ")
    for product in productList:
        if product[1] == name:
            print(f'Name: {product[1]} \n Price: {product[2]} \n ID: {product[0]}')
            return
    print("Product not found")
    
def FindProductByPrice():
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
        
def ChangeProductPrice():
    productId = input("Enter product ID: ")
    for product in productList:
        if str(product[0]) == productId:
            product[2] = input("Enter new price: ")
            print("Price changed successfully")
            return
    print("Product not found")
    
def DeleteProduct():
    productId = input("Enter product ID: ")
    for product in productList:
        if product[0] == productId:
            productList.remove(product)
            print("Product deleted successfully")
            return
    print("Product not found")
    

funcs = {
    '0': [exit, 'Exit'],
    '1': [AddProduct, 'Add a product'],
    '2': [ProductList, 'Product list'],
    '4': [FindProductByName, 'Find product by name'],
    '5': [FindProductByPrice, 'Find product by price'],
    '6': [ChangeProductPrice, 'Change product price'],
    '7': [DeleteProduct, 'Delete product'],
}

def print_menu():
    for item in funcs:
        print(f'{item}. {funcs[item][1]}')

def menu_chosen(choice):
    if choice not in funcs:
        print("Invalid choice")
        return False
    funcs[choice][0]()




main()
