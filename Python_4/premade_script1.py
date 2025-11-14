from Bio.Seq import Seq

def codons(sequence_file):
    """A function that reads a fasta file and returns a list of codons for each sequence in the file"""
    
    sequence = ""
    with open(sequence_file) as fasta_file:
        for row in fasta_file:
            if not row.startswith('>'):
                sequence += row.strip()
    
    sequence_codon_list = []
    for i in range(0, len(sequence), 3):
        if i + 3 <= len(sequence):
            sequence_codon_list.append(sequence[i:i + 3])
    
    return sequence_codon_list


def exercise_function(sequence_codons):
    """Translates a list of codons into an amino acid string"""
    aa_string = ""
    for codon in sequence_codons:
        amino_acid = Seq(codon).translate()
        aa_string += str(amino_acid)
    return aa_string
