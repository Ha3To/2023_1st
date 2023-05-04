from abc import *

class ParentClass(metaclass=ABCMeta):

    field1 = 0
    field2 = 0

    @abstractmethod
    def methodA(self):
        pass

    def methodB(self):
        pass

class ChildClass(ParentClass):

    def methodA(self):
        print("methodA is implemented", field1)

    def methodC(self):
        print("methodC is defined")

# 상위클래스에서 (metaclass=ABCMeta)를 작성해주고, @abstractmethod를 달아주면
# 반드시 하위클래스에서 @abstractmethod부분에 있는 메소드들을 구현하여야한다. 안그러면 에러남