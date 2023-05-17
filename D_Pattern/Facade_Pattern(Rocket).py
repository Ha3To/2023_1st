class Stage1:
    def ignite(self):
        print('1st stage ignite')
    def liftOff(self):
        print('1st stage liftOff')
    def eject(self):
        print('1st stage eject')
    def comeBack(self):
        print('1st stage return')

class Stage2:
    def ignite(self):
        print('2nd stage ignition')
    def eject(self):
        print('2nd stage eject')

class Capsule:
    def ignite(self):
        print('capsule ignition')
    def landing(self):
        print('capsule landing / deploy')

class Rocket:
    def __init__(self):
        self.stage1 = Stage1()
        self.stage2 = Stage2()
        self.capsule = Capsule()

    def launch(self):
        self.stage1.ignite()
        self.stage1.liftOff()
        self.stage1.eject()
        self.stage2.ignite()
        self.stage1.comeBack()
        self.stage2.eject()
        self.capsule.ignite()
        self.capsule.landing()

rocket = Rocket()
rocket.launch()