from Vehicles import Vehicles
class Trains(Vehicles):
    def __init__(self,wheels,color,model,years=0):
        super().__init__(wheels,color,model)
        self.years = years
    def getYears(self):
        return self.years
    def setFlight_Hs(self,years):
        self.years = years
    def __str__(self):
        return super().__str__()+" "+str(self.years)