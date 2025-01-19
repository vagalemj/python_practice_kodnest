# Strings are immutable in Python
# if we try to modify the string, it will create a new string object in memory
# if new string doesnt not have any reference variable it will be garbage collected
# Python uses internally string interning to optimize memory usage
# String interning is a process of checking string intern pool before creating a new string object
# when ever we want to create new object, python first checks the string intern pool weather the object is already present or not
# when the object is already exist in the string intern records then address of existing object will be reused

s1 = 'kodnest'
s = s1.upper()
print(s)

s2 = 10
print(s2, id(s2))

s3 = 'Hello'
s4 = 'World'
print(s3, id(s3))
print(s4, id(s4))

print('s3 ID of H',id(s3[0]))
print('s3 ID of o',id(s3[-1]))

print('s4 ID of W',id(s4[0]))
print('s4 ID of l',id(s4[2]))