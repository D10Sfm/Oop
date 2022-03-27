from Vehicles import Vehicles
class Bycycle(Vehicles):
    def __init__(self,wheels,color,model,size):
        super().__init__(wheels,color,model)
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size = size
    def __str__(self):
        return super().__str__()+" "+str(self.size)