# import random
# print('Random Number from 1 to 1000')
# print(random.randint(1,10))



#expLuckyDraw
# import random
# name=input('Enter YOur Name:')
# luckyNumber=random.randint(1,10)
# print(f'Welcome Mr.\\Ms {name} Cuppon Number: {luckyNumber}')
# if(luckyNumber==1):
#     print('you have won Proton XL=65')
# elif(luckyNumber==3):
#     print('you have won a IPad')
# elif(luckyNumber==9):
#     print('you have won a IPhone')
# else:
#     print('Better Luck Next Time')



import random
def findwinner():
    name=input('Enter YOur Name:')
    luckyNumber=random.randint(1,10)
    print(f'Welcome Mr.\\Ms {name} Cuppon Number: {luckyNumber}')
    if(luckyNumber==1):
        print('you have won Proton XL=65')
    elif(luckyNumber==3):
        print('you have won a IPad')
    elif(luckyNumber==9):
        print('you have won a IPhone')
    else:
        print('Better Luck Next Time')   