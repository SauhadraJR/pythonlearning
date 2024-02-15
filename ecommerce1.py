import json

def register():
    user_name = input("Enter your username: ")
    user_password = input("Create a password: ")
    user_type = input("Are you a buyer or seller? ").lower()

    user_data = {"user_name": user_name, "user_password": user_password, "user_type" :user_type }
    json_user_data = json.dumps(user_data)

    f = open("C:/Users/sauha/Desktop/Python Class/file/ecommerce_user_data.txt","a")
    f.write(json_user_data + "-")
    f.close()
    user_log = input("Do you want to login? [y/n]").lower()
    if user_log == "y":
        login()
    else:
        print("thankyou for the registration!!")

def login():
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")
    
    f = open("C:/Users/sauha/Desktop/Python Class/file/ecommerce_user_data.txt","r")
    json_user_datas = f.read()
    f.close()
    list_user_data = json_user_datas.split("-")
    user_login = False
    for i in list_user_data:
        if i!= '':
            dict_data = json.loads(i)
            if (user_name == dict_data.get("user_name")) and user_password == dict_data.get("user_password"):
                user_login = True
                type = dict_data.get("user_type") 
                break

    if user_login == True:
        print("Login Successful!!")
        if type == "buyer":
            print(f"Hi {dict_data.get('user_name')}! Welcome to your buyer account.")
            print("What would you like to do? ")
            user_operation = input("[view products/ purchase/ view bills] :").lower() 
            if user_operation == "view product" or user_operation == "view products":
                view_all_products()   
            elif user_operation == "view bill" or user_operation == "view bills":
                view_bills(user_name)
            elif user_operation == "purchase":
                purchase(user_name)
            else:
                print("Invalid selection!!!")
        
        else:
            print(f"Hi {dict_data.get('user_name')}! Welcome to your seller account.")
            print("What would you like to do? ")

            user_operation = input("[add product/ view product/ view bills / my products] :").lower() 
            if user_operation == "add product" or user_operation == "add products":
                add_product(user_name)              
            elif user_operation == "view product" or user_operation == "view products":
                view_all_products()
            elif user_operation == "view bill" or user_operation == "view bills":
                view_bills_seller(user_name) 
            elif user_operation == "my product" or user_operation == "my products":
                view_products(user_name)   
            else:
                print("Invalid selection!!!")
        
    else:
        print("Invalid Credentials!!")                              
        

def view_bills(username):
    
    f = open("C:/Users/sauha/Desktop/Python Class/file/bill_data.txt","r")
    json_bill = f.read()
    f.close()
    list_json = json_bill.split("-")
    total_amount = 0
    for i in list_json:
        if i!="":
            dict_data = json.loads(i)
            if (username == dict_data.get("username")):
                print(f"{dict_data.get("product")} x {dict_data.get("quantity")}: Rs. {dict_data.get("total")}")
                total_amount = total_amount + int(dict_data.get("total"))
    print(f"Your total is Rs. {total_amount}")

def view_bills_seller(username):
    
    f = open("C:/Users/sauha/Desktop/Python Class/file/bill_data.txt","r")
    json_bill = f.read()
    f.close()
    list_json = json_bill.split("-")
    total_amount = 0
    print(f"For the seller account {username}:")
    for i in list_json:
        if i!="":
            dict_data = json.loads(i)
            if (username == dict_data.get("sellername")):
                print(f"Buyer: {dict_data.get("username")} || {dict_data.get("product")} x {dict_data.get("quantity")}: Rs. {dict_data.get("total")}")
                total_amount = total_amount + int(dict_data.get("total"))
    print(f"Total : Rs. {total_amount}")


def purchase(username):
    purchase_product_name = input('Which product do you want to buy? ')
    
    purchase_quantity = int(input('How much quantity? '))

    f = open('C:/Users/sauha/Desktop/Python Class/file/product_data.txt','r')

    product_json_data = f.read()

    f.close()

    list_product_data = product_json_data.split('-')
    available = False
    for i in list_product_data:
        if i != '':
            dict_data = json.loads(i)
            if purchase_product_name == dict_data['product_name']:
                price = int(dict_data['product_price'])
                available = True
                break
    

    if available == True:
        print(f"Purchase of {purchase_product_name} completed!")
        total = purchase_quantity * price
        print(f'Your total is {total}')

        total_bill = {"username":username,"product":purchase_product_name,"quantity":purchase_quantity,"total":total, "sellername": dict_data.get("sellername")}
        json_bill_data = json.dumps(total_bill)
        g = open("C:/Users/sauha/Desktop/Python Class/file/bill_data.txt","a")
        g.write(json_bill_data + "-")
        g.close()
    else: 
        print(f"Product with name {purchase_product_name} not available!")


def view_all_products():
    f = open("C:/Users/sauha/Desktop/Python Class/file/product_data.txt","r")
    product_json_data = f.read()
    f.close()
    list_user_data = product_json_data.split("-")
    for i in list_user_data:
       if i != "":
        dict_data = json.loads(i)
        print(f"{dict_data.get("product_name")}   |   Rs. {dict_data.get("product_price")}  |   seller: {dict_data.get("sellername")}")

def view_products(username):
    f = open("C:/Users/sauha/Desktop/Python Class/file/product_data.txt","r")
    product_json_data = f.read()
    f.close()
    list_user_data = product_json_data.split("-")
    print("Your products are: ")
    for i in list_user_data:
       if i != "":
        dict_data = json.loads(i)
        if (username == dict_data.get("sellername")):
            print(f"{dict_data.get("product_name")}   |   Rs. {dict_data.get("product_price")}  ")


def add_product(username):
    product_name = input("Enter product name: ")
    product_description = input("Enter product description: ")
    product_price = int(input("Enter product price: "))

    product_dict_data = {"product_name":product_name , "product_description": product_description , "product_price": product_price, "sellername" : username}
    product_json_data = json.dumps(product_dict_data)
    f = open("C:/Users/sauha/Desktop/Python Class/file/product_data.txt","a")
    f.write(product_json_data + "-")
    f.close()

    print(f"Your product with name {product_name} is added!!")

while True:
    user_input = input("Do you want to login or register? ").lower()

    if user_input == "register":
        register()
    elif user_input == "login":
        login()
    else: 
        print("Invalid option!!!")
    user_choice = input("do you want to use the program again? (y/n)")
    if(user_choice =="y" or user_choice == "Y"):
        continue
    elif(user_choice =="n" or user_choice =="N"):
        print("Thankyou for using this program")
        break
    else:
        print("Invalid answer")
        break
