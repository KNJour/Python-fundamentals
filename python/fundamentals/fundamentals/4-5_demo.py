x = "Hello Python"
print(x)
y = 42
print(y)

# composite types
ninjas = ['Harleigh','Keith','Rodney']

print(ninjas[2])

#dictionaries are objects
#Key values need to be in quotes
dojo = { 'location' : 'Chicago',"num_of_ninjas":37}

# tuples are immutable lists - they dont change
tuple_dojo = ("Chicago",37)

# Loops! use len() for length - can increment different with a ,

for x in range (len(ninjas) - 1, -1, -1):
    print (ninjas[x])

for x in range(0,len(ninjas)):
    print(ninjas[x])

    #conditionals
if name == "Mr. Nibbles":
    print('Hello' + " " + name)
    print("Hello",name)
        #f string must be double quotes
    print(f"Hello {name}")
elif name == "Benny Bob":
    print("Oh no!")
else:
    print("Where is Mr. Nibbles")
# taking a variable and making it equal to a function
# fav_color = "purple"
# color = input("What is your favorite color?")
# while color!= fav_color:
#     color = input(f"what is wrong. \nWhat is yoru favorite color?\n")
# print(f"Your favorite color is {color}")