def isValid(str):
    countParenth = 0
    countSquig = 0
    countBracket = 0
    for i in range(0, len(str)):
        if str[i] == "(":
            countParenth += 1
        if str[i] == ")":
            countParenth -= 1
        if countParenth < 0:
            return False
            # new section
        if str[i] == "[":
            countBracket += 1
        if str[i] == "]":
            countBracket -= 1
        if countBracket < 0:
            return False
            # new section
        if str[i] == "(":
            countSquiqs += 1
        if str[i] == ")":
            countSquiqs -= 1
        if countSquiqs < 0:
            return False

    if countParenth != 0 or countSquiqs != 0 or countBracket != 0:
        return False
    else:
        return True

print(isValid("[]{}()"))