HP = 0

class Battleship:

    def __init__(self, damage, health, name):
        self.Damage = damage
        self.Health = health
        self.Name = name
       # return health              #error I get: " TypeError: __init__() should return None, not 'str' "

    def get_health(self, health):
        if health <= 0:
            print('you died')
        print(health)



    def hp(self):
        print(20)

    def list_info(self):
        print("Damage: " + self.Damage + " Health: " + str(self.Health) + " Name: " + self.Name)


b1 = Battleship('12', HP, 'Destroyer')

b1.get_health(HP)

print(f" Health = {b1.get_health(HP)} ")


info = []
info.append(Battleship('12', HP, 'Destroyer'))

print(info)


var1 = b1.list_info()

print(var1)

#b1.hp()
