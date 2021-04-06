# def searchInList(list, val):
#     for i in range(len(list)):
#         if list[i] == val:
#             return True
#     return False
        


# searchInList([2,5,6,8,9,5], 8)

capitals = { "Washington": "Olympia", "California": "Sacramento", "idaho": "Boise" }


def printValues(some_dict):
    for key, val in some_dict.items():
        print(val)
print(printValues(capitals))