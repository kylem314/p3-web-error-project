HP = 10

class Battleship:

    def __init__(self, damage, health, name):
        self.Damage = damage
        self.Health = health
        self.Name = name
       # return health              #error I get: " TypeError: __init__() should return None, not 'str' "

    @property
    def get_health(self, health):
        if health <= 0:
            print('you died')
        print(health)


   #- @property
    def hp(self):
        return '{}'.format(self.Health)
       # return self.Health

 #   @hp.setter
  #  def hp(self, Hp):
   #     health1 = Hp
   #     self.Health = health1


    def list_info(self):
      #  print("Damage: " + self.Damage + " Health: " + str(self.Health) + " Name: " + self.Name)
        return 'Damage: {} |  Type: {}'.format(self.Damage, self.Name)





#b1.get_health(HP)

#print(f" Health = {b1.get_health(HP)} ")



#------Testing Stuff-------------------------------------------------------------------
b1 = Battleship('12', HP, 'Destroyer')

info = []
info.append(Battleship('12', HP, 'Destroyer'))

print(info)


var1 = b1.list_info()

print(var1)

#b1.hp()

print('------')

BoatHealth = b1.hp()
print(BoatHealth)
print(BoatHealth)


Boatstats = b1.list_info()
print(Boatstats)
#varr = b1.hp()

#print(varr)

