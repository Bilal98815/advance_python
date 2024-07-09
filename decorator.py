import time
import math


# ---->>>>> First Class Objects <<<<<<-----

# In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
# Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …

# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello'))


# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

greet(shout) 
greet(whisper) 



# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

add_15 = create_adder(15) 

print(add_15(10))



# --------->>>>>>>> DECORATORS <<<<<<<<----------


# A decorator is a higher-order function that takes another function as an argument,
# adds some functionality, and returns a new function.
# It allows modifying or extending behavior of functions or methods


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)



def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))



# ----------->>>>>>>> Chaining Decorators <<<<<<<<<-----------
# In simpler terms chaining decorators means decorating a function with multiple decorators

# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())
