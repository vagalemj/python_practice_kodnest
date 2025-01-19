li = [10, 5, 3, 20]
li.sort()
print(li) # [3, 5, 10, 20]

li.sort(reverse=True)
print(li) # [20, 10, 5, 3]

li2 = [100, 30, 500, 10]
s_li2 = sorted(li2)
print(s_li2) # [10, 30, 100, 500]
print(li2) # [100, 30, 500, 10]