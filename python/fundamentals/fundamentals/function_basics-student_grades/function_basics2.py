
# def countdown(num):
#     result = []``
#     for i in range(num, -1, -1):
#         result.append(i)
#     return result
# print(countdown(10))

# def listFirstSecond(x):
#     print(x[0])
#     return x[1]

# x = listFirstSecond([1,2])
# print(x)

# def plusLength(arr):
#     return arr[0] + len(arr)
# total = plusLength([10,20,20,4,6,9])
# print(total)

# def valueGreater(x):
#     newList = []
#     count = 0
#     for i in range (len(x)):
#         if (x[i] > x[1]):
#             newList.append(x[i])
#             count = count + 1
#     print(count)
#     if(len(newList) < 2):
#         return False
#     return newList
# answer = valueGreater([2, 4, 6, 9, 9, 1, 1, 0])
# print(answer)


def lengthValue(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
answer = lengthValue(5,4)
print(answer)