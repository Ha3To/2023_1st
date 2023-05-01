
#-------------Target-------------
class Animal:
    def walk(self):
        pass

class Cat(Animal):
    def walk(self):
        print("cat walking")

class Dog(Animal):
    def walk(self):
        print("dog walking")

def makeWalk(animal: Animal):
    animal.walk()
#--------------------------------

#----------주어진것----------------
class Fish:
    def swim(self):
        print("fish swimming")
#--------------------------------

#-------------Adapter------------
class FishAdapter(Animal):
    def __init__(self, fish:Fish):
        self.fish = fish

    def walk(self):
        self.fish.swim()
#--------------------------------

kitty = Cat()
bingo = Dog()

makeWalk(kitty)
makeWalk(bingo)

nemo = Fish()
# makeWalk(nemo) 
# => Fish class의 nemo object를 만들어서 makeWalk 함수로 넘겨주면 Error발생

adapted_nemo = FishAdapter(nemo)
makeWalk(adapted_nemo)
# Nemo는 Fish Object이고 adapted_nemo는 FishAdapter에 nemo를 넘겨줌
# MakeWalk에 adapted_nemo를 넘겨주면 Fish의 Swim interface를 FishAdapter의 walk를 통해 호출