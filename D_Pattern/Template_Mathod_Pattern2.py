class AbstractDisplay:
    def open(self):
        pass

    def textPrint(self):
        pass

    def close(self):
        pass

    def display(self):
        self.open()

        for i in range(5):
            self.textPrint()

        self.close()

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<", end=" ")
    
    def textPrint(self):
        print(self.ch, end=" ")

    def close(self):
        print(">>")

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def open(self):
        self.printLine()

    def textPrint(self):
        print("|" + self.string + "|")

    def close(self):
        self.printLine()

    def printLine(self):
        print("+", end="")
        for i in range(self.width):
            print("-", end="")

        print("+")