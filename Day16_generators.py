'''Generator:
->this generator is a special function that returns interator,
instead of returning all the values at once.
--> Here we are gonna use 'yield' keyword
--> Laxy evolution'''
def some():
    yield 1
    yield 2
    yield 3
    yield 4
so=some()
print(next(so))
print(next(so))
print(next(so))
print(next(so))

'''working of generator
--> when the function is called, it doesnot execute the function immediately..
--> it will return the genartor object.
--> Then the functionwill pauses at each yield
--> When the next() is called again,execution resumes from where it stopped '''
def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3
samp=demo()
print(next(samp))
print(next(samp))
print(next(samp)) 

def how(so):
    for i in range(so):
        yield i*i
any_=how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_)) 

#without generator
def Sqrt(so):
    for i in range(so):
        print(i*i)
Sqrt(5)

'''Function:                                            Generator:
-->return                                    |   -->yield
-->return complte result                     |   -->return one value at once
-->function will end after return the values |   -->pauses after each yield
-->more memory usage                         |   -->less memory usage
-->This function never resume                |   -->resume after next()
 
yield keyword:
--> this will produces the valu
-->but the yield pauses the function
-->and yield will save the functions current state
-->yield will continues where it stopped.

next() :
-->next() function is used to retrive the next value from a generator

StopIteration Error:
-->Calling next() function after all values retrieved then it will raises this error'''
def how(so):
    for i in range(so):
        if i==3:
            break
        yield i*i
any_=how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

def how(so):
    for i in range(so):
        if i==3:
            continue
        yield i*i
any_=how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


def some(a):
    for i in range(a):
        yield i
any_=some(10)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

'''Generator Expression:
-->the generator expression is similar to a list comprehension but uses () instead of []
'''
gen=(x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



















































