import tsk4


class Flora:

    def __init__(self, name, lifespan, habitat, plant_type):
        self.name = name
        self.lifespan = lifespan
        self.habitat = habitat
        self.plant_type = plant_type
        self.plant_size = 0

    def ad_flora(self, planet:tsk4.Planet):
        if planet.flora:
            planet.add_flora(self.name,self.plant_type)

class Fauna:

    def __init__(self, name):
        self.name = name


class Predator(Fauna):

    def __init__(self, name:str, predator_type:str, what_eats:str, lifespan:int):
        super().__init__(name)
        self.predator_type = predator_type
        self.what_eats = what_eats
        self.lifespan = lifespan

    def check_planet(self, planet: tsk4.Planet):
        if planet.flora and planet.fauna and not planet.humanity:
            planet.add_fauna(self.name,self.predator_type)
    # def check_planet(self,planet:tsk4.Planet):
    #     if planet.fauna and not planet.humanity:
    #         print('YES')
    #     else:
    #         print('NO')


class Mammal(Fauna):

    def __init__(self, name, mammal_type, lifespan):
        super().__init__(name)
        self.mammal_type = mammal_type
        self.lifespan = lifespan

    def check_planet(self,planet:tsk4.Planet):
        if planet.flora and planet.fauna and not planet.humanity and 'grass' and 'wheat' in planet.flora_list["name"]:
            planet.add_fauna(self.name,self.mammal_type)

shark = Predator('baby shark','predator','all',20)
shark.check_planet(tsk4.friendly)
grass = Flora("grass",20,"mammal","grass")
wheat = Flora("wheat", 20, "mammal", 'wheat')
wheat.ad_flora(tsk4.friendly)
grass.ad_flora(tsk4.friendly)
print(tsk4.friendly.flora_list)
giraffe = Mammal('malwan','earth',20)
giraffe.check_planet(tsk4.friendly)
marti = Mammal('marti','earth',20)
marti.check_planet(tsk4.friendly)

print(tsk4.friendly.__dict__)

