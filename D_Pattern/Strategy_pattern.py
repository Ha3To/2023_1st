from abc import *

#API부분
class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def offensive(self):
        pass

#콘크리트 1 ~ 3
class Sword(Weapon):
    def offensive(self):
        print("칼을 휘두르다")

class Shield(Weapon):
    def offensive(self):
        print("방패로 밀치다")

class CrossBow(Weapon):
    def offensive(self):
        print("활을 쏘다")


#컨텍스트(전략 등록 / 실행)
class TakeWeaponStrategy:

    def __init__(self):
        self.weapon = 0
        self.move = 0

    def setWeapon(self, weapon:Weapon):
        self.weapon = weapon

    def setMove(self, move:Move):
        self.move = move

    def moving(self):
        self.move.

    def attack(self):
        self.weapon.offensive()

#클라이언트
#플레이어가 손에 무기 착용 전략을 설정
hand = TakeWeaponStrategy()

#플레이어가 검을 들도록 전략 설정
hand.setWeapon(Sword())
hand.attack()

#플레이어가 방패을 들도록 전략 설정
hand.setWeapon(Shield())
hand.attack()

#플레이어가 석궁을 들도록 전략 설정
hand.setWeapon(CrossBow())
hand.attack()

'''
result: 칼을 휘두르다
        방패로 밀치다
        활을 쏘다
'''