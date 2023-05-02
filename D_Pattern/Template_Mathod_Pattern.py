#-----------------기본 틀(Template)-------------
class BasicRamenRecipe:
    def cookRamen(self):
        self.boilWater()
        self.addRamen()
        self.addons()
        self.wait()

    def boilWater(self):
        print("boil 550ml of water")
    def addRamen(self):
        print("add noodles, soup Base, flakes")
    def addons(self):
        pass
    def wait(self):
        print("cook for 4min 30s")

#----addons라는 기능을 좀 더 특화시킨 버전------
class NocopeRecipe(BasicRamenRecipe):
    def addons(self):
        print("add onions")

#----boilwater, wait 기능을 특화시칸 버전-----
class GrandmaRecipe(BasicRamenRecipe):
    def boilWater(self):
        print("boil 1000ml of water")
    def wait(self):
        print("cook for 10m")