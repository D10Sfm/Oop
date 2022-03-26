from Mammels import Mammals
class Horseshoe(Mammals):
    def __init__(self,age,family,land_of_origin,no_legs,gender,breed):
        if super().family == "mammals" and super().gender == "horseshoe":
            super().__init__(age,family,land_of_origin,no_legs,gender)
            self.breed = breed
    def getBreed(self):
        return self.breed
    def setBreed(self,breed):
        self.breed = breed
    def __str__(self):
        return super().__str__()+" "+self.breed