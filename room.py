class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


def addStudent(room):
    #room is the list of students we passed in we passed in
    print("What is the students name: ")
    stuName = input()
    print("What is the students grade level (numarical): ")
    stuGrade = input()
    newStu = student(stuName, stuGrade)
    room.append(newStu)

def removeStudent(room):
    room.remove(name)
