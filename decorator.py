#Advance Function
'''Decorator:-A Fuction that modifies other function without changing it's original code'''
#Creating decorator function
def my_dec(func):
    def wrapper():
        print("Enter login details")
        func()
        print("Successfully logined")
    return wrapper
#main function with decorator
@my_dec
def say_hello():
    print("Hello")
#Calling main function with dacorator
say_hello()


