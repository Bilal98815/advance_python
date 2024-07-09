from functools import partial

# def simpleGeneratorFun(): 
#     yield 10            
   
# # Driver code to check above generator function 
# for value in simpleGeneratorFun():  
#     print(value)

# for i in range(10):
#     print(i)
#     i = i * 5
 
 
# def power(a, b):
#     print("A value: ", a)
#     print("B value: ", b)
#     return a ** b
 
 
# # partial functions
# pow2 = partial(power, b=2)
# pow4 = partial(power, b=4)
# power_of_5 = partial(power, 5)
 
# print(power(2, 3))
# print(pow2(4))
# print(pow4(3))
# print(power_of_5(2))

# print('Function used in partial function pow2:', pow2.func)
# print('Default keywords for pow2:', pow2.keywords)
# print('Default arguments for power_of_5:', power_of_5.args)

def myFun(*argv):
    for arg in argv:
        print(arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
