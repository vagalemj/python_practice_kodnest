li1 = list('Kod')
print(li1)

li2 = list((10, 20))
print(li2)  

li3 = list({100, 200})
print(li3)

li4 = list({'name':'madhu', 'age':25})
print(li4)

li5 = list(range(1,11))
print(li5)

tup1 = tuple([10, 20, 30, 40])
tup2 = tuple({100, 200, 300})
tup3 = tuple({'name':'madhu', 'age':25})
tup4 = tuple(range(1, 11))
tup5 = tuple('KodNest')
print(tup1) # (10, 20, 30, 40)
print(tup2) # (100, 200, 300)
print(tup3) # ('name','age')
print(tup4) 
print(tup5)


s1 = set([10, 20, 30, 30])
s2 = set({100, 200, 300, 300})
s3 = set({'name':'madhu', 'age':25})
s4 = set(range(1, 11))
s5 = set('KodNest')
print(s1) # {10, 20, 30}
print(s2) # {100, 200, 300}
print(s3) # {'name','age'}
print(s4) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s5) # {'K', 'o', 'd', 'N', 'e', 's', 't'}

d1 = dict([['name', 'madhu'],['age', 25]]) # type: ignore
print(d1)