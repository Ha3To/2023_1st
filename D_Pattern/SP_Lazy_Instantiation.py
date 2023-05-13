class LazyInstantiation:
    _instance = None
    def __init__(self):#객체의 존재여부를 확인하는 부분
        if not LazyInstantiation._instance:
            print('__init__method called but nothing is created')
        else:
            print('instance already created:', self.getInstance())
        
    @classmethod
    def getInstance(cls):#객체를 만드는 static method부분
        if not cls._instance:
            cls._instance = LazyInstantiation()
        return cls._instance

s = LazyInstantiation() #클래스를 초기화 했으나 객체는 생성되지 않음
print(s._instance)
s1 = LazyInstantiation.getInstance() #객체가 생성됨
s2 = LazyInstantiation()
