#----------Component----------
class Display:

    def getColumns(self):
        pass

    def getRows(self):
        pass

    def getRowText(self, row):
        pass

    def show(self):
        n = self.getRows()
        for i in range(n):
            print(self.getRowText(i))
#-----------------------------

#----------Concreat-----------
class StringDisplay(Display):
    def __init__(self, letters):
        self.letters = letters

    def getColumns(self):
        return len(self.letters)
    
    def getRows(self):
        return 1
    
    def getRowText(self, row):
        if row == 0:
            return self.letters
        else:
            return -1
#------------------------------

#----------Decorator-----------
class Deco(Display):
    def __init__(self, display: Display):
        self.display = display
#------------------------------

#--------ConcreatDeco----------
class SideBorder(Deco):

    def __init__(self, display, deco):
        super().__init__(display)
        self.borderDeco = deco

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return self.display.getRows()
    
    def getRowsText(self, row):
        return self.borderDeco + self.display.getRowText(row) + self.borderDeco
    
class FullBorder(Deco):

    def __init__(self, display):
        super().__init__(display)

    def getColumns(self):
        return 1 + self.display.getColumns() + 1
    
    def getRows(self):
        return 1 + self.display.getRows() + 1
    
    def makeLine(self, deco, count):
        buffer = ""
        for i in range(count):
            buffer += deco
        return buffer
    
    def getRowText(self, row):
        if row == 0:
            return "+" + self.makeLine("-", self.display.getColumns()) + "+"
        elif row == (self.display.getRows() + 1):#인덱스 -> 개수
            return "+" + self.makeLine("-", self.display.getColumns()) + "+"
        else:
            return "|" + self.display.getRowText(row-1) + "|"

'''
    이미 콘크리트 데코들은 데코의 속성값(컴포넌트의 속성값)을 가지고 있음
'''
#------------------------------

b1 = StringDisplay("hello")
b2 = SideBorder(b1, "#")
b3 = FullBorder(b2)
b1.show()
b2.show()
b3.show()

b1 = StringDisplay("hello, world")
b1 = FullBorder(b1)
b1.show()

a = StringDisplay("hello")
a = FullBorder(a)
a = SideBorder(a, "*")
a = FullBorder(a)
a = FullBorder(a)
a = SideBorder(a, "/")
a.show()