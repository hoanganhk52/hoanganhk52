from turtle import*


##I. Study
##A list within another list is said to be nested
##  example: nested = ["hello", 2.0, 5, [10, 20]]
##A list can store both integers and strings in it
##  example: abc=[1,"a",2,"b"]
##exercise1:
##     if start < stop and step <0, the list is emperty
##        rule for relationship:
##            case1:start<stop, step>0
##            for i in range(stop-start):
##                if start< stop:
##                    start = start+step
##            case2:start>stop, step<0
##                for i in range(start-stop):
##                    if start> stop:
##                        start = start+step

##exercise 2:
##    When I type:"alex is tess", I get "True" value. That means two name refer to the same object
##    So that this fragment creates one turtle instance, setting the color of alex
##    also change the color of tess

##II. turtle exercises                
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
##bai 1: 
##for n in range(3,8):       
##    color(colors[n-3])
##    for i in range(n):        
##        forward(100)
##        left(360/n)

##bai 2:
##for j in range(5):
##    color(colors[j])
##    begin_fill()
##    for i in range(2):
##        forward(50)
##        left(90)
##        forward(100)
##        left(90)    
##    end_fill()
##    forward(50)

##III. Serious exercises
##bai 1:
##clothes = ["T-Shirt","Sweater"]
##choice = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()
##choices= ["C","R","U","D"]
##while choice in choices:
##    if choice=="C":
##        new_cloth = input("Enter new item: ")
##        clothes.append(new_cloth)
##        print("Our items: ",end="")
##        for cloth in clothes:
##            print(cloth,",",end="")
##        print()
##        choice = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()
##    elif choice=="R":
##        print("Our items: ",end="")
##        for cloth in clothes:
##            print(cloth,",",end="")
##        print()
##        choice = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()
##    elif choice=="U":
##        a=int(input("Update position? "))
##        b=input("new item? ")
##        clothes[a]=b
##        print("Our items: ",end="")
##        for cloth in clothes:
##            print(cloth,",",end="")
##        print()
##        choice = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()
##    else:    
##        a=int(input("Delete position? "))
##        del clothes[a]
##        print("Our items: ",end="")
##        for cloth in clothes:
##            print(cloth,",",end="")
##        print()
##        choice = input("Welcome to our shop, what do you want (C, R, U, D)?").upper()

##bai 2:
size=[5,7,300,90,24,50,75]

print("Hello, my name is Hoang Anh and these are my ship sizes:")
print(size)
print()
max_size=max(size)
max_index=size.index(max(size))
print("Now my biggest sheep has size ",max_size," let's shear it")
size[max_index]=8
print("After shearing, here is my flock")
print(size)
print()
n=3
for i in range(1,n):        
    print("MONTH ",i," :")
    print("One month passed, now here is my flock")
    for j in range(len(size)):
        size[j-1] = size[j-1]+50
    print(size)
    print("Now my biggest sheep has size ",max(size)," let's shear it")
    size[size.index(max(size))]=8
    print("After shearing, here is my flock")
    print(size)
    print()
for j in range(len(size)):
        size[j-1] = size[j-1]+50
print("One month passed, now here is my flock")
print(size)
money = sum(size)
print ("My flock has size in total", money)
print('I would get',money,'* $2 = ',money*2,"$")
    

    
    

     


