
#--------------2.1 Data type usage--------------#
#### Make a sequence of one value of each data type to its own variable. 
#### Afterwards, print all the variables and their type 
#### using the commands print() and type()
name = "Angela"
age = 26
km_from_home = 1.1

print(f"My name is {name},", type(name))

print(f"I am {age} years old,", type(age))

print(f"I am {km_from_home}km away from home,", type(km_from_home))


# Save a string to a variable
my_string = "'This is my string'"

# Check how many letters are in my_string. 
# It's the same thing as checking the length of a string.

len(my_string)
print(my_string, f"and the length of it is {len(my_string)} characters")

#------------2.2.2 Multi-way (If/elif/else clause)------------#
#### Pick the 'int' you created. Write an if-statement with 3 scenarios:
# I created age = 26
if age >= 1: #The integer could be positive
    print(f"The number {age} is positive")
elif age == 0: #The integer could be zero
    print("The number {age} is zero")
else: #The integer could be negative
    print("The number {age} is negative")

#------------2.2.3 Type gate + nested classification------------#
# List SEQUENCE
countries = ["USA", "UK", "Japan"]
print(f"My sequence is a {type(countries)}")
if type(countries) in (list, tuple, range):
    print(f"My {type(countries)} consist of countries")
    if type(countries) is list:
        if len(countries) == 0:
            print(f"The {type(countries)} consist of {len(countries)} countries")
        elif len(countries) == 1:
            print(f"The {type(countries)} consist of {len(countries)} country")
        elif len(countries) > 1:
            print(f"The {type(countries)} consist of {len(countries)} countries") 
else:
    print("My sequence has the wrong type for this task")