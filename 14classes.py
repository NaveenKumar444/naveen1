# we use classes to defines new types
class Point:
    # this (constructor) method is used to create the object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)

#exercise
class Person:
   def __init__(self, name):
        self.name = name
   def talk(self):
        print(f"hi, i am {self.name}")

naveen = Person("naveen kumar")
bob = Person("nitish kumar")
naveen.talk()
bob.talk()




