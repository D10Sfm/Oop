"""Mammals Class"""
from Animels import Animels
class Mammals(Animels):
    def __init__(self,age,land_of_origin,no_legs,gender):
            super().__init__(age,land_of_origin,family="mammals")
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
        return super().__str__()+" "+self.gender+" "+str(self.no_legs)