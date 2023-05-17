import copy

#--------[Prototype]---------
class Cat:
    def __init__(self):
        self.color = None
        self.eye_color = None
        self.nose_color = None
        self.tail_color = None
        self.name = None

        def clone(self):
            return copy.deepcopy(self)

#--------[Concreat_Prototype]---------
class BlackCat(Cat):
    def __init__(self):
        super().__init__()
        self.color = 'black'

class WhiteCat(Cat):
    def __init__(self):
        super().__init__()
        self.color = 'white'

'''
BlackCat을 먼저 만들면 그 다음부터는 계속해서 복제하여 각각의 객체에 맞게 속성값을 부여하면됨
여기서는 고양이의 색깔만 바꾸지만 눈, 코, 꼬리도 각각의 객체에 맞게 변경ㄱㄴ
'''