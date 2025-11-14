#3 https://n2bin-gu.github.io/BIO511-2025/practicals/Practicals%20-%20Python/PRACTICAL_LOOPING.html
# Example code
# Make a list
mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
# You can double check if it's a list
print(type(mylist))
# print your list
print(mylist)

# print the first item in your list
print(f"The first item in my list is '{mylist[0]}'")
# 3.1 Simple loops
# create a list of 7 items
# Loop over the list printing each item of the list.
list01 = [1, 2, 3, 4, 5, 6, 7]
for n in list01:
    print(n)

list02 = [8, 9, 10, 11, 12, 13, 14]
for n in list02:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

list03 = [15, 16, 17, 18, 19, 20, 21]
for n in list03:
    if n == 19:
        print("Found 19, stopping the loop")
        break
    print(f"Loop {n}: {n}")

### 3.2.1 
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
startcodon = 'ATG' # ATG is a start codon
stopcodons = ['TAA', 'TAG', 'TGA'] # TAA, TAG, and TGA are stop codons 
results = {}

for sequence in sequences:
    start_index = sequence.find(startcodon)  # position of start codon (-1 if not found)
    stop_index = None
    for stop in stopcodons:
        position = sequence.find(stop)
        if position != -1:  # if found, != is the does not equal sign so if stop would have been before
            if stop_index is None or position < stop_index:
                stop_index = position  # keep the earliest one
    # Determine if start comes before stop
    if start_index != -1 and stop_index is not None and start_index < stop_index:
        results[sequence] = True
    else:
        results[sequence] = False
# Loop through dictionary and print results
for sequence, has_start_before_stop in results.items():
    if has_start_before_stop:
        print(f"The sequence {sequence} has a start codon before a stop codon.")
    else:
        print(f"The sequence {sequence} does NOT have a start codon before a stop codon.")

### 3.2.2 
data = dict({'pat_001': ['bacZZt98', 'bac889Ytd'],
            'pat_002': ['bac0GFrr'], 
            'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']})

unique_bacteria = []
bacteria_dict = {} # will become {'bac...': []}

# Dictionary -> list
for key_patient, value_bact_list in data.items():
    print(key_patient)
    print(value_bact_list)
    for bacteria in value_bact_list:
        if bacteria not in unique_bacteria:
            unique_bacteria.append(bacteria)
print(f"Unique bacterias: {unique_bacteria}")

# List -> dict with empty lists
for bac in unique_bacteria:
    bacteria_dict[bac] = []
print(f"And transformed to dictionary with empty lists as: {bacteria_dict}")

# Fill each bacteria with the patients that have it
for pat, bact_list in data.items():
    for bac in bact_list:
        bacteria_dict[bac].append(pat)
print(f"Whereas the list now has values as patients: {bacteria_dict}")