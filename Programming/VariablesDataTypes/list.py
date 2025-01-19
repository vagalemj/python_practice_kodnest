li1 = [10, 11.5, True, 'KodNest'] # type: ignore
print(li1, type(li1)) # type: ignore

fruits = ['apple','apple', 'apple', 'banana', 'cherry', 'date']
print(fruits, type(fruits))
# Output: ['apple', 'apple', 'apple', 'banana', 'cherry', 'date']

fruits.append('peach')
print(fruits)
# Output: ['apple', 'apple', 'apple', 'banana', 'cherry', 'date', 'peach']

print(fruits.index('banana'))
# Output: 3

fruits.pop()
print(fruits)
# Output: ['apple', 'apple', 'apple', 'date']

fruits.insert(2,'mango')
print(fruits)
# Output: ['apple', 'apple', 'mango', 'apple', 'date']

fruits.remove('apple')
print(fruits)
# Output: ['peach', 'mango', 'apple', 'apple', 'date']

fruits.extend('pineapple')
print(fruits)
# Output: ['peach', 'mango', 'apple', 'apple', 'date']

del fruits[0]
print(fruits)
# Output: ['mango', 'apple', 'apple', 'date']

for i in fruits:
    print(i, " ", end='')
# Output: peach  mango  apple  apple  date  apple

print()
animals = ['dog', 'cat', 'bird']
for i in animals: 
    print(i, end=' ')
# Output: dog cat bird

