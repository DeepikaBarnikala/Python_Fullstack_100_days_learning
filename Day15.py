#removing duplicates
nums=[23,4,6,7,5,4,6,3,23,7,7]
empty_=[]
def removes(nums,empty_):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
        #print(j)
        print(empty_)
removes(nums,empty_) 


#prime or not
prime=int(input())
count=0
def not_prime(prime,count):
    for i in range(1,prime+1):
        if prime%i==0:
            count+=1
    if count==2:
        print("prime num")
    else:
        print("Not a prime")
not_prime(prime,count)


#counting words in the given string
def counting(txt,count):
    so=txt.split(' ')
    for j in so:
        count+=1
    print(count)
counting(txt,count)


#counting upper and lower letters and spaces in a txt
txt=input("Enter a txt:")
capCount=0
smallCount=0
spaceCount=0
def checking(txt,capCount,smallCount,spaceCount):
    for j in txt:
        if j.isupper():
            capCount+=1
        elif j.islower():
            smallCount+=1
        else:
            spaceCount+=1
    print(capCount)
    print(smallCount)
    print(spaceCount)
        
checking(txt,capCount,smallCount,spaceCount)
