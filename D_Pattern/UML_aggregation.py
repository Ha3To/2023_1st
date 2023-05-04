class Color():
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

class Fruit():
    def __init__(self):
        self.color = Color()

class Basket():
    def __init__(self):
        self.fruits = []

        for i in range(10):
            self.fruits.append(Fruit())

# Fruit는 Color에 구현 / Basket은 Fruit의 구현 클래스이므로 서로 집약관계임을 알수있다.