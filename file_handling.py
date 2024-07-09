import os


# --------->>>>>> Reading File <<<<<<---------

# file = open('python.txt', 'r')

# example 1 of reading file
# for each in file:
#     print(each)

# example 2 of reading file
# print(file.read())


# example 3 of reading file
# with open('python.txt') as file2:
#     data = file2.read()
# print(data)


# reading certain characters
# print(file.read(3))


# Python code to illustrate split() function
# with open("python.txt", "r") as file3:
#     data = file3.readlines()
#     for line in data:
#         word = line.split()
#         print (word)



# ---------->>>>>>> Writting File <<<<<<<---------

# writeFile = open("python1.txt", "w")
# writeFile.write("This is the write command")
# writeFile.write("It allows us to write in a particular file")
# writeFile.close()

# we can also write with with statement
# with open("python1.txt", "w") as f: 
#     f.write("Hello World!!!") 



# --------->>>>>> Appending Mode <<<<<<--------

# appendFile = open("python1.txt", "a")
# appendFile.write("This will add this line")
# appendFile.close()




# create file function
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello World!\n')
        print("File " + filename + " created successfully")
    except IOError:
        print("Error: could not create file "+ filename)


# read file function
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)


# append to file function
def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


# rename file function
def rename_file(filename, newName):
    try:
        os.rename(filename, newName)
        print("File " + filename + " renamed to " + newName + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)


# delete file function
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)





filename = "example.txt"
new_filename = "new_example.txt"

create_file(filename)
read_file(filename)
append_file(filename, "This is some additional text.\n")
read_file(filename)
rename_file(filename, new_filename)
read_file(new_filename)
delete_file(new_filename)
