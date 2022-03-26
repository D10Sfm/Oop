"""Mammals Class"""
from Animels import Animels
class Mammals(Animels):
    def __init__(self,age,family,land_of_origin,no_legs,gender):
        if super().family == "mammals":
            super().__init__(age,family,land_of_origin)
            self.no_legs = no_legs
            self.gender = gender

    def getNo_legs(self):
        return self.no_legs
    def getGender(self):
        return self.gender
    def setNo_legs(self,no_legs):
       self.no_legs = no_legs
    def setGender(self,gender):
        self.no_legs = gender
    def __str__(self):
        return super().__str__()+" "+str(self.no_legs)+" "+self.gender