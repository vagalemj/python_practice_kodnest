t1 = (10, 22.5, True, 'KodNest') 
print(t1)

#t1.append(400)  # type: ignore
print(t1) 

t2 = (10, 20, 30)
t3 = (40, 50, 60)
t4 = t2 + t3
print(t4)

tup = (10,)
print(tup, type(tup))

new_tup = (10, 20, 30, 40)
ele1,ele2,ele3,ele3 = new_tup
print('Value of ele1:',ele1)
print('Value of ele2:',ele2)
print('Value of ele3:',ele3)
print('Value of ele4:',ele3)