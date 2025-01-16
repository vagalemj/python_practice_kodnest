'''
1. In dictionary we cannot have duplicate keys but in list we can have duplicate values.
2. In dictionary we can have only immutable data types as keys but in list we can have any
data type as an element.
3. In dictionary we can access the elements by their keys but in list we can access the elements
by their index.
4. In dictionary we can perform operations like union, intersection, difference etc. but in list w
e can perform operations like append, insert, remove etc.
5. In dictionary we can have a fixed number of elements but in list we can have a variabl
e number of elements.
6. In dictionary we can have a key-value pair but in list we can have only elements.
'''

dict = {'name' : 'Madhusudhan', 'age' : 27, 'phone' : 48733} # type: ignore
print(dict['name']) 
print(dict, type(dict)) 

dict['name'] = 'Madhu' 
print(dict) 

for i in dict.keys():
    print(i)

for j in dict.values(): 
    print(j) 

for k in dict.items(): 
    print(k) 

