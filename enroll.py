import addStudent
import removeStudent

print("Hello and welcome to my python enrollment script")

while True:
    print("What would you like to do?\n1) Add a student\n2) Remove a student\n3) exit program")
    choice = input()
    if choice == 1:
        addStudent
    elif choice == 2:
        removeStudent
    elif choice == 3:
        break
    else:
        print("error: please select a real number listed in choices above!")

