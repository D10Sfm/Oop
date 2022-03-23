"""Working with oop"""

# x = 1
# print(dir(x))
# print(x.bit_length())
# print(x.__dir__())

# import sys
# class Players:
#         """
#         Creating the players class
#         """
#         def __init__(self,name,age,goals):
#             self.__name = name
#             self.__age = age
#             self.__goals = goals
#         def getName(self):
#             return self.__name
#         def setName(self,name):
#             if name in ["Messi","ronaldo","benzema","neymar","lewandoski","mbappe","pedri"]:
#              self.__name = name
#             else:
#                 return sys.stderr.write("Can't Update name\nthe name not match to the class!")
#         def getAge(self):
#             return self.__age
#         def setAge(self,age):
#             if age in range(17,39):
#              self.__age = age
#             else:
#                return sys.stderr.write("can't update the age\nout of bounce!")
#         def getGoals(self):
#             return self.__goals
#         def setGoals(self,goals):
#             self.__goals = goals
#         def __del__(self):
#             pass
#         def __str__(self):
#             return self.__name+" "+str(self.__age)+" "+str(self.__goals)
#         def __int__(self):
#             return self.goals-50
#
# player1 = Players("Messi",34,759)
# player2 = Players("Ronaldo",37,807)
# player3 = Players("Benzema",34,350)
# player3.setName("lewandoski")
# player3.setGoals(450)
# print(dir(Players))
# import sys


# Exercised
#QA1
# from math import *
# class Square:
#     def __init__(self,color,surface=0):
#         self.__surface = surface
#         self.__color = color
#         self.side = 2.5
#     def __str__(self):
#         return self.__color+str(self.__surface)
#     def getSurface(self):
#         return self.__surface
#     def getColor(self):
#         return self.__color
#     def setSurface(self,surface):
#         self.__surface = surface
#     def setColore(self,color):
#         self.__color = color
#     def getArea(self):
#         self.__surface = self.side**2
#         return self.__surface
# class Circle:
#     def __init__(self,color,surface=0):
#         self.__surface = surface
#         self.__color = color
#         self.__radius = 2.5
#     def getSurface(self):
#         return self.__surface
#     def getColor(self):
#         return self.__color
#     def setSurface(self,surface):
#         self.__surface = surface
#     def setColore(self,color):
#         self.__color = color
#     def getArea(self):
#         self.__surface = self.__radius**2 * pi
#         return self.__surface
#     def __str__(self):
#         return self.__color + str(self.__surface)
# circle = Circle("red")
# square = Square("blue")
# print(Square.getArea(square),Circle.getArea(circle),sep="\n")
# print(Square.getArea(square))
# print(Circle.getArea(circle))
# print(circle.getArea())
# print(square.getArea())

# Qa2
# class Apartment:
#     def __init__(self,address,number,price,avg_rental):
#         self.__address = address
#         self.__number = number
#         self.__price = price
#         self.__avg_rental = avg_rental
#     def yieldd(self):
#         z = self.__avg_rental*12/self.__price
#         return z
#
# apartment1 = Apartment("Gedera,tzivouni",54,250000,3900)
# print("The apartment yield in % is ",apartment1.yieldd())

# class Cats:
#     def __init__(self,name,age,fur_color):
#         self.__name = name
#         self.__age = age
#         self.__fur_color = fur_color
#     def sound(self):
#         return "Miao!!!"
#     def mustash(self):
#         return "Yes!"
# class Dogs:
#     def __init__(self,name,type,color,risk):
#         self.__name = name
#         self.__type = type
#         self.__color = color
#         self.__risk = risk
#     def sound(self):
#         return "Hao hao!!"
#     def biting(self):
#         if self.__risk > 4:
#            return "Yes!"
#         else:
#            return "no"


# cat1 = Cats("Halaf",4,"ginger")
# cat2 = Cats("Mitzi",3,"white")
# dog1 = Dogs("Solomon","Lavrador","yellow",4)
# dog2 = Dogs("Jahloo","Pitbull","Brown\\white",5)
# print("The sound of the animels is ",cat1.sound(),dog1.sound(),"\nIf dog2 are biting?",dog2.biting())

