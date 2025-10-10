def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return

my_added_numbers = add_two_numbers(5, 10)
print(my_added_numbers) # will print 15

# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# 4 Exercises
# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"

#4.1 
# Count-above  (uses nums, limit, count)
# Goal: make a small function called whatever you want and then call(run) it.

# a) Define a function named count_above that takes two arguments: seq and lim.
# b) Inside the function, create a LOCAL variable named count starting at 0.
# c) Loop through seq; for each number strictly greater than lim, increase count by 1.
# d) Return count.

def count_above(seq, lim):
    count = 0 #starts at 0 and goes up to 999 i guess?
    for numbers in seq:
        if numbers > lim: #checks whether the number (or value) is greater than the limit (4).
            count += 1 #if its True, add +1 each time
    return count #The result is then stored in a global variable (result) when you call the function.
# e) Outside the function:
#    - Print the GLOBAL count.
#    - Call count_above(nums, limit) and print the returned number.
#    - Print the GLOBAL count again (notice the global didn’t change).

print(count)

#var = count_above(nums, limit) #calling
#print(var)
print(count_above([1, 2, 3, 4, 8], 5)) 

#4.2
# Text summary  (uses text, summary)
# Goal: classify characters with an if/elif/else chain and return a clear result.

# a) Define a function named summarize_text that takes one argument: s.
# b) Inside the function, create a LOCAL variable named summary that holds a result dictionary
#    with exactly these keys: "digits", "letters", "other" — each starting at 0.
# c) Loop through each character in s:
#       - if the character is a digit, increase "digits"
#       - elif the character is a letter, increase "letters"
#       - else increase "other"
# d) Return the summary dictionary.
# e) Outside the function:
#    - Print the GLOBAL summary.
#    - Call summarize_text(text) and print the returned dictionary.
#    - Print the GLOBAL summary again.

summary = "unset" # Global variable
def summarize_text(s): # a) Define the function
    summary = {     # b) Local variable: result dictionary
        "digits": 0,
        "letters": 0,
        "other": 0
    }
    #return summary= that first return made Python exit the function immediately, before it ever reached the loop
    for character in s:
        if character.isnumeric(): 
            summary["digits"] += 1
        elif character.isalpha(): #asked chatgpq
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary #right where the retunr should be 
print("Global summary before function call:", summary) #GLOBAL

text = "Hello123!?"                                    #LOCAL
results = summarize_text(text)
print("Returned local summary:", results)

print("Global summary after function call:", summary)  #GLOBAL