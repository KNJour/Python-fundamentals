for i in range(151): #1
    print(i)

for i in range(0, 1001, 5): #2
    print(i)

for i in range(101): #3
    if i % 10 == 0:
        print ("Coding Dojo")
        continue
    if i % 5 == 0:
        print("Coding")
        continue
    else:
        print(i)

x = 0 #4
i = 0
while i <= 500000:
    if i % 2 != 0:
        x += i
    i += 1
print(x)

for i in range(2018, 0, -4): #5
    print(i)

lowNum = 2  #6
highNum = 12
mult = 3
for l in range(lowNum, highNum + 1):
    if l % mult == 0:
        print(l)