# Q3
# import sys
# class Cars:
#     def __init__(self,wheels,model,year,price):
#         self.__model = model
#         self.__year = year
#         self.__price = price
#         if wheels < 4:
#             self.__wheels = 4
#             print(sys.stderr.write("can't register a car with less than 4 wheels!"))
#         else:
#             self.__wheels = wheels
#     def __str__(self):
#         return self.__model,str(self.__wheels),str(self.__year),str(self.__price)
#     def getWheels(self):
#         return self.__wheels
#     def getModel(self):
#         return self.__model
#     def getYear(self):
#         return self.__year
#     def getPrice(self):
#         return self.__price
#     def getMaxpricedetails(t=1):
#         x = max(car1.getPrice(), car2.getPrice(), car3.getPrice(), car4.getPrice())
#         l = [car1.getPrice(), car2.getPrice(), car3.getPrice(), car4.getPrice()]
#         y = car1.__str__(), car2.__str__(), car3.__str__(), car4.__str__()
#         if t == 1:
#          for (i,r) in zip(l,y):
#             if i == x:
#                 return r
#     def setPara(self,x):
#         if type(x) == str:
#             self.__model = x
#         elif type(x) == int:
#             if x < 100:
#                 self.__wheels = x
#             elif len(str(x)) == 4:
#                 self.__year = x
#             else:
#                 self.__price = x
#     def delPara(self,x):
#         if x == 'model':
#             self.__model = None
#         elif x == 'wheels':
#             self.__wheels = None
#         elif x == 'year':
#             self.__year = None
#         elif x == 'price':
#             self.__price = None
# car1 = Cars(4,"honda",2008,18000)
# car2 = Cars(4,"BMW",2019,250000)
# car3 = Cars(4,"Audi",2020,500000000)
# car4 = Cars(4,"mazerrati",2022,2000000)
# price1 = Cars.getPrice(car1)
# price2 = Cars.getPrice(car2)
# price3 = Cars.getPrice(car3)
# price4 = Cars.getPrice(car4)
# print(Cars.getMaxpricedetails())
# car1.delPara('model')
# car1.setPara('honda')
# print(car1.__str__())
# car1.setPara(6)
# car1.delPara('model')
# print(car1.__str__())
# car1.kms = 15
# print(car1.__str__())
# Qa4
# from datetime import *
# class Student:
#     def __init__(self,name,id,birth_year,class_id,math_grd,history_grd,literature_grd):
#         self.__name = name
#         self.__id = id
#         self.__math_grad = math_grd
#         self.__history_grd = history_grd
#         self.__literature_grd = literature_grd
#         self.__birth_year = birth_year
#         self.__class_id = class_id
#
#     def __str__(self):
#         name = self.__name
#         id = self.__id
#         math_grd = self.__math_grad
#         history_grd = self.__history_grd
#         literature_grd = self.__literature_grd
#         birth_year = self.__birth_year
#         class_id = self.__class_id
#         return name,id,math_grd,history_grd,literature_grd,birth_year,class_id
#     def getName(self):
#         return self.__name
#     def getId(self):
#         return self.__id
#     def getBirth_year(self):
#         return self.__birth_year
#     def getClass_id(self):
#         return self.__class_id
#     def getMath_grd(self):
#         return self.__math_grad
#     def getHistory_grd(self):
#         return self.__history_grd
#     def getLiterature_grd(self):
#         return self.__literature_grd
#     def setName(self,name):
#         self.__name = name
#     def setId(self,id):
#         self.__id = id
#     def setBirth_year(self,birthday):
#        self.__birth_year = birthday
#     def setClass_id(self,class_id):
#         self.__class_id = class_id
#     def setMath_grd(self,math_grd):
#         self.__math_grad = math_grd
#     def setHistory_grd(self,history_grd):
#         self.__history_grd = history_grd
#     def setLiterature_grd(self,literature_grd):
#         self.__literature_grd = literature_grd
#     def age_Avg_grd(self):
#         x = date.today()
#         avg = (self.__math_grad+self.__history_grd+self.__literature_grd)/3
#         age = abs(x.year-self.__birth_year)
#         return age, round(avg,1)
#     def getDegree(self):
#         x = (self.__math_grad+self.__history_grd+self.__literature_grd)/3
#         det = self.__name,self.__id,self.__math_grad,self.__history_grd,self.__literature_grd
#         if x > 90:
#             print("name: ",det[0],"id: ",det[1],"math_grd: ",det[2],"history_grd: ",det[3],"literature_grd: ",det[4],"\nThe avg: ",round(x,1),"\ngraduated with distinction!")
#         elif x < 60:
#             print("name: ",det[0],"id: ",det[1],"math_grd: ",det[2],"history_grd: ",det[3],"literature_grd: ",det[4],"\nThe avg: ",round(x,1),"\nNot passed!!!")
#         else:
#             print("name: ",det[0],"id: ",det[1],"math_grd: ",det[2],"history_grd: ",det[3],"literature_grd: ",det[4],"\nThe avg: ",round(x,1),"\nGraduated!")
# student1 = Student('Eli',13052445,1990,10,95,75,100)
# student2 = Student('Daniel',23014955,1994,10,75,68,85)
# student3 = Student('Yaalem',33071234,1995,10,85,70,95)
# student4 = Student('solomon',42084954,1997,10,100,75,98)
# student5 = Student('ron',53021562,1979,2,35,35,55)
#  print(student1.age_Avg_grd())
#  print(student4.getDegree())