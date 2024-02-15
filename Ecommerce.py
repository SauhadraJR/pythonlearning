import json

def buyer():
    buyer_input = input("Do you want to login or register? ").lower()
    if buyer_input == "login":
        login_buyer()
    if buyer_input == "register":
        register_buyer()

def seller():
    seller_input = input("Do you want to login or register? ").lower()
    if seller_input == "login":
        login_seller()
    if seller_input == "register":
        register_seller()

def register_buyer():
    user_name = input("Enter your username: ")
    user_password = input("Create a password: ")

    user_data = {user_name:user_password}
    json_user_data = json.dumps(user_data)

    f = open("C:/Users/sauha/Desktop/Python Class/file/buyer_user_data.txt","a")
    f.write(json_user_data + "-")
    f.close()


def register_seller():
    user_name = input("Enter your username: ")
    user_password = input("Create a password: ")

    user_data = {user_name:user_password}
    json_user_data = json.dumps(user_data)

    f = open("C:/Users/sauha/Desktop/Python Class/file/seller_user_data.txt","a")
    f.write(json_user_data + "-")
    f.close()


def login_buyer():
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")
    f = open("C:/Users/sauha/Desktop/Python Class/file/buyer_user_data.txt","r")
    json_user_datas = f.read()
    f.close()
    list_user_data = json_user_datas.split("-")
    user_login = False
    for i in list_user_data:
        if i!= '':
            dict_data = json.loads(i)
            if (user_name in dict_data) and user_password == dict_data.get(user_name):
                user_login = True 

    if user_login == True:
        print("Login Successful!!")
        user_operation = input("What do you want to do? [view products/ view bills/ purchase products]").lower()
        if user_operation == "view products":
            view_products()
        
    else:
        print("Invalid Credentials!!")                               


def login_seller():
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")
    f = open("C:/Users/sauha/Desktop/Python Class/file/seller_user_data.txt","r")
    json_user_datas = f.read()
    f.close()
    list_user_data = json_user_datas.split("-")
    user_login = False
    for i in list_user_data:
        if i!= '':
            dict_data = json.loads(i)
            if (user_name in dict_data) and user_password == dict_data.get(user_name):
                user_login = True 

    if user_login == True:
        print("Login Successful!!")
    else:
        print("Invalid Credentials!!")                               

def view_bills():
    pass

def purchase():
    pass

def view_products():
    pass


user_input = input("Are you a buyer or a seller? ").lower()

if user_input == "buyer":
    buyer()

if user_input == "seller":
    seller()

