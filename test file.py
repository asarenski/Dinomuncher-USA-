class Stack(list):
    def push(self,object):
        self.append(object)

apple = Stack()
apple.push("monkey")
print apple

apple.pop()
print apple
'''
----------------------------------------------
'''

class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, list1):
        self.name = list1[0]
        self.age = list1[1]
        self.major = list1[2]

def make_student(object):
    student = Student(object)
    return student

stud_list = ('dave',13,'physics')
monkeyman = make_student(stud_list)
print stud_list
print monkeyman.name

'''
----------------------------------------------
'''

print type(1)
print type("monkey")