'''
*args and **kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.
Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly:

The *args parameter allows a function to accept any number of positional arguments.
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

*args -> tuples
**kwargs -> Dicionary
'''

#*args in function
def function1(*args):
    print(args)
    print(type(args))

function1(1,2,3,4,5)

#**kwargs in function
def function2(**kwargs):
    print(kwargs)
    print(type(kwargs))

function2(Fname = "John",Lname = "Doe")

def function3(**details):
    print(details)
    for key,value in details.items():
        print(key ,":", value)

function3(Fname = "Jane", Lname="Doe")