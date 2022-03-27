from Vehicles import Vehicles
class Plains(Vehicles):
    def __init__(self,wheels,color,model,flight_hs=0):
        super().__init__(wheels,color,model)
        self.flight_hs = flight_hs
    def getFlight_Hs(self):
        return self.flight_hs
    def setFlight_Hs(self,flight_hs):
        self.flight_hs = flight_hs
    def __str__(self):
        return super().__str__()+" "+str(self.flight_hs)