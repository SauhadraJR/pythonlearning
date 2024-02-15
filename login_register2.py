import json

def register():
    user_name = input("Enter your username: ")
    user_password = input("Create a password: ")

    user_data = {user_name:user_password}
    json_user_data = json.dumps(user_data)

    f = open("C:/Users/sauha/Desktop/Python Class/file/userdata.txt","a")
    f.write(json_user_data + "-")
    f.close()

def login():
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")
    f = open("C:/Users/sauha/Desktop/Python Class/file/userdata.txt","r")
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
user_choice = input("Do you want to login or register? ").lower()

if user_choice == "register":
    register()

if user_choice == "login":
    login()