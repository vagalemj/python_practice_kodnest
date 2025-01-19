li1 = [1, 2, 3, 4, 5]
print(li1)
sq_li = []
for i in li1:
    sq_li.append(i ** 2)
print(sq_li)


lis1 = [1, 2, 3, 4, 5]
dup_lis = [i for i in lis1]
print(dup_lis)
even = [i for i in lis1 if i % 2 == 0]
print(even)
sq_lis = [i ** 2 for i in lis1]
print(sq_li)
new_lis = [ele + 2  for ele in lis1]
print(new_lis)

lis2 = [10, 19, 30, 37, 50]
even_odd = ['even' if i % 2 == 0 else 'odd' for i in lis2]
print(even_odd)

new_li = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
li = [i for sublist in new_li for i in sublist]
print(li)