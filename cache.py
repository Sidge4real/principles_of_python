from functools import cache

@cache #cache will check previous num input so when same input it will get to prev. value back 
def increment(num):
    print("Running 1000 lines of code") #if there was so much code it will take so long to run..
    return num+1

print(increment(1))
print(increment(2))
print(increment(8))
print(increment(1))




# windows search: advanced system settings
    # > environment variables
    # > ad: 
            # > C:\Users\[pc_user_name]\AppData\Local\Programs\Python\Python311\python //python
            # > C:\Users\[pc_user_name]\AppData\Local\Programs\Python\Python311\Scripts //pip install (for libraries)

            # add those lines in path
                # > click on path and then edit
                # > click on new and add one of those lines and then repeat for the other one!