import random
import time

class Memento:

    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money
    
    def addFruit(self, fruit):
        self.fruits.append(fruit)

    def getFruits(self):
        return self.fruits


class Gamer:

    def __init__(self, money):
        self.money = money
        self.fruits = []
        self.fruitsName = ["사과", "포도", "바나나", "귤"]

    def getMoney(self):
        return self.money
    
    def getFruit(self):
        fN = len(self.fruitsName)
        fruitName = self.fruitsName[random.randint(0, fN-1)]
        return "맛있는 " + fruitName
    
    def bet(self):

        dice = random.randint(1, 6)

        if dice == 1:
            self.money += 100
            print("소지금 증가")

        elif dice == 2:
            self.money /= 2
            print("소지슴 절반 감소")

        elif dice == 6:
            f = self.getFruit()
            print("과일 " + f + " 를 받았습니다.")
            self.fruits.append(f)

        else:
            print("아무것도 변한 것이 없습니다.")

    def createMemento(self):
        m = Memento(self.money)

        for f in self.fruits: #deep copy
            m.addFruit(f)

        return m
    
    def restoreMemento(self, memento):
        self.money = memento.money
        self.fruits = memento.fruits

    def printState(self):
        print("[money: " + str(self.money) + ", fruits: ", end="")

        for f in self.fruits:
            print(", " + f, end="")

        print("]")

def gameRun():
    print("game start")
    gamer = Gamer(100)
    memento = gamer.createMemento()

    for i in range(100):
        print("===game turn===, " + str(i))
        gamer.printState()

        gamer.bet()

        print("소지슴이 " + str(gamer.getMoney()) + "원이 되었습니다.")

        #memento 취급 결정
        if gamer.getMoney() > memento.getMoney():
            print("게임을 잘 하고 있으니 현재 상태를 저장")
            memento = gamer.createMemento()

        elif gamer.getMoney() < memento.getMoney()/2:
            print("소지금이 너무 많이 감소해서 이전의 상태로 다시 복원")
            gamer.restoreMemento(memento)

        time.sleep(0.5)
        print()

gameRun()