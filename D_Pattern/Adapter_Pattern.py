#-----------Adaptee------------
class Banner():

    def __init__(self, word):
        self.word = word

    def showWithParen(self):
        print("(" + self.word + ")")

    def showWithAster(self):
        print("*" + self.word + "*")
#-------------------------------

#-----------Target--------------
class Print():

    def printWeak(self):
        pass
    def printStrong(self):
        pass
#--------------------------------

#-----------Adapter--------------
class PrintBanner(Banner, Print):
    def __init__(self, word):
        super(PrintBanner, self).__init__(word)

    def printWeak(self):
        self.showWithParen()

    def printStrong(self):
        self.showWithAster()
#--------------------------------

#-----------Adapter2-------------
# class PrintBanner(Print):
#     def __init__(self, word):
#         self.banner = Banner(word)

#     def printWeak(self):
#         self.banner.showWithParen()

#     def printStrong(self):
#         self.banner.showWithAster()
# 위임을 통해서도 Adapter패턴을 적용할 수 있다.
#--------------------------------

#-----------Client---------------
pb = PrintBanner("hello")
pb.printStrong()
pb.printWeak()
#--------------------------------

'''
result: *hello*
        (hello)

Adapter패턴은 이미 제공되어있는 부분(Adaptee)과 필요한 부분(Target)간의 차이를 Adapter를 이용하여 없애서
Client를 수정하지 않고 기능을 사용하도록 하는 패턴이다.

여기서는 Banner는 이미 제공되는 기능이고, 클라이언트는 printStrong, printWeak라는 기존에 사용되는 시스템이 있는 상황
하지만 Banner의 기능을 그대로 가져와서 사용할순없으니, Adapter를 만들어서 기능을 가져온다.

PrintBanner는 Banner와 Print 클래스를 둘다 상속받아서 super로 Banner의 기능을 가져오고,
printWeak와 printStrong을 사용하더라도 실제기능은 showWithParen과 showWithAster를 사용한다.
물론 Client는 기존에 사용하는 함수명을 그대로 유지하면서 말이다.
'''