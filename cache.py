from functools import cache

@cache #cache will check previous num input so when same input it will get to prev. value back 
def increment(num):
    print("Running 1000 lines of code") #if there was so much code it will take so long to run..
    return num+1

print(increment(1))
print(increment(2))
print(increment(8))
print(increment(1))




