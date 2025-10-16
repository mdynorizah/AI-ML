# def factorial(num):
#     if((num==0)or(num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
    
# num=int(input('Enter a number to find out factorial: '))
# print(f'Factorial of {num} is:',factorial(num))


#write a python function which converts inches to cms.
# 1 inch = 2.5cm

# def inch_to_cm(num):
#         return num*2.5
        
# num=int(input('Enter to inches: '))
# print(f'{num} inches are equal to {inch_to_cm(num)} centimeter')


# def inch_to_cm(inc):
#         return inc*2.5
        
# inc=int(input('Enter to inches: '))
# print(f'{inc} inches are equal to {inch_to_cm(inc)} centimeter')



# def factorial(num):
#     if((num==0)or(num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
        
    
# num=int(input('Enter a number to find out factorial: '))
# print(f'Factorial of {num} is:',factorial(num))

#Write a python function which converts inches to cms.
# 1 inch =2.5 cm
# def inch_to_cm(inc):
#     return inc*2.5
        
    
# inc=int(input('Enter inches: '))
# print(f'{inc} inch are equal to {inch_to_cm(inc)} centimeter')

#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter Number to findout table '))
gen_table(number)