def export(filename, list):
    file = open(filename, "w")
    for stu in list:
        file.write(stu.name + "\t" + stu.grade)
    file.close
