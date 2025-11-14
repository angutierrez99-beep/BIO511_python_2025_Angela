"""What does it does? 

defines a function
    it reads fasta files
    returns codons (3 AA in lenght) as list for each sequence of the file


NEW VARIABLE sequence 
is defined to 
1. read read the file and 
2. store sequences as codons in STRING format

via
1 open the file as fasta_file format

2. read the file line by line 

3. If the line starts with '>', it is a header and we skip it

4. If the line does not start with '>', it is a sequence and we add it to the list


NEW VARIABLE sequence_codon_list
is defined to 
1. Loop over the sequence in steps of 3 (codons) 
2.  Append the codon to the LIST if it is a full codon (3 nucleotides)
3. Then append the codon to the list (SEQUENCE)
Return the list of codons "sequence_codon_list"


defines a new function
exercise_function(sequence_codons):
    To reverse list to string?


3.1.2 
What's the input of the function 1?
    Fasta file

3.1.3 
In the main function of main.py, add a print statement to print the output of the function

3.2.1 
What's the input of the function 2?
    Codons
3.2.2 
What does this function do?
    takes each amino acid and translates them?
3.2.3 
Try calling it through main.py (see how the previous function is imported and used)
    Tried 

3.3 
Make the exercise_function work

3.3.1 
A non standard module is needed to run the function. Which? Install/use/call it
    from Bio.Seq import Seq 

3.3.2 
Check the output of the script
    (base) angelagtrrz@Mac ~ % /Users/angelagtrrz/miniconda3/bin/python /Users/angelagtrrz/repos/BIO511_python_2025_Angela/main1.py
    usage: main1.py [-h] -s SEQUENCE
    main1.py: error: the following arguments are required: -s/--sequence
    (base) angelagtrrz@Mac ~ % 


"""