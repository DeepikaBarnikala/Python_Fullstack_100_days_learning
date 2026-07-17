'''
-->What is Inheritance?
Inheritance is a way to reuse code.
You create a parent class (base class) with common features.
Then you create a child class (derived class) that automatically gets those features and can add its own.
It’s like a child inheriting traits from parents but also having unique qualities.

-->Why Use Inheritance?
Avoids repeating code (DRY principle: Don’t Repeat Yourself).
Makes programs easier to maintain.
Helps organize related classes logically.

types of Inheritences... '''

#1.Single Inheritance: A child class inherit from one parent is single inheritance.

class animal:
    def sound(self):
        print("Animal make sounds")
class dog(animal):
    def barks(self):
        print("Dog barks")
d=dog()
d.sound()
d.barks()


class father:
    def land(self):
        print("5 Acrs of land")
class son(father):
    def flat(self):
        print("3BHK flat")
s=son()
s.land()
s.flat()

#2.Multiple Inheritance: Child inherit from more than one parent.

class Father:
    def skill(self):
        print("Driving")

class Mother:
    def talents(self):
        print("Cooking")

class Child(Father, Mother):
    def mySkills(self):
        print("Coding")

c = Child()
c.skill()
c.talents()
c.mySkills()

#3. Multi-level Inheritance: Chain of Inheritance
class Grandparent:
    def house(self):
        print("Big house")

class Parent(Grandparent):
    def car(self):
        print("Family car")

class Child(Parent):
    def bike(self):
        print("Sports bike")

obj = Child()
obj.house()   # From Grandparent
obj.car()     # From Parent
obj.bike()    # From Child 

#4.Hierarchical: One parent → multiple children

class mother:
    def gold(self):
        print('10 kgs gold')
class priya(mother):
    def show(self):
        print("Will get 5kgs of gold")

class deepu(mother):
    def show_2(self):
        print('Will get remaining 5 Kgs of gold')

child1=priya()
child2=deepu()

child1.gold()
child1.show()

child2.gold()
child2.show_2

# Base class
class LivingBeing:
    def breathe(self):
        print("Breathing...")

# Level 1 child
class Animal(LivingBeing):
    def move(self):
        print("Animals can move")

# Level 2 child
class Mammal(Animal):
    def feed_milk(self):
        print("Mammals feed milk")

# Level 3 child
class Dog(Mammal):
    def sound(self):
        print("Woof Woof!")

# Using hierarchy
d = Dog()
d.breathe()    # From LivingBeing
d.move()       # From Animal
d.feed_milk()  # From Mammal
d.sound()      # From Dog


#5.Hybrid Inheritance: Combination of 2 or more diff inheritances
class A:
    def methodA(self):
        print('Class A')
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')
class D(B,C):
    def methodD(self):
        print('Class D')

so=D()
so.methodA()
so.methodB()
so.methodC()
so.methodD() 

#super(): this function is used to access the parent class methods or constructor in the child class..

class parent:
    def show(self):
        print("Parent method")
class child(parent):
    def show(self):
        super().show()
        print("Child Method")
c=child()
c.show() 

#contrcutor usage in OOPs
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)

s=student('Deepika',124)
s.display()












































































































