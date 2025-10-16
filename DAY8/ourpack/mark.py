class InvalidMarks(Exception):
    pass
def check_marks(marks):
    if(marks<0):
        raise InvalidMarks('mark should not be negative')
    elif(marks>50):
        raise InvalidMarks('mark should not be within range 0-50')
    else:
        print(f'Marks {marks} are accepted')