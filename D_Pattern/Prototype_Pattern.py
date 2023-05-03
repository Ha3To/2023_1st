# class Cat:
#     def __init__(self):
#         self.color = None
#         self.eye_color = None
#         self.nose_color = None
#         self.tail_color = None
#         self.name = None

# kitty = Cat()
# kitty.color = 'white'
# kitty.eye_color = 'white'
# kitty.nose_color = 'white'
# kitty.tail_color = 'white'
# kitty.name = 'kitty'

# nabi = Cat()
# nabi.color = 'white'
# nabi.eye_color = 'white'
# nabi.nose_color = 'white'
# nabi.tail_color = 'white'
# nabi.name = 'nabi'

'''
눈, 코, 몸, 꼬리 색은 모두 동일하고,이름만 다른 고양이를 만들기위해 모든 propertty를 하나씩 따로 지정하는 것은 비효율적임
그래서 다음과 같은 방법(프로토타입)으로 만들면 효율적임
'''

import copy
class Cat:
    def __init__(self):
        self.color = None
        self.eye_color = None
        self.nose_color = None
        self.tail_color = None
        self.name = None

        #copy.deepcopy를 이용하면 단순히 레이블만 바꾸는 것이 아닌, 완전히 다른 메모리를 할당받는 객체를 생성
        def clone(self):
            return copy.deepcopy(self)

#최초 한번은 초기화겸 한개의 객체를 만들어야함
kitty = Cat()
kitty.color = 'white'
kitty.eye_color = 'white'
kitty.nose_color = 'white'
kitty.tail_color = 'white'
kitty.name = 'kitty'

#kitty의 객체를 복사하여 nabi객체를 만든다.
nabi = kitty.clone()
nabi.name = 'nabi'

'''
위 방식으로 고양이를 만들면, 속성은 같지만 이름만 다른 nabi를 copy를 이용하여 쉽게 만들어낼 수 있다.

nabi = kiity => 이건 안되는 이유는 단순 레이블만 바뀐다.
1. kitty가 Cat()이라는 객체를 가리키고있음
2. nabi가 Cat()에 연결되면서 kitty는 Cat()과의 연결을 끊는다.
3. 2개의 객체를 가리키지 못하는 상황 그래서, deepcopy를 통해 nabi만의 객체를 생성해줘야함
'''