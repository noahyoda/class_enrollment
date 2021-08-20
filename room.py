class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


def addStudent(room):
    # room is the list of students we passed in we passed in
    print("What is the students name: ")
    stuName = input()
    print("What is the students grade level (numarical): ")
    stuGrade = input()
    newStu = student(stuName, stuGrade)
    room.append(newStu)


def removeStudent(room):
    print("What is the students name you want to remove: ")
    stuName = input()
    oldStudent = contains(room, stuName)
    if oldStudent != False:
        room.remove(oldStudent)
        print(oldStudent.name + " was removed!\n")
    else:
        print("Error, student does not exist yet")


def listStudents(list):
    for student in list:
        text = student.name + "\t" + student.grade
        print(text)

def contains(list, name):
    for student in list:
        if student.name == name:
            return student
    return False
