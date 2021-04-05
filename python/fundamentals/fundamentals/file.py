num1 = 42 # variable declaration number
num2 = 2.3 # variable declaration number
boolean = True # boolean
string = 'Hello World' # string declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') # tuple initialize
print(type(fruit)) # log statement
print(pizza_toppings[1]) #access 
pizza_toppings.append('Mushrooms') # list change value
print(person['name']) #log statement access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #access value

if num1 > 45: # conditional - if
    print("It's greater") #log statement
else: # conditional - else
    print("It's lower")

if len(string) < 5: # conditional - if
    print("It's a short word!") #log statement
elif len(string) > 15: # conditional - else if
    print("It's a long word!") #log statement
else: # conditional - ese
    print("Just right!") #log statement

for x in range(5):   # for loop  until 5
    print(x)  # log statement x
for x in range(2,5): # loops between start 2 and stop 5
    print(x) # log statement x
for x in range(2,10,3): #loop start 2 end 10 increment 3
    print(x) # log statement x
x = 0 # variable declaration number
while(x < 5): # while loop start top when x is no longer less than 5
    print(x) #log statement 
    x += 1 #increment by 1

pizza_toppings.pop() #removes last item from pizza topping
pizza_toppings.pop(1) #REMOVES 2ND ELEMENT FROM PIZZA TOPPING

print(person) # log statement
person.pop('eye_color') #add value to person dictionary
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if start
        continue #continue (moves to next iteration of loop)
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if start
        break #break ends loop

def print_hello_ten_times():  #function is defined
    for num in range(10): #for loop range of 10 (10 times)
        print('Hello') #log hello

print_hello_ten_times() #calls function

def print_hello_x_times(x): #function is defined paramater x determines how many times it loops
    for num in range(x): #for loop range of the argument used when calling
        print('Hello') #log statement

print_hello_x_times(4) #calls function prints hello x times

def print_hello_x_or_ten_times(x = 10): #function is defined
    for num in range(x): #for loop range of x
        print('Hello') #log statement

print_hello_x_or_ten_times() #calls function prints 10 times 
print_hello_x_or_ten_times(4) #calls function prints 6 times (4-10)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)