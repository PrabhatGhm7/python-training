from unicodedata import numeric


numbers =[1,2,3,4,5]
numbers.append(6)
print(numbers)
numbers.insert(0,0)
print(numbers)
print(3 in numbers)
numbers.remove(3)
print(numbers)
print(3 in numbers)
print(len(numbers))