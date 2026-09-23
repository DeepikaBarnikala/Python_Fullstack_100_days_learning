'''
Polymorphism--> Method Overloading, Method overriding, Operator Overloading
Method overloading--> Default arguments, variable length arguments, Type of an argument

#method overloading(complie time Ploymorphism) --> Default arguments

class Hotstar:
    """default args usage"""
    def watch(self,movie=None):
        self.movie=movie
        if self.movie==None:
            print(f'Welcome to Hotstar')
        elif self.movie==movie:
            print(f'User watching {self.movie}')
u1=Hotstar()
#u1.watch() #in this case we made movie as default
u1.watch("Saaho")

#variable length arguments

class Prime:
    """Default args"""
    def watch(self,movie=None):
        print(f'Welcome to Prime')
    """ *args usage"""
    def watchList(self,*movie):
        self.movie=movie
        print("your watchList movies...Give it a look and happy weekend")
        for m in movie:
            print(m)
ur1=Prime()
#ur1.watchList() #in this case we made movie as default
ur1.watchList("Saaho","Billa","Kalki","Bhahubali")
ur1.watch()


#Method Overloading with type of arguments(isintance())
#Hotstar--->one movie, multiple movies
class Hotstar:
    """usage of type of args"""
    def watch(self,movie=None):
        print(f'welcome to Hotstar')
    def movie_list(self,content):
        self.content=content
        if isinstance(content,str):
            print(f'user watching {self.content}')
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)
u1=Hotstar()
u1.watch()
u2=Hotstar()
u2.movie_list("Billa")
u2.movie_list(["Narnia","Harry Potter","Leo"])
print(u2.movie_list(("Narnia","Harry Potter","Leo"))) #it returns none cz tuple is not defined


#method overriding --> Inheritance usage
#when the same method name is used in base class and also in derived class
#super()

#free user-->[can watch free content with advertisements]
#premium user --> [can watch premium content without advertisements]
#VIP user-->[can watch premium content along with devices count,streaming]

class Hotstar:
    """Base class"""
    """Multi level inheritance"""
    """method Overriding with example of Hostar"""
    def watch(self):
       print(f'welcome to Hotstar')
class FreeUser(Hotstar):
    def watch(self):
        super().watch()
        print(f'Can watch free content with advertisement')
class PremiumUser(FreeUser):
    def watch(self):
        super().watch()
        print(f'can watch premium content without advertisement')
class VIPUsers(PremiumUser):
    def watch(self):
        super().watch()
        print(f'can watch premium content along with devices count,streaming')
u1=Hotstar()
u2=FreeUser()
u3=PremiumUser()
u4=VIPUsers()

u2.watch()
u3.watch()
u4.watch()


#operator OverLoading --> (Magic methods/dunder methods) __init__(),__add__ etc

a =13;b=24
print(a+b)
print(a.__le__(b))
print(a.__add__(b))
print('codegnan '.__add__('python'))
print([1,2,].__add__([3,4,5]))

#in above case same _add_() is performing different cases (Addition,concatenation,merging)

a = [1,2,3,4]
print(a.__len__())
'''

#now linking above operators scenario to Hotstar

class WatchHistory:
    """Duration of watching content"""
    def duration(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        print(f'User watching {self.hours} hours duration')
u1 = WatchHistory()
u1.duration(25)
u2 = WatchHistory()
u2.duration(35)
#get the complete duration
print(u1+u2)
u1.__str__()
u2.__str__()
print(u1.hours + u2.hours)


























