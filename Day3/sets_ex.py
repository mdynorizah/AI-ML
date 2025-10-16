# print("Sets in Python")
# set_one={'laptop','airphone','ipad','mobile','headphone','laptop','ipad'}
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#clear(): remove all the items from set

# set_one={'laptop','airphone','ipad','mobile','headphone'}
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")
# #set.remove(item): Updates the set and removes item from set.
# set_one.remove('airphone')
# print('\n After removing one item from set:',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#union,intersection, difference
# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# set_three={5000,11000}
#union
#s1.union(s2): Returns a new set with all items from both sets s1,s2.
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two,set_three)
# print(f'Union of set_one and set_two and set_three contains {len(unionset)} following items')

# print(unionset)

#union,intersertion,diffrence
# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# #intersection example
# #s1.intersection(s2): Returns set which contain only item in both sets s1,s3..
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f'intersection of set_one and set_two contains {len(newset)} following items')
# print(newset)

set_one={100,200,300,500,700,900,150}
set_two={50,150,200,700,550,650}
#difference example
#s1.difference(s2): Returns set which contain only item those are in s1 but not in s2.
print(f'set_one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)} items')
print(set_two)
newset=set_one.intersection(set_two)
print(f'intersection of set_one and set_two contains {len(newset)} following items')
print(newset)