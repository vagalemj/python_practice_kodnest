li = []

n = int(input('Enter the number of students: '))
for i in range(n):
    name = input('Enter the name of the student: ')
    score = float(input('Enter the score of the student: '))
    li.append([name, float(score)])
print(li)

scores = []
for name, score in li:
    scores.append(score)
scores = list(set(scores))
scores.sort()
print(scores)

name_li = []
second_small_score = scores[1]
for name, score in li:
    if score == second_small_score:
        name_li.append(name)
name_li.sort()  

for name in name_li:
    print(name)