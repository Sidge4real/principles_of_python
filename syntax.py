# python doesn't use [let, var or const]

a = 5
a = "Radom string"

print(a) 
# output: Random string


# array:
a = [5,"H1",'a',True]
b = [9,9,3]
c = ["hi","goodmorning"]
d = [False,True,False]

print(a)

for x in a :
    print(x)

# add data:
a.append("added!")
print(a)

d.append(False)
print(d)

# functions:
def add(a,b) :
    return a+b

def calc(a, b=None, c=None, d=None):
    if c is None and d is None:
        return a + b
    elif c is None:
        return a + b + d
    elif d is None :
        return a + b + c  
    else : return a 

print("result: " , add(9,9))


