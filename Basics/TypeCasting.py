# Typecasting is the process of converting one data type to another data type.

# if we want to convert one data type to another data type, we can use typecasting
a = '20'
print(a, type(a))
b = int(a)
print(b, type(b))

# str to integer conversion is not possible if the string contains any character other than digits
x = 'Code'
print(x, type(x))
# y = int(x)
# print(y, type(y))

z = float(input("Enter a number: "))
print(z, type(z))

# bool() function is used to convert any data type to boolean
q = 12
print(q, type(q))
q = bool(q)
print(q, type(q))

'''
1. While converting int to bool for all non zero values we will get True
2. While converting int to bool for 0 and empty string we will get False    
'''