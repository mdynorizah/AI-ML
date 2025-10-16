# import datetime
# import inspect
# dtclassess=inspect.getmembers(datetime, inspect.isclass)

# print('All Classes in datetime module')
# for n, func in dtclassess:
#     print(n,end="\t")



# import datetime
# import inspect
# dtclassess=inspect.getmembers(datetime, inspect.isclass)

# print('All Classes in datetime module')
# for n, func in dtclassess:
#     print(n,end="\t")

# print('\n ---Today---\m')
# print(datetime.date.today())



import datetime
import inspect
dtclassess=inspect.getmembers(datetime, inspect.isclass)

print('All Classes in datetime module')
for n, func in dtclassess:
    print(n,end="\t")

print('\n ---Today---\m')
print(datetime.date.today())

print('\n ---Current Date Time---\m')
print(datetime.datetime.now())
print('\n ---Current Date Time---\m')
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I %M %S %p')
print('Current time',cttime)
print('Formated time',formatedtime)