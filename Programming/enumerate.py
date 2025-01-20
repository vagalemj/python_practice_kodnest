li = [10, 20, 30]
for idx, ele in enumerate(li):
    print(idx, ele)

# print all even index from list

for idx, ele in enumerate(li, start=1):
    if idx % 2 == 0:
        print(ele)