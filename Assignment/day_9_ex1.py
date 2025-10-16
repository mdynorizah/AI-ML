num1=float(input('enter your first number'))
num2=float(input('enter your second number'))
num3=float(input('enter your third number'))
def greatest_num(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
great_num=greatest_num(num1,num2,num3)
print('your greatest number is ', great_num)