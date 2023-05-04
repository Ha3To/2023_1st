from abc import *

class Printable(metaclass=ABCMeta):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def newPage(self):
        pass

class PrintClass(Printable):

    def show(self):
        print("show implemented")

    def newPage(self):
        print("newPage implemented")

pc = PrintClass()

pc.show()

# class Printable에서 추상메소드를 만들어놓고(추상클래스)
# class PrintClass에서 구현한다(구현클래스)