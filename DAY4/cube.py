print('write a function to findout the cube of given number')
#5 : 5*5*5 (e.g.cube of 5 is 5*5*5 means 125)'
#5 minutes to do this task


#def cube(num):
#     return num*num*num
# given_num=int(input('Enter Number to find out cube of number:\t'))
# print(f'Number is: {given_num} cube is',cube(given_num))

# #Write a function to calculate bonus of given salary
# #function take salary as input and return bunus 10% of salary.

# def cube(num):
#     return num*0.1
# given_num=int(input('Enter Number to find out cube of number:\t'))
# print(f'Number is: {given_num} cube is',cube(given_num))

def calc_bonus(salary):
    return salary*0.1
salary=float(input('Enter Salary to find out bonus:\t'))
print(f'Salary is: {salary} bonus is',calc_bonus(salary))