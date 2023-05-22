class MyInt(type):#type을 상속받았다 = Metaclass임

    def __call__(cls, *args, **kwds):#*가 1개면 인자를 tuple로(a, b, c, d, ...)이런식, 2개면 dictionary로 꾸려서 내부로 전달
        print("myint ", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)

class int(metaclass=MyInt):#메타클래스 지정, 생성시 MyInt의 call이 호출됨
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4, 5)

'''
result: myint (4, 5)
        Now do whatever you want with these objects...
4, 5가 call의 tuple로 들어가서 출력하고, 메시지가 이어서 출력
지금은 메시지만 출력했지만 제어문을 넣으면 데이터를 가지고 먼저 생성에 관여할 수 있다.
'''