#----------Component----------
class Animal:
    def speak(self):
        pass
#-----------------------------

#----------Concreat-----------
class Cat(Animal):
    def speak(self):
        print("meow", end='')

class Dog(Animal):
    def speak(self):
        print("bark", end='')
#------------------------------

#--------Polymorphism----------
def makeSpeak(animal: Animal):
    animal.speak()
    print(" ")
#------------------------------

#----------Decorator-----------
class Deco(Animal):
    def __init__(self, animal: Animal):
        self.animal = animal
    def speak(self):
        self.animal.speak()

'''
    Animal과 동일한 인터페이스를 가지고 있음
    Animal에서 상속받고 constructor에서 Animal을 property로 가지고 있고
    speak는 Animal의 speak함수 호출
'''
#------------------------------

#--------ConcreatDeco----------
class WithSmile(Deco):
    def speak(self):
        self.animal.speak()
        print("😀",end='')

class WithHeartEyes(Deco):
    def speak(self):
        self.animal.speak()
        print("😍",end='')

'''
    WithSmile, WithHeartEyes는 Deco를 상속받고 부모인 Deco 내부에 있는 Animal에서
    Speak를 호출 하고 각각 이모지를 print
'''
#------------------------------


kitty = Cat()
makeSpeak(kitty)
kitty_smile = WithSmile(kitty)
makeSpeak(kitty_smile)
kitty_smile_heart = WithHeartEyes(kitty_smile)
makeSpeak(kitty_smile_heart)