def decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print("Completed task")
    return wrapper
    
@decorator
def do_this():
    print('Doing the dishes')

@decorator
def do_that():
    print("Doing cleaning car windows")

do_this()
do_that()

# With decorators you pass a function into another one when you call them
