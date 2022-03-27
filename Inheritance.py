'''Inheritance - ירושה'''
# class Students:
#     def __init__(self,name,id,age):
#         self.__name = name
#         self.__id = id
#         self.__age = age
#         self.__grade = [1]
#     def GetterID(self):
#         return self.__id
#     def GetterName(self):
#         return self.__name
#     def GetterGrade(self):
#         return self.__grade
#     def GetterAge(self):
#         return self.__age
#     def setName(self,name):
#         self.__name = name
#     def setID(self,id):
#         self.__id = id
#     def setAge(self,age):
#         self.__age = age
#     def setGrade(self,grade):
#         self.__grade.append(grade)
#     def __str__(self):
#         return self.__name+" "+str(self.__id)+" "+str(self.__age)+"\n"+str(self.__grade)+"\n"+str(self.getAvgGrade())
#     def getAvgGrade(self):
#         x = round(sum(self.__grade)/(len(self.__grade)-1))
#         return x
#
# class Automation(Students):
#     def __init__(self, name, id,age, classid):
#         super().__init__(name,id,age)
#         self.classid = classid
#     def getClassId(self):
#         return self.classid
#     def setClassId(self,classid):
#         self.classid = classid
#     def addGrade(self,grade):
#        grade = super().setGrade(grade)
#     def __str__(self):
#       return  super().__str__()+"\n"+str(self.classid)
#
# class Full_Stack(Students):
#     def __init__(self, name, id,age, classid):
#         super().__init__(name,id,age)
#         self.classid = classid
#     def getClassId(self):
#         return self.classid
#     def setClassId(self,classid):
#         self.classid = classid
#     def addGrade(self,grade):
#        grade = super().setGrade(grade)
#     def __str__(self):
#       return  super().__str__()+"\n"+str(self.classid)
#
#
# class Devnet(Students):
#     def __init__(self, name, id,age, classid):
#         super().__init__(name,id,age)
#         self.classid = classid
#     def getClassId(self):
#         return self.classid
#     def setClassId(self,classid):
#         self.classid = classid
#     def addGrade(self,grade):
#        grade = super().setGrade(grade)
#     def __str__(self):
#       return  super().__str__()+"\n"+str(self.classid)
#
# class Selsforce(Students):
#     def __init__(self, name, id,age, classid):
#         super().__init__(name,id,age)
#         self.classid = classid
#     def getClassId(self):
#         return self.classid
#     def setClassId(self,classid):
#         self.classid = classid
#     def addGrade(self,grade):
#        grade = super().setGrade(grade)
#     def __str__(self):
#       return  super().__str__()+"\n"+str(self.classid)
#
# class Manual_QA(Students):
#     def __init__(self, name, id,age, classid):
#         super().__init__(name,id,age)
#         self.classid = classid
#     def getClassId(self):
#         return self.classid
#     def setClassId(self,classid):
#         self.classid = classid
#     def addGrade(self,grade):
#        grade = super().setGrade(grade)
#     def __str__(self):
#       return  super().__str__()+"\n"+str(self.classid)
# s1 = Automation("yalam",12346,27,10)
# s1.setGrade(85)
# s1.setGrade(100)
# s1.setGrade(55)
# print(s1)
# s2= Full_Stack("yossef",12364,25,11)
# s2.setGrade(100)
# s2.setGrade(75)
# s2.setGrade(89)
# s2.setGrade(95)
# print(s2)
# s3 = Devnet("miki",14563,24,12)
# s3.setGrade(100)
# s3.setGrade(100)
# s3.setGrade(89)
# s3.setGrade(75)
# print(s3)
# s4 = Selsforce("Solomon",20846,24,13)
# s4.setGrade(85)
# s4.setGrade(95)
# s4.setGrade(100)
# s4.setGrade(95)
# s4.setGrade(77)
# print(s4)
'''------------------'''
# Exercise
# QA1
from Cars import Cars
from Trains import Trains
from Bycycle import Bycycle
from Plains import Plains
train1 = Trains(200,'black',"TfhTrain2000",4)
train2 = Trains(178,'yellow',"SfPlatinum2000",12)
train3 = Trains(320,'black/white',"AlphaSS3000",1)
plain1 = Plains(4,"white","Loftahnzasrs",12000)
plain2 = Plains(6,"blaugrana","AirBus2000",120)
plain3 = Plains(7,"black","Totto12S",15000)
car1 = Cars(4,"gray","honda",120000)
car2 = Cars(4,"white","hyundai",70000)
car3 = Cars(4,"white/black","BMW",50000)
bycycle1 = Bycycle(2,'brown','kalfon',16)
bycycle2 = Bycycle(2,'black','kalfon',12)
bycycle3 = Bycycle(2,'gold','Bolt',14)
a = car1.__dict__  #"""from 196 line to 204 line ,outside the QA"""
b = a.values()
c = a.items()
for i in a:
    print(i)
for i in b:
    print(i)
for i in c:
    print(i)
print(plain2,bycycle1,car3,train2,sep="\n")
car3.setColor("black\gold")
print(car3)
print(train2)

# QA2
from Tiger import Tiger
tiger1 = Tiger(4,"India",4)
tiger2 = Tiger(6,"Russia",4)
tiger3 = Tiger(3,'Bendeglash',4)
from Lion import Lion
lion1 = Lion(10,"Kenia",4)
lion2 = Lion(3,"Jerusalem",4)
lion3 = Lion(7,"North korea",4)
from Horse import Horse
horse1 = Horse(8,"Lebanon",4)
horse2 = Horse(4,"Wesex",4)
horse3 = Horse(6,"Mongolia",4)
from Donkey import Donkey
donkey1 = Donkey(6,"Ireland",4)
donkey2 = Donkey(5,"Cyprus",4)
donkey3 = Donkey(2,"Peru",4)
print(donkey1,horse2,lion3,tiger1,sep="\n")
