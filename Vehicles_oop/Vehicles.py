
class Vehicles:
    def __init__(self,wheels,color,model):
        self.wheels = wheels
        self.color = color
        self.model = model
    def __str__(self):
        return str(self.wheels)+" "+self.color+" "+self.model
    def GetWheels(self):
        return self.wheels
    def GetColor(self):
        return self.color
    def GetModel(self):
        return self.model
    def setWheels(self,wheels):
        self.wheels = wheels
    def setColor(self,color):
        self.color = color
    def setModel(self,model):
        self.model = model