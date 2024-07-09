# Importing the StringIO module.
from io import StringIO


# The arbitrary string.
string ='This is initial string.'

# Using the StringIO method to set
# as file object. Now we have an 
# object file that we will able to
# treat just like a file.
file = StringIO(string)

# this will read the file 
print(file.read())

# We can also write this file.
file.write(" Welcome to geeksforgeeks.")

# This will make the cursor at 
# index 0.
file.seek(0)

# This will print the file after 
# writing in the initial string.
print('The string after writing is:', file.read()) 

# Retrieve the entire content of the file.
print(file.getvalue())

# This will returns whether the file
# is interactive or not.
print("Is the file stream interactive?", file.isatty()) 
 
# This will returns whether the file is
# readable or not.
print("Is the file stream readable?", file.readable())
 
# This will returns whether the file supports 
# writing or not.
print("Is the file stream writable?", file.writable())
 
# This will returns whether the file is
# seekable or not.
print("Is the file stream seekable?", file.seekable())
 
# This will returns whether the file is 
# closed or not.
print("Is the file closed?", file.closed)

# To set the cursor at 0.
file.seek(0) 
 
 
# This will drop the file after 
# index 18.
file.truncate(18)

# Print the index of cursor
print(file.tell())

# Closing the file.
file.close() 
 
# If we now perform any operation on the file 
# it will raise an ValueError.
 
# This is to know whether the
# file is closed or not.
print("Is the file closed?", file.closed)
