def printpattern1():
    for i in range(0,4):
        
        for j in range(0,i+1):
                print("*",end='')
        
        print("\r")
        
def printpattern2():
    for i in range(0,4):
        
        for j in range(0,4):
                print("*",end='')
        
        print("\r")
        
def printpattern3():
    for i in range(0,4):
        num=1
        for j in range(0,i+1):
            print(num,end='')
            num=num+1
        print("\r")   
        
def printpattern4():
    for i in range(1,5):
        #Repeatation Of ith String i no. of times 
        print(str(i)*i)
        
        print("\r")  


            
                     
            
print("Pattern 1")
print("\r")
printpattern1()
print("Pattern 2")
print("\r")
printpattern2()
print("Pattern 3")
print("\r")
printpattern3()
print("Pattern 4")
print("\r")
printpattern4()
