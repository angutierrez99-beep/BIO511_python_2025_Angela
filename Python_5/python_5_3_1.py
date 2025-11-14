"""3.1 File Manipulation Create a script that: 
1. Uses with open() to create a csv file with 5 rows and 5 columns. 
2. Make sure to save the file and use comma as the separator.
3. Appends a row to the file based on the users input, using argv."""

import sys, csv, os

filename = "myfile.csv" # Step 1️: Defining the file name

# Step 2️: If the file doesn’t exist, create a 5×5 CSV
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file: #write if not there, overwrite otherwise
        writer = csv.writer(file)
        for i in range(1, 6): #for variable i in range 1-6 = 1, 2, 3, 4, 5.
            row = [f"r{i}c{j}" for j in range(1, 6)] #row = i, column=j with range 1-6, final output will be r1c1, r1c2, etc
            writer.writerow(row) #write the above aka create a 5x5 CSV
    print(f"Created {filename} with 5 rows and 5 columns.")

# Step 3️: Get user input from argv (command-line arguments)
new_row = sys.argv[1:]  # 1: means everything after the script name [0]
# Step 4️: Append the user input row to the CSV
if new_row:  
    with open(filename, "a", newline="") as file: # 'a' append
        writer = csv.writer(file)
        writer.writerow(new_row)
    print(f"Appended row to {filename}: {new_row}")
else:
    print("No input given")
