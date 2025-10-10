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
result = "unset" # global variable
def aggregate(seq, mode, threshold):
    if mode in ("sum", "count"): # mode is a string, not a list so you need decisions (if, elif, else).
        result = 0
    else:
        result = None


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
print("Global result before function call:",result)

## Call and print each mode separately
nums = [-10, -5, 0, 5, 10]
limit = 6
print("Sum mode:", aggregate(nums, "sum", limit)) # -> 10
print("Count mode:", aggregate(nums, "count", limit)) # -> 1
print("Max mode:", aggregate(nums, "max", limit)) # -> 10

#print global again to show it’s unchanged
print("Global result after function calls:", result)