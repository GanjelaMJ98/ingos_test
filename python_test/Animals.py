# Базовый класс
class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def say(self):
        print(f"Hello, i'm {type(self).__name__} and my name is {str(self.name)}")
        
    def run(self):
        print(f"My name is {str(self.name)} and i can't run")
        
    def swim(self):
        print(f"My name is {str(self.name)} and i can't swim")
    
    def fly(self):
        print(f"My name is {str(self.name)} and i can't fly")
    
    def get_energy(self):
        return self.energy



# Классы с навыками
class SwimAnimal(Animal):
    def __init__(self, name, energy, energy_for_swim):
        Animal.__init__(self, name, energy)
        self.energy_for_swim = energy_for_swim

    def swim(self):
        if self.energy >= self.energy_for_swim:
            print(f"My name is {str(self.name)} and i'm swimming and need {self.energy_for_swim} e.p. for swim")
            self.energy = self.energy - self.energy_for_swim
        else:
            print(f"My name is {str(self.name)} and i can't swim because my energy is low")


class RunAnimal(Animal):
    def __init__(self, name, energy, energy_for_run):
        Animal.__init__(self,name, energy)
        self.energy_for_run = energy_for_run

    def run(self):
        if self.energy >= self.energy_for_run:
            print(f"My name is {str(self.name)} and i'm running and need {self.energy_for_run} e.p. for run")
            self.energy = self.energy - self.energy_for_run
        else:
            print(f"My name is {str(self.name)} and i can't run because my energy is low")


class FlyAnimal(Animal):
    def __init__(self, name, energy, energy_for_fly):
        Animal.__init__(self,name, energy)
        self.energy_for_fly = energy_for_fly

    def fly(self):
        if self.energy >= self.energy_for_fly:
            print(f"My name is {str(self.name)} and i'm flying and need {self.energy_for_fly} e.p. for fly")
            self.energy = self.energy - self.energy_for_fly
        else:
            print(f"My name is {str(self.name)} and i can't fly because my energy is low")







# Классы наследники
class Cat(Animal):
    def __init__(self, name, energy = 100):
        Animal.__init__(self, name, energy)

class Tiger(SwimAnimal, RunAnimal):
    def __init__(self, name, energy = 100):
        # значения energy_for_swim, energy_for_run можно задавать, передавая в __init__
        SwimAnimal.__init__(self, name, energy, energy_for_swim = 40) 
        RunAnimal.__init__(self, name, energy, energy_for_run = 20)

class SuperDuck(SwimAnimal, RunAnimal, FlyAnimal):
    def __init__(self, name, energy = 100):
        SwimAnimal.__init__(self, name, energy, energy_for_swim = 40)
        RunAnimal.__init__(self, name, energy, energy_for_run = 20)
        FlyAnimal.__init__(self, name, energy, energy_for_fly = 10)




# cat = Cat('Tom')
# cat.say()
# cat.fly()
# cat.run()
# cat.swim()
# print(cat.get_energy())

# tig = Tiger('Alex',1100)
# tig.say()
# tig.fly()
# tig.run()
# tig.swim()
# print(tig.get_energy())

# duck = SuperDuck('Donald',1100)
# duck.say()
# duck.fly()
# duck.run()
# duck.swim()
# print(duck.get_energy())