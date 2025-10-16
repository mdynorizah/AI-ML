
# class Player:
#     def __nit_(self):
#         print('Welcome to Player Class')

# parameterize constructor
class Player:
    def __inti__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id:{self.id} \t Name: {self.name} \t Team: {self.team}')

    def __str__(self):
        return f'{self.id} {self.name} {self.team}'
    
#object creation

p1=Player(1,'MSD','India')
p2=Player(2,'Moin Ali','England')
p3=Player(3,'Joe Root','England')

# displaying first player details
# p1.display()
# p2.display()
# p3.display()

print(p1)
print(p2)
print(p3)