class MonoState:
    __shared_state = {"1":"2"}#dictionary

    def __init__(self):
        self.x = 1 #속성 = 상태
        self.__dict__ = self.__shared_state #dict = 클래스인스턴스가 내부의 속성들을 실질적으로 보관하고있는 변수(클래스의 정의된 변수정보들을 딕션어리({"key1:value1", "key2:value2"}) 형태로 보관)
        pass

ms1 = MonoState()
ms2 = MonoState()

print(ms1)
print(ms2)

ms2.x = 10

print(ms1.x)
print(ms2.x)

'''
객체마다 자신만의 속성(상태)을 가진 dict가 있는데 __shared_state를 참조하게 함으로서 기존 dict는 소멸되고
모든 객체가 __shared_state를 참조하게됨(생성즉시)

result: <__main__.MonoState object at 0x1023cc760>
        <__main__.MonoState object at 0x1023cc940>
        10
        10
ms1, ms2는 서로 주소는 다르지만(다른 객체임을 의미) ms2.x의 값을 10으로 변경했을때 ms1도 같이 적용되는 것을 알 수 있음
'''