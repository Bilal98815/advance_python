n = 10
a = 1 if n < 10 else 2 if n > 10 else 0

print(a)

l1 = [1, 2, 3, 4, 5]
numbers  = [num for num in l1 if num % 2 == 0]
print(numbers)


result = n * 2 + 10 if n % 2 == 0 else n / 2 - 10
print(result)
