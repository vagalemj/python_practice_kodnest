'''
1. In set we can store Homogeneous as well as Heterogeneous data types.
2. Set is an unordered collection of unique elements.
3. Set does not support indexing of data
4. Set does not support duplicate values
5. Set is mutable i.e. it can be changed after creation
'''

s1 = {10, True, 'Madhu', 15.5} # type: ignore
print(s1, type(s1))  # type: ignore # Output: (10, True, 'Madhu', 15.5)

s1.add(500) # type: ignore
print(s1) # type: ignore
# Output: (10, True, 'Madhu', 15.5, 500)

s1.remove(500) # type: ignore
print(s1) # type: ignore
# Output: (10, True, 'Madhu', 15.5)

p_ele = s1.pop() # type: ignore
print(p_ele) # type: ignore
# Output: 15.5

