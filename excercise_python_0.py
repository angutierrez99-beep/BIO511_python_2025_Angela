import sys #to deal with Python itself: for reading the file path argument
import os #for interacting with the operating system: for handling file path operations

#### MAIN ####
file_path = sys.argv[1] #gives access to command-line arguments passed to your script.
print(os.path.basename(file_path)) #prints/extracts the file name (basename) from a full path.