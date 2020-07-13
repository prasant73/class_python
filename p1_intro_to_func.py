
# def function_name(arguments, keyword_arguments):
#     function_body

# function body
def add_num(num1, num2): # num1, num2 are arguments to the function add_num. they are local to the function
    return num1 + num2

# function should always return >= 0
def sub_num(num1, num2):
    if num1 > num2:
        return num1 - num2
    return num2 - num1

def mul_num(num1, num2):
    return num1 * num2

# always return >= 1
def div_num(num1, num2):
    if num1 == num2:
        if num1 == 0:
            return "0/0 undefined"
    # if num2 == 0:
    #     return "Division by 0 not possible"
    elif num1 > num2:
        if num2 != 0:
            return "Division by 0 not possible"
        else:
            return num1/num2
    else:
        if num1 != 0:
            return "Division by 0 not possible"
        else:
            return num2/num1

# driver code
a = int(input("Enter a : "))
b = int(input("Enter b : "))

# caller
print(add_num(a, b)) # => a, b = num1, num2
print(sub_num(a, b))



# c = a + b

# print(f"{a} added with {b} is {c}")



'''
    input -> process -> output -> print/store/pass it to a different function
'''