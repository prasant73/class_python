'''
    id() - gives you the memory location of a data
    hex() - converts any number to a hexadecimal value
    type() - data type of any variable
    dir() - the static files, dunder methods, functions defined for a particular data in a list format
'''


# print("Hello World...")

# # variable assignment - right to left
# a = 5 # a is referencing to a memory location which stores the value 5
# b = 10
# c = a + b
# print(c)



# input() - default takes a string as a user input
# int(input())

a = int(input("Enter a : "))
b = float(input("Enter b : "))

c = a + b

print(c, bin(a), hex(a))

print(f"{a} added with {b} is {c}")

print(type(a), type(b), type(c))


# a = 5