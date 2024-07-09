try: 
	raise NameError("Hi there")
except NameError:
	print ("An exception")
	

# 4 keywords: (try, except, else, finally)
# else is executed if try is executed without any exception
# finally is always exceuted no matter what there is exception or not



# ---------->>>>>> CUSTOM EXCEPTION HANDLING <<<<<<<----------


# define Python user-defined exceptions
class InvalidAgeException(Exception):
    pass

# RunTimeError class is a standard exception that is raised when error does not fall into any category
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.msg = arg




# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")



try:
    raise Networkerror("Error")
 
except Networkerror as e:
    print(e.msg)
