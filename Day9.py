# Functions in python

# In short - Function is used to make a block of codes reusable
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')

# def hello():
#     print('Hello user!')

# def my_function():
#     print('Hello world')
#     print('Hello world')
#     print('Hello world')
#     print('Hello world')
#     print('Hello world')

    # def hello():
    #     print('Hello')

    # hello()

# my_function()
 
# hello()


# my_function()
# print('Break')

# my_function()

# user_name = input('Enter your name : ')

# user_name_2 = input('Enter your name : ')

# def greeting(name):
#     print(f'Hello {name}')

# greeting(user_name)
    
# greeting(user_name_2)

# def greeting(name,surname):
#     print(f'Hello {name} {surname}')

# greeting(surname='bahadur',name='ram')
# greeting(name='shyam')

# Args
# username = input('Enter your username :')
# password = input('Enter your password : ')




def child(*args,**kwargs):
    print(args,kwargs)

child('ram','shyam','hari','gopal',parent_name='gopal',address='dhapasi')
# child('ram','shyam')