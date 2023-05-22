class MetaSingleton(type):#type이 들어왔으므로 메터클래스가 된거임
    _instances = {}#프라이빗변수를 만들어두기

    #call함수에 객체의 존재여부 확인하는 부분
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:#객체가 없으면 만들어서 리턴하셈ㅋ
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwds)

        return cls._instances[cls]

class Box( metaclass = MetaSingleton):#메타클래스 지정 => Box클래스를 싱글톤으로 지정했다.
    pass

b1 = Box()
b2 = Box()

print(b1==b2)#싱글톤이기에 동일한 인스턴스임을 알 수 있다.
