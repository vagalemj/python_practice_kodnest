def mutation(string, position, character):
    li = string(li)
    li[position] = character
    string = ''.join(li)
    return res

s = input()
p, c = input().split()
res = mutation(s, int(p), c)
print(res)