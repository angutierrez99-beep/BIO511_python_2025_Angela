import Bio
print("Biopython version:", Bio.__version__)

from Bio.Seq import Seq
seq = Seq("ATGCTTGA")
print("Reverse complement:", seq.reverse_complement())
