shoppingcart={}
print("""
WELCOME TO THE AMANDO SHOPPING SITE
1. Add Product to the cart
2. Search the Product
3. Delete the product from the cart
4. Quit
""")

option=int(input("Enter Your Choice:"))

while option != 4:
    if option==1:
        qty=int(input("Enter the number of items to be added in the stationery shop: "))
        if len(shoppingcart)+qty >=5:
            print("Shoppingcart Full")
        else:
            for i in range(qty):
                product_name=input("Enter an Item: ")
                brand=input("Enter the brand name: ")
                shoppingcart[product_name]=brand
                print("You added the following items: ")
                print(product_name, ":" , shoppingcart[product_name])

    elif option==2:
        product_name=input("Enter the item to be searched: ")
        if product_name in shoppingcart:
            print(product_name, ":" , shoppingcart[product_name])
        else:
            print("No product exists with this name")


    elif option==3:
        product_name=input("Enter the item to delete: ")
        del(shoppingcart[product_name])
        print(product_name,"deleted")
        if len(shoppingcart) == 0:
            print("Cart is empty, no item is found")


    elif option!=4:
        print("Wrong Option Entered")

    option=int(input("Enter Your Choice:"))

else:
    print("Program Closed")
    
    
