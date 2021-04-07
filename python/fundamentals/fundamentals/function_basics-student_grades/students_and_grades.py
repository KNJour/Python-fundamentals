# fullList = {'Student': 'John', 'Course': 'Math', 'Grade': '88'}

# studentNum = input('How Many Students Do You Have?')

def studentInput():
    studentNum = input('How Many Students Do You Have?')
    studentList = []
    studentStr = ""
    for i in range(0, int(studentNum)):
        x = input("Student Name:")
        y = input("Student Grade")
        z = input("Select a course 1 - MATH, 2 - SCIENCE, 3 - HISTORY")
        if z == "1":
            z = "MATH"
        elif z == "2":
            z = "SCIENCE"
        elif z == "3":
            z = "HISTORY"
        studentList.append([f"Name: {x} Grade: {y} Class {z}"])
        studentStr += str(', '.join(studentList[i])) 
        studentStr += " || "
        # globals()[f"tempvar{i}"] = f"Name: {x} Grade: {y} Class {z}"
        # globals()[f"tempvar{i}"] = str(', '.join(studentList[i]))
        
    print(studentStr)
    # for k in range(0, int(studentNum)):
    #     print(f"tempvar{k}")
studentInput()
     

    #  for i in range(0, int(studentnum)):

    #      studentList[0].append(input())
