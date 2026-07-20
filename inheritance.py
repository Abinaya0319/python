
# class father:
#     father = ""
# class mother:
#     mother = ""
# class son(father,mother):
#     pass
# parent = son()
# father = "Ram"
# mother = "Sita"
# print("father:",father,"mother:",mother)


# class Father:
#      father = "sakthivel"
# class Mother:
#      mother = "lakshmi"
# class sister:
#     sister = "gopika"
# class brother:
#     brother = "saravanan" 
# class Son(Father, Mother, sister,brother):

#     def display(self):
#      print("Father:", self.father)
#      print("Mother:", self.mother)
#      print("sister:",  self.sister)
#      print("brother:", self.brother)

# parent = Son()
# parent.display()




# class Parent:
#     def display(self):
#         print("This is Parent")

# class self(Parent):
#     def show_son(self):
#         print("This is Son")

# class Daughter(Parent):
#     def show_daughter(self):
#         print("This is Daughter")

# class parent():
      
#      def display(self):
#          print(" this is a parent")
#          return ()

# class child():
#         def self
#         print
#         return()

# def main_process():
#     print()
#     print()
#     print()
#     print()

# main_process()

# hierarchal inheritance

# class Parent:
#     name = "lakshmi"

# class Son(Parent):
#     pass

# class Daughter(Parent):
#     pass

# s = Son()
# d = Daughter()

# print("Son Parent Name:",s.name)
# print("Daughter Parent Name:",d.name)
    


#hierarchial inheritance

# class Parent:  
#     def show(self):
#         print("I am Parent")

# class Child1(Parent):
#     def display1(self):
#         print("son")
#         print("saravanan")
        
# class Child2(Parent):
#     def display2(self):
#         print("daughter")
#         print(" abinaya")

# obj1=Child1()
# obj1.show()
# obj1.display1()

# obj2 = Child2()
# obj2.show()
# obj2.display2()


# hybrid inheritance
# class vehicle():
#     def vehicle(self):
#         print("scooty")
# class Car(Vehicle):
#     def car(self):
#         print("Car")

# class Bike(Vehicle):
#     def bike(self):
#         print("Bike")

# class SportsCar(Car):
#     def sports(self):
#         print("sports car")

# obj =  SportsCar()
# obj.vehicle()
# obj.car()
# obj.sports()



# class cloud:
#     def cloud(self):
#         cloud = ""
# class s3(cloud):
#     def s3(self):
#         s3 =  ""
# class ec2(s3):
#     def ec2(self):
#         ec2 = ""
# class ami(s3,cloud):
#     def ami(self):
#         ami = ""
# a = ami()
# b = ec2()
# c = s3() 
# a.cloud = "Amazon Web Service"
# a.ami = "Amazon Machine Image"
# a.s3 ="Simple Storage Service"
# print(f"{a.ami} is derived from {a.cloud} and {a.s3}")
# b.ec2 = "Elastic Compute Cloud"
# print(f"{b.ec2} is derived from {a.s3}")
# print(f"{a.s3} is derived from {a.cloud}")