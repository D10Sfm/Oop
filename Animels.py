"""Animels Class"""
class Animels:
    def __init__(self,age,land_of_origin,family):
        self.age = age
        self.land_of_origin = land_of_origin
        self.family = family
    def getAge(self):
        return self.age
    def getFamily(self):
        return self.family
    def getLand_of_origin(self):
        return self.land_of_origin
    def setAge(self,age):
        self.age = age
    def setFamily(self,family):
        self.family = family
    def setLand_of_origin(self,land_of_origin):
        self.land_of_origin = land_of_origin
    def __str__(self):
        return str(self.age)+" "+self.land_of_origin+" "+self.family
