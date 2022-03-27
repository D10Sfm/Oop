from Mammels import Mammals
class Predators(Mammals):
    def __init__(self,age,land_of_origin,no_legs,breed):
            super().__init__(age,land_of_origin,no_legs,gender="predator")
            self.breed = breed
    def getBreed(self):
        return self.breed
    def setBreed(self,breed):
        self.breed = breed
    def __str__(self):
        return super().__str__()+" "+self.breed