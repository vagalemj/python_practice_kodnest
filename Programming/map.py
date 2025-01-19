# map() is a built-in function in Python that applies a given function to each item of an iterable (such as a
# list, tuple, or string) and returns a list of the results.
# map() is a function that takes two arguments: a function and an iterable. It applies th
# e function to each item in the iterable and returns a map object which is an iterator.

# map(function, iterable_object) --> Iterator object

def double(x):
    return x * 2

li = [1, 2, 3, 4, 5]
d_li = map(double, li)
print(list(d_li))  # Output: [2, 4, 6, 8, 10]

tup = ('1', '2', '3', '4', '5')
print(tup)
c_tup = tuple(map(int, tup))
print(c_tup)

li2 = [1, 5, 55]
print(li2)
li2 = list(map(float, li2))
print(li2)