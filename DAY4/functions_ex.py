# def function_name(parameters):
#   "'Docstring"'
#   statement(s)

#function without parameters
# def welcome():
#     print("Welcome to Functions")
#     print("Our First Function")

# welcome()


# def welcome(name):
#     print("Welcome to Functions in python Mr.\\Ms",name)

# username=input('Enter your name: \t')
# #function call
# welcome(username)


#function with parameter and return

# def add(num1,num2):
#     return num1+num2
# fnum=int(input("Ener first Number: \t"))
# snum=int(input("Ener second Number: \t"))
# print(f'REsult afer adding {fnum} and {snum} is =\t',add(fnum,snum))


def multi(num1,num2):
    return num1*num2
fnum=int(input("Enter first Number: \t"))
snum=int(input("Enter second Number: \t"))
print(f'Result afer multiplying {fnum} and {snum} is =\t',multi(fnum,snum))