#Take user marks from user with in 0 to 50
#if usr enter outside[0-50] raise Error InvalidMarks using Custom Exception
#Give chance to the user till, he/she entered valid marks



# while True:
#     try:
#         usermarks=int(input('Enter your marks[0-50]: '))
#         check_marks(usermarks)
#     except InvalidMarks as e:
#         print('Invalid Marks!!!',e)
#     except Exception as ex:
#         print('Error!!!',ex)
#     else:
#         print('Recorded')
#         break
#     choice=input('Do you wanna re-enter marks? If yes press y, to exist press any other key: \t').lower()
#     if(choice!='y'):
#         print('Bye')
#         breakclass InvalidMarks(Exception):
#     pass
# def check_marks(marks):
#     if(marks<0):
#         raise InvalidMarks('mark should not be negative')
#     elif(marks>50):
#         raise InvalidMarks('mark should not be within range 0-50')
#     else:
#         print(f'Marks {marks} are accepted')


from ourpack import mark
while True:
    try:
        usermarks=int(input('Enter your marks[0-50]: '))
        mark.check_marks(usermarks)
    except mark.InvalidMarks as e:
        print('Invalid Marks!!!',e)
    except Exception as ex:
        print('Error!!!',ex)
    else:
        print('Recorded')
        break
    choice=input('Do you wanna re-enter marks? If yes press y, to exist press any other key: \t').lower()
    if(choice!='y'):
        print('Bye')
        break