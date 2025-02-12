class Student():
    def study(self):
        print('study')
    def play():
        print('play')

s1 = Student()
s1.study()
s1.study = 'learning'
print(s1.study)
#s1.play() # Error: play() takes 0 positional arguments but 1 was given