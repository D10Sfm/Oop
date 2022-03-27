from Mammels import Mammals
class Horseshoe(Mammals):
    def __init__(self,age,land_of_origin,no_legs,breed):
            super().__init__(age,land_of_origin,no_legs,gender="horseshoe")
            self.breed = breed
    def getBreed(self):
        return self.breed
    def setBreed(self,breed):
        self.breed = breed
    def __str__(self):
        return super().__str__()+" "+self.breed