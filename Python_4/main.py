#!/usr/bin/env python3
from Python_4.premade_script import codons
import argparse
import os


def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Process a string and a folder.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Input sequence file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input string as an argument
    sequence_codons = codons(args.sequence)
    
    # Here the students should check the output of the function
    print(sequence_codons) # REMOVE THIS
    
    # Here the students will need to call the exercise_function from my_function.py
    exercise_output = exercise_function(sequence_codons) # REMOVE THIS
    
    # And check the output of that function
    print(exercise_output) # REMOVE THIS
if __name__ == "__main__":
    main()
