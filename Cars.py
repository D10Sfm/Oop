from Vehicles import Vehicles
class Cars(Vehicles):
    def __init__(self,wheels,color,model,kms=None):
        super().__init__(wheels,color,model)
        self.kms = kms
    def getKms(self):
        return self.kms
    def setKms(self,kms):
        self.kms = kms
    def __str__(self):
        return super().__str__()+" "+str(self.kms)