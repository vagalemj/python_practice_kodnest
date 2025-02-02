print(bool('KodNest')) # True
#print(int('Kod')) # ValueError: invalid literal for int() with base 10: 'Kod'
print(int('11')) #11
#print(float('KodNest')) # Traceback (most recent call last):
print(float('12.54')) #12.54
print(bool('')) #False
print(bool(0)) #False
print(bool(12)) #True
#print(int('12.54')) # Traceback (most recent call last):
print(int(12.43)) # Traceback (most recent call last):

# Taking float input from user and converting it to int
value = int(float(input("Enter a float: ")))
print(value, type(value))