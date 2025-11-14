def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return

my_added_numbers = add_two_numbers(5, 10)
print(my_added_numbers) # will print 15

# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so 
# use different variable names inside the function). Do not rename these.
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
    count = 0 #starts at 0 
    for numbers in seq:
        if numbers > lim: #checks whether the number (or value) is greater than the limit (4).
            count += 1 #if its True, add +1 each time
    return count #The result is then stored in a global variable (result) when you call the function.
# e) Outside the function:
#    - Print the GLOBAL count.
print(count)
#    - Call count_above(nums, limit) and print the returned number.
#    - Print the GLOBAL count again (notice the global didn’t change).

var = count_above(nums, limit) #calling
print(var) # printing the returned number
print(count) #GLOBAL count again

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

def summarize_text(s): # a) Define the function that takes argument s
    summary = {     # b) Local variable: result dictionary
        "digits": 0,
        "letters": 0,
        "other": 0
    }
    for character in s:
        if character.isnumeric(): 
            summary["digits"] += 1
        elif character.isalpha(): 
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary 
print("4.2 Global summary before function call:", summary) #GLOBAL

results = summarize_text(text) # "Room 101: bring 2 apples & 1 banana.
print("Returned local summary:", results)

print("4.2 Global summary after function call:", summary)  #GLOBAL

#4.3 
#C) Aggregate with mode  (uses nums, limit, result)
# Goal: nested decisions based on a mode string. Return one final value.
# a) Define a function named aggregate that takes three arguments: seq, mode, threshold.
# b) Inside the function, create a LOCAL variable named result.
#    Initialize it based on mode:
#       - if mode is "sum": start at 0
#       - if mode is "count": start at 0
#       - if mode is "max": start at None (meaning “no qualifying value yet”)
# c) Loop through each number n in seq:
#       - First, ignore n if it is negative (skip it).
#       - If n is at least threshold, then:
#           * if mode is "sum": add n to result
#           * elif mode is "count": increase result by 1
#           * else (treat any other mode as "max"):
#                 if result is None or n is greater than result, update result to n
# d) Return the result.
# e) Outside the function:
#    - Print the GLOBAL result.
#    - Call and print each of these:
#         aggregate(nums, "sum", limit)
#         aggregate(nums, "count", limit)
#         aggregate(nums, "max", limit)
#    - Print the GLOBAL result again.
# Your Code below

def aggregate(seq, mode, threshold):
    if mode == "sum":
        result = 0
    elif mode == "count":
        result = 0
    elif mode == "max":
        result = None 
    else:
        result = None
        mode = "max"
#C
    for n in seq:    
        if n < 0:
            continue #to ignore negatives
        if n >= threshold:
            if mode == "sum":
                result += n 
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result:
                    result = n
    return result  
# Print the GLOBAL result 
print("4.3 Global result before function call:", result)

## Call and print each mode separately
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
print("Sum mode:", aggregate(nums, "sum", limit)) # -> 20
print("Count mode:", aggregate(nums, "count", limit)) # -> 3
print("Max mode:", aggregate(nums, "max", limit)) # -> 9

#print global again to show it’s unchanged
print("4.3 Global result after function calls: still", result)