"""3.2 
Arguments and pandas
Create a second script that takes the file you created in the previous task as a user defined input argument. Use argparse for this.
Make sure to add useful help messages to the arguments in your script.
use the csv module to read the csv file you created
Convert the data to a pandas dataframe. Print a statistical summary of your data.
"""

#Task 3.2 — moving from file manipulation with csv to argument handling and pandas.
"""Takes a CSV filename as a user-supplied argument (using argparse, not sys.argv).
1. Shows help messages for clarity.
2. Reads that CSV file using the csv module.
3. Converts it into a pandas DataFrame.
4. Prints a statistical summary of the data."""

#!/usr/bin/env python3

import argparse
import csv
import pandas as pd

def main():
    # 1️ Set up the argument parser , in this case 'description', could have been 'program' or 'usage'
    parser = argparse.ArgumentParser() #can be empty
    parser.add_argument( # Adding an argument to the parser object with help messages and setting parameters such as its required
        "-f", "--file", #You can use either one, they both store their value in the same variable (args.file).
        type=str, #for it to check if/when crushing
        required=True,
        help="Path to the CSV file created in the previous exercise"
    )
    args = parser.parse_args() #“Look at what the user typed when running the script and put those values into the variable args.”

    csv_path = args.file #renaming the input argument value the user provided.
    """
I can skip #2 and #3 and go via
df = pandas.read_csv('csv_path')
manual csv.reader approach vs the shortcut with pandas.read_csv().
    """
    # 2️ Read the CSV using the csv module first 
    """this block of code is about reading your CSV file manually 
    using Python's built-in csv module, before you move on to converting it into a pandas DataFrame."""
    rows = [] #You create an empty list that will store each row from your CSV file.
    with open(csv_path, "r", newline="") as f: #automatically closes the file afterward. Opens the file (in read mode) ="" avoids issues with extra blank lines on some systems.
        reader = csv.reader(f) #This creates a CSV reader object that can read each line in the file and split it into a list of values
        for row in reader: #This loop goes through each row from the CSV file (as a list) 
            rows.append(row) #and appends it to the list rows.

    print("\nCSV content (via csv module):")
    for row in rows:
        print(row)

    # 3️ Convert to a pandas DataFrame
    df = pd.DataFrame(rows)      # convert list of lists into dataframe
    """end of the read_csv()"""
    print(df.head())             # quick look
    print(df.describe())   # statistical summary, OR df[["0","1","2"]].describe()
if __name__ == "__main__":
    main()
#Task 3.3
"""
Biopython Exercise — Mini FASTA toolkit with Biopython (Seq, SeqRecord, SeqIO)

Remember that you can copy these commented code blocks into your script to not have to refer back to your browser window

Step 0 — Create the input file:
Save the text below as a file named `dna.fasta` in the same folder as your script:

>seq1
ATGCATGCATGCATGCATGCATGCATGC
>seq2
GATTACAGATTACAGATTACA
>seq3
CGCGATATCGCGATATCGCGATATCGCGATATCGCGATATC
>seq4
TTTAAACCCGGGTTTAAA
>seq5
GCCGCGGCGCGCCGCGGCGCGCCGCGGCGC
>seq6
ATATATATATATATATATATAT
>seq7
ACGTTGCAACGTTGCAACGTTGCAACGTTGCA
>seq8
CATGACTGACTGATGCTAGCTAGCTGATCGTACGATC"""