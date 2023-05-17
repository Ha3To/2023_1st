from abc import *
import copy

#----------Prototype----------

class Product(metaclass = ABCMeta):

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def clone(self):
        pass

#---------------------------------------

#----------Concreat_Prototype----------

class UnderlinePen(Product):

    def use(self, s:str):
        n = len(s)
        print(s)
        for i in range(n):
            print("~", end="")
        print()

    def clone(self):
        return copy.deepcopy(self)
    
class MessageBox(Product):

    def __init__(self, deco:str):
        self.deco = deco

    def use(self, s:str):
        n = len(s) + 4

        for i in range(n):
            print(self.deco, end="")
        print()
        print(self.deco, s, self.deco)
        for i in range(n):
            print(self.deco, end="")
        print()
    
    def clone(self):
        return copy.deepcopy(self)

#---------------------------------------

#----------Manager----------
#클라이언트에서 편리하게 사용하기위한 Manager클래스

class Manager():

    def __init__(self):
        self.showcase = {"a":1}#dict를 가지고있음
        #프로토타입의 인스턴스 => 모범 모델

                            #이 친구들은 스트링형태로 짝을 지어서 Product에 삽입
    def register(self, name:str, proto:Product):
        self.showcase[name] = proto #dict에 추가
    '''
    각각의 객체(msg*, msg#, pen)이름을 붙여주고, Product객체를 넘겨줘서 등록을해주는 형태
    '''
    
    #showcase에 product을 담아놓으면 ProtoName(=> msg*, msg#, pen)으로 참조 후, 해당 오브젝트 복사 후 생성
    def create(self, protoName):
        p = self.showcase[protoName]
        return p.clone()

#---------------------------------------

#----------------Client-----------------------
manager = Manager()

#모든 객체의 프로토타입을 최초 생성
#=> object가 copy되기 전까지 상태를 prototype으로 가지고 있으라는 의미(아직 실사용 x)
m1 = MessageBox("*")
m2 = MessageBox("#")
p1 = UnderlinePen()

#위에서 생성된 객체들을 manager.register()를 통해 모범 케이스로 등록해주기
manager.register("msg*", m1)
manager.register("msg#", m2)
manager.register("pen", p1)

#Manager가 msg*, msg#, pen을 가지고 있음
#그리고, manager.create()에다가 각각의 이름을 넘겨줘서 사용함(이제부터 실사용)
msg1 = manager.create("msg*")
msg2 = manager.create("msg#")
pen = manager.create("pen")
'''
이름을 통해서 객체를 만들어서 실사용하는데
그 이유는 framework과 생성하는 인스턴스를 분리하기 위해서
=> 디펜던시를 낮추고, 언제든지 '이름'을 참조해서 그 인스턴스을 사용할 수 있다.
'''

#출력1
word = "hello"
msg1.use(word)

#출력2
word = "world"
msg2.use(word)

#3출력3
pen.use(word)