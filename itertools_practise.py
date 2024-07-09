from itertools import combinations, accumulate, chain, compress, dropwhile, takewhile, filterfalse, islice, starmap, tee, zip_longest
import operator


# print ("All the combination of list in sorted order(without replacement) is:")  
# print(list(combinations(['AB', 2, 3], 2))) 
# print() 
   
# print ("All the combination of string in sorted order(without replacement) is:") 
# print(list(combinations('ABC', 3))) 
# print() 
   
# print ("All the combination of list in sorted order(without replacement) is:") 
# print(list(combinations(range(2), 1)))



li1 = [1, 4, 5, 7]
li2 = [1, 6, 5, 9]
li3 = [8, 10, 5, 4]
 
# using accumulate()
# prints the successive summation of elements
# print("The sum after each iteration is : ", end="")
# print(list(accumulate(li1)))
 
# # using accumulate()
# # prints the successive multiplication of elements
# print("The product after each iteration is : ", end="")
# print(list(accumulate(li1, operator.mul)))

# print("All values in mentioned chain are : ", end="")
# print(list(chain(li1, li2, li3)))


# using chain.from_iterable() to print all elements of lists 
# print ("All values in mentioned chain are : ", end ="") 
# print (list(chain.from_iterable([li1, li2, li3])))


# using compress() selectively print data values
# print("The compressed values in string are : ", end="")
# print(list(compress('Bilal', [
#       1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))


# using dropwhile() to start displaying after condition is false
# print ("The values after condition returns false : ", end ="") 
# print (list(dropwhile(lambda x : x % 2 == 0, li1)))


# using filterfalse() to print false values 
# print ("The values that return false to function are : ", end ="") 
# print (list(filterfalse(lambda x : x % 2 == 0, li1)))


li = [2, 4, 5, 7, 8, 10, 20]
t1 = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)] 
     
# using islice() to slice the list acc. to nee# print ("All the combination of list in sorted order(without replacement) is:")  
# print(list(combinations(['AB', 2, 3], 2))) 
# print() 
   
# print ("All the combination of string in sorted order(without replacement) is:") 
# print(list(combinations('ABC', 3))) 
# print() 
   
# print ("All the combination of list in sorted order(without replacement) is:") 
# print(list(combinations(range(2), 1)))



li1 = [1, 4, 5, 7]
li2 = [1, 6, 5, 9]
li3 = [8, 10, 5, 4]
 
# using accumulate()
# prints the successive summation of elements
# print("The sum after each iteration is : ", end="")
# print(list(accumulate(li1)))
 
# # using accumulate()
# # prints the successive multiplication of elements
# print("The product after each iteration is : ", end="")
# print(list(accumulate(li1, operator.mul)))

# print("All values in mentioned chain are : ", end="")
# print(list(chain(li1, li2, li3)))


# using chain.from_iterable() to print all elements of lists 
# print ("All values in mentioned chain are : ", end ="") 
# print (list(chain.from_iterable([li1, li2, li3])))


# using compress() selectively print data values
# print("The compressed values in string are : ", end="")
# print(list(compress('Bilal', [
#       1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))


# using dropwhile() to start displaying after condition is false
# print ("The values after condition returns false : ", end ="") 
# print (list(dropwhile(lambda x : x % 2 == 0, li1)))


# using filterfalse() to print false values 
# print ("The values that return false to function are : ", end ="") 
# print (list(filterfalse(lambda x : x % 2 == 0, li1)))


li = [2, 4, 5, 7, 8, 10, 20]
t1 = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)] 
     
# using islice() to slice the list acc. to need 
# starts printing from 2nd index till 6th skipping 2 
# print ("The sliced list values are : ", end ="") 
# print (list(islice(li, 2, 6, 3)))


# using starmap() for selection value acc. to function 
# selects min of all tuple values 
# print ("The values acc. to function are : ", end ="") 
# print (list(starmap(min, t1)))

# using takewhile() to print values till condition is false. 
# print ("The list values till 1st false value are : ", end ="") 
# print (list(takewhile(lambda x : x % 2 == 0, li )))


# iti = iter(li)
 
# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
# it = tee(iti, 3)
 
# printing the values of iterators
# print("The iterators are : ")
# for i in range(0, 3):
#     for j in list(it[i]):
#         print(j)
#     print("   ")


# using starmap() for selection value acc. to function 
# selects min of all tuple values 
# print ("The values acc. to function are : ", end ="") 
# print (list(starmap(min, t1)))

# using takewhile() to print values till condition is false. 
# print ("The list values till 1st false value are : ", end ="") 
# print (list(takewhile(lambda x : x % 2 == 0, li )))


# iti = iter(li)
 
# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
# it = tee(iti, 3)
 
# printing the values of iterators
# print("The iterators are : ")
# for i in range(0, 3):
#     for j in list(it[i]):
#         print(j)
#     print("   ")


# using zip_longest() to combine two iterables.
print("The combined values of iterables is  : ")
print(*(zip_longest('GesoGes', 'ekfrekute', fillvalue='_')))