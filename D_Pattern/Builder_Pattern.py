import random

# Actor 클래스
'''
생성되는 캐릭터(주인공, 몬스터)들의 기본적인 수치들을 생성 및 출력
'''
class Actor:
    def __init__(self, x, y, vitality, agility, strength):
        self.x = x
        self.y = y
        self.vitality = vitality
        self.agility = agility
        self.strength = strength
        

    def print(self):
        return print("X-axis:", self.x, "Y-axis:", self.y, "Vitality:", self.vitality, "Agility:", self.agility, "Strength:", self.strength)

# ActorBuilder 클래스
'''
상위 빌더이며, 캐릭터들의 수치들을 구체화하는 부분
'''
class ActorBuilder:
    def __init__(self):
        self.x = None
        self.y = None

        self.vitality = None
        self.agility = None
        self.strength = None

    def set_X(self, x):
        self.x = max(0, min(x, 100))
        return self
    
    def set_Y(self, y):
        self.y = max(0, min(y, 100))
        return self
    
    def setVitality(self, vitality):
        self.vitality = vitality
        return self
    
    def setAgility(self, agility):
        self.agility = agility
        return self
    
    def setStrength(self, strength):
        self.strength = strength
        return self
    
    def build(self):
        actor = Actor(self.x, self.y, self.vitality, self.agility, self.strength)
        return actor

# MonsterBuilder 클래스
'''
몬스터 콘크리트 빌더, ActorBuilder의 구조를 상속받음

'''
class MonsterBuilder(ActorBuilder):

    def __init__(self):
        super().__init__()
        print("[Monster]", end=" ")

# HeroBuilder 클래스
'''
주인공 콘크리트 빌더, ActorBuilder의 구조를 상속받음
'''
class HeroBuilder(ActorBuilder):
    def __init__(self):
        super().__init__()
        print("[Hero]", end=" ")


# 주인공은 사용자로부터 임의의 값을 입력받아 캐릭터 생성, 다만 x, y의 값이 0보다 작으면 0, 100보다 크면 100으로 조정됨
print("주인공의 위치(x, y)값, 생명력, 능력, 근력 수치를 입력하세요.")
x, y, Vital, Agi, Str = map(int, input().split())

Hero = HeroBuilder().set_X(x).set_Y(y).setVitality(Vital).setAgility(Agi).setStrength(Str).build()
Hero.print()

# 몬스터는 모든 수치가 임의의 수치(xy는 0~100 / 체력, 민첩성, 힘은 50~ 100)로 모든 수치 적용
Monster = MonsterBuilder().set_X(random.randint(0, 101)).set_Y(random.randint(0, 101)).setVitality(random.randint(50, 101)).setAgility(random.randint(50, 101)).setStrength(random.randint(50, 101)).build()
Monster.print()