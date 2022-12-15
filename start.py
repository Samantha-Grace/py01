# python
# hello = "hello"
# print(hello)


# listvar = ll
# dictvar = {}
# string = "something something"
# intvar = 123
# boolar= False

# print(boolvar)


# dictionary vs list 
# we will use a lot of these
# array = dict

# list = comma seperated list of things (key with multiple values)
# listvar = ["garn", 123, False, "nick", ]

# calling these things:
# for item listvar:

# listvar = ["garn", 123, False, "nick", ]
# dictvar = {}

# for item in listvar:
#     print(item)
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# if statements

# listvar = ["garn", 123, False, "nick", ]
# dictvar = {}

# if (listvar[0] != "hi" or listvar[0] =="bye") and listvar[1] =="nick":
#     print("TRUE")
# else:
#     print("NO")

# if listvar[0] != "hi" or listvar[0] =="bye" and listvar[1] =="nick":
#     print("TRUE")
# else:
#     print("NO")

# listvar = ["garn", 123, False, "nick", ]
# # key and key value pairs
# dictvar = {"Garn": "cool guy", "Nick": "smart guy"}
# # gives you just the items Garn Nick
# for item in dictvar:
#     print(item)



# if "rn" in listvar[0]:
#     print("TRUE")
# else:
#     print("NO")


# listvar = ["garn", 123, False, "nick", ]
# # key and key value pairs
# dictvar = {"Garn": "cool guy", "Nick": "smart guy"}
# # gives you just the items Garn Nick
# for item in dictvar:
#     print(item)

# Define function

# def helloworld(name):
#     print(f"hello {name}")

# helloworld("Meow")

# name = "Chandler"

# def helloworld(name = "you", wassup = "wazzzup"):
#     print(f"hello {name}, {wassup}")

# helloworld("Meow", "nice to meet you")
# helloworld("cats")
# helloworld()

# print(name)

# name = "Chandler"

# def helloworld(name: str = "Sam", wassup = "wazzzup"):
#     print(f"hello {name}, {wassup}")

# helloworld("Meow", "nice to meet you")
# helloworld("cats")
# helloworld(123)
# helloworld()
# helloworld()

# print(name)

listvar = ["garn", 123, False, "nick", "stuff"]
dictvar = {"Garn": "cool guy", "Nick": "smart guy"}
listvar2 = ["garn", 123]


# def helloWorld(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for kwarg in kwargs:
#         print(kwarg)

#     helloWorld(listvar, "test")
#     helloWorld(listvar2)


def helloworld(name):
    name = f"hello {name}"
    return name

newname = helloworld("sam")

print(newname)