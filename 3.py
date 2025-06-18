#Print first 10 odd and even numbers using iterators and compress. You can use duck typing.

from itertools import compress

numbers = list(range(1,21))

even_selector = [num % 2 == 0 for num in numbers]
odd_selector = [num % 2 != 0 for num in numbers]

even = list(compress(numbers,even_selector))
odd = list(compress(numbers,odd_selector))

#duck typing - any iterable can be passed

def print_iterable(it):
     for i in it:
          print(i)

print("First 10 even numbers : ")
print_iterable(even)

print("First 10 odd numbers : ")
print_iterable(odd)
