def codons(sequence_file):
    """A function that reads a fasta file and returns a list of codons for each sequence in the file"""
    
    # First we read the fasta file and store the sequences as a string
    sequence = ""
    
    # Open the file
    with open(sequence_file) as fasta_file:
        # Read the file line by line
        for row in fasta_file:
            # If the line starts with '>', it is a header and we skip it
            if not row.startswith('>'):
                # If the line does not start with '>', it is a sequence and we add it to the list
                sequence += row.strip()
    
    # Now we split the sequences into codons
    sequence_codon_list = []
    
    # Loop over the sequence in steps of 3
    for i in range(0, len(sequence), 3):
        # Append the codon to the list if it is a full codon (3 nucleotides)
        if i + 3 <= len(sequence):
            # Then append the codon to the list
            sequence_codon_list.append(sequence[i:i + 3])
    
    # Return the list of codons
    return sequence_codon_list


def exercise_function(sequence_codons):
    """What does this function do?"""
    aa_string = ""
    for codon in sequence_codons:
        amino_acid = Seq(codon).translate()
        aa_string += str(amino_acid)
    return aa_string
