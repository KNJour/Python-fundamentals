# fullList = {'Student': 'John', 'Course': 'Math', 'Grade': '88'}

# studentNum = input('How Many Students Do You Have?')

def studentInput():
    studentNum = input('How Many Students Do You Have?')
    studentList = []
    studentStr = ""
    for i in range(0, int(studentNum)):
        x = ""
        y = ""
        z = ""
        student = {}
        while x == "":
            x = input("Student Name:")
            if x == "":
                print("Name required, try again")
        # while isinstance(y, int) == False:
            y = input("Student Grade")
            # if isinstance(y, int) == False:
            #     print("Must be a numeric number")
        while z != "1" or z != "2" or z != "3":
            z = input("Select a course 1 - MATH, 2 - SCIENCE, 3 - HISTORY")
            if z != "1" or z != "2" or z != "3":
                print("Must be 1 - 3")
        if z == "1":
            z = "MATH"
        elif z == "2":
            z = "SCIENCE"
        elif z == "3":
            z = "HISTORY"
        student["Name"] = x
        student["Grade"] = y
        student["Class"] = z
        studentList.append(student)
    for i in studentList:
        print("Name:", i["Name"]+",", "Grade:", i["Grade"]+",", "Class:", i["Class"])
studentInput()
        # [f"Name: {x} Grade: {y} Class {z}"])
        # studentStr += str(', '.join(studentList[i])) 
        # studentStr += " || "
        # # globals()[f"tempvar{i}"] = f"Name: {x} Grade: {y} Class {z}"
        # globals()[f"tempvar{i}"] = str(', '.join(studentList[i]))2
    # for k in range(0, int(studentNum)):
    #     print(f"tempvar{k}")
     

    #  for i in range(0, int(studentnum)):

    #      studentList[0].append(input())
