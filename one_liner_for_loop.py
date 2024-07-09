# common for loop:
for i in range(10):
    print(i)

# one liner for loop:
for i in range(10): print(i)

for i in range(10):
    if i<5:
        j = i**2
    else:
        j = 0    
    print(j)

# same code with one liner approach:
for i in range(10): print(i**2 if i<5 else 0)


# ---------->>>>>>> LIST COMPRESIONS <<<<<<<---------

squares = []

for i in range(10):
    squares.append(i**2)
    
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# list compression one liner
print([i**2 for i in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


for i in range(10):
    if i%2==0:
        squares.append(i**2)
    
print(squares)
# [0, 4, 16, 36, 64]


print([i**2 for i in range(10) if i%2==0])
# [0, 4, 16, 36, 64]


# nested loop
for i in range(3):
    for j in range(3):
        print((i,j))


# one liner nested for loop
print([(i,j) for i in range(3) for j in range(3)])

# palindromre python one liner
phrase = "ABCBACV"
print(phrase.find(phrase[::-1]))


# List
lst = [1, 2, 3, 'Alice', 'Alice']
# One-Liner
indices = [i for i in range(len(lst)) if lst[i]=='Alice']
# Result
print(indices)
# [3, 4]


matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

# Generate transpose 
trans = [[i[j] for i in matrix] for j in range(len(matrix[0]))]
print(trans)