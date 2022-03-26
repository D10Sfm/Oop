"""Animels Class"""
class Animels:
    def __init__(self,age,family,land_of_origin):
        self.age = age
        self.family = family
        self.land_of_origin = land_of_origin
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
        return str(self.age)+" "+self.family+" "+self.land_of_origin
