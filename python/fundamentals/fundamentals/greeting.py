myName = "Keith"
name = input('What is your name?')
if name == myName:
    print("Hey, that's my name too!")
else:
    print(f'Hello {name}')

nameList = [] #part  3 & 4
flag = False
for i in range(1,11):
    loopName = input(f"give me name # {i}")
    if i > 1:
        k = 0
        flag = False
        while k < len(nameList):
            if loopName == nameList[k]:
                loopName = input("Please pick a different name")
                nameList.append(loopName)
                flag = True
                break
            k += 1
    if flag == False:
        nameList.append(loopName)
print(f"Hello {nameList}, it was nice to meet all of you")
