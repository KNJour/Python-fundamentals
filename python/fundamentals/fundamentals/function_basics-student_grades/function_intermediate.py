
#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]['y'] = 30
print(sports_directory)
print(students)
print(x)
print (z)

# #2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i])
iterateDictionary(students) 

def iterateDictionary(theKey, students):
    for i in range(len(students)):
        print(students[i][theKey])
iterateDictionary('last_name', students) 

#3

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(d):
    x = len(d['locations'])
    print(f"{x} LOCATIONS")
    for i in range(len(d['locations'])):
        print(d['locations'][i])

    y = len(d['instructors'])
    print(f"{y} INSTRUCTORS")
    for n in range(len(d['instructors'])):
        print(d['instructors'][n])

printInfo(dojo)

