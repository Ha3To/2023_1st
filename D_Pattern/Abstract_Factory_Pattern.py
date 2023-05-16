class Button:
    def click(self):
        pass

class DarkButton(Button):
    def click(self):
        print("dark click")

class LightButton(Button):
    def click(self):
        print("light click")

class RedButton(Button):
    def click(self):
        print("red click")

class BlueButton(Button):
    def click(self):
        print("blue click")

'''
버튼을 담당하는 부분 click되었을때
색깔별 하위 클래스에서 click을 구체화하여 실행
'''

# ============================================

class CheckBox:
    def check(self):
        pass

class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")

class LightCheckBox(CheckBox):
    def check(self):
        print("light check")

class RedCheckBox(CheckBox):
    def check(self):
        print("red check")

class BlueCheckBox(CheckBox):
    def check(self):
        print("blue check")

'''
버튼을 담당하는 부분 check되었을때
색깔별 하위 클래스에서 check을 구체화하여 실행
'''

# ============================================

class ScrollBar:
    def scroll(self):
        pass

class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("dark scroll")

class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light scroll")

class RedScrollBar(ScrollBar):
    def scroll(self):
        print("red scroll")

class BlueScrollBar(ScrollBar):
    def scroll(self):
        print("blue scroll")

'''
버튼을 담당하는 부분 scroll되었을때
색깔별 하위 클래스에서 scroll을 구체화하여 실행
'''

# ============================================

class Slider:
    def slid(self):
        pass

class DarkSlider(Slider):
    def slid(self):
        print("dark slid")

class LightSlider(Slider):
    def slid(self):
        print("light slid")

class RedSlider(Slider):
    def slid(self):
        print("red slid")

class BlueSlider(Slider):
    def slid(self):
        print("blue slid")

'''
버튼을 담당하는 부분 slid되었을때
색깔별 하위 클래스에서 slid을 구체화하여 실행
'''

# ============================================

class TextBox:
    def text(self):
        pass

class DarkTextBox(TextBox):
    def text(self):
        print("dark text")

class LightTextBox(TextBox):
    def text(self):
        print("light text")

class RedTextBox(TextBox):
    def text(self):
        print("red text")

class BlueTextBox(TextBox):
    def text(self):
        print("blue text")

'''
버튼을 담당하는 부분 text되었을때
색깔별 하위 클래스에서 text을 구체화하여 실행
'''

# ============================================

class UIFactory:
    def getButton(self):
        pass

    def getCheck(self):
        pass

    def getScrollBar(self):
        pass

    def getSlider(self):
        pass

    def getTextBox(self):
        pass

'''
상위 팩토리 여기서 기능을 호출
'''

# ============================================

class DarkFactory(UIFactory):

    def getButton(self):
        return DarkButton()

    def getCheck(self):
        return DarkCheckBox()

    def getScrollBar(self):
        return DarkScrollBar()

    def getSlider(self):
        return DarkSlider()

    def getTextBox(self):
        return DarkTextBox()
    
class LightFactory(UIFactory):

    def getButton(self):
        return LightButton()

    def getCheck(self):
        return LightCheckBox()

    def getScrollBar(self):
        return LightScrollBar()

    def getSlider(self):
        return LightSlider()

    def getTextBox(self):
        return LightTextBox()
    
class RedFactory(UIFactory):

    def getButton(self):
        return RedButton()

    def getCheck(self):
        return RedCheckBox()

    def getScrollBar(self):
        return RedScrollBar()

    def getSlider(self):
        return RedSlider()

    def getTextBox(self):
        return RedTextBox()
    
class BlueFactory(UIFactory):

    def getButton(self):
        return BlueButton()

    def getCheck(self):
        return BlueCheckBox()

    def getScrollBar(self):
        return BlueScrollBar()

    def getSlider(self):
        return BlueSlider()

    def getTextBox(self):
        return BlueTextBox()

'''
하위 팩토리 여기서 각 색깔별 기능을 각자 호출
'''
# ============================================

df = DarkFactory()
lf = LightFactory()
rf = RedFactory()
bf = BlueFactory()

'''
각 색깔별 제품 생산 요청
'''

# ============================================

bt = df.getButton()
ck = df.getCheck()
sc = df.getScrollBar()
sl = df.getSlider()
tb = df.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slid()
tb.text()

# ============================================

bt = lf.getButton()
ck = lf.getCheck()
sc = lf.getScrollBar()
sl = lf.getSlider()
tb = lf.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slid()
tb.text()

# ============================================

bt = rf.getButton()
ck = rf.getCheck()
sc = rf.getScrollBar()
sl = rf.getSlider()
tb = rf.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slid()
tb.text()

# ============================================

bt = bf.getButton()
ck = bf.getCheck()
sc = bf.getScrollBar()
sl = bf.getSlider()
tb = bf.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slid()
tb.text()