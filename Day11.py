#File handling

# user = {"ram":"ram123","hari":"hari123"}

# # print(user)
# print(user.get("ram"))
# print(user.get("hari"))

# f = open("C:/Users/sauha/Desktop/Python Class/hello.txt",'r')
# a = f.read()

# f.close()

# print(a)

f = open("C:/Users/sauha/Desktop/Python Class/hello1.txt",'w')

f.write("world")

f.close()

g = open("C:/Users/sauha/Desktop/Python Class/hello.txt",'r')
a = g.read()
print(a)
g.close()