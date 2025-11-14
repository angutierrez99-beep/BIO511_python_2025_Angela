#!/usr/bin/env python3

#3.3.1 
# A) Load and report (use SeqIO) 
# https://biopython.org/wiki/SeqIO
# Im using Day6_Biopythin_BIO511 power point presentation to grab my commands needed
#   - Read all records from `dna.fasta`.
#   - For each record, print the record ID and the sequence length.
#   - Also print the first 10 bases of the sequence.

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord   # for 3.3.2
from Bio.SeqUtils import gc_fraction  # for 3.3.3

def main():
    print("=== 3.3.1 A) Load and report (SeqIO) ===")
    # Read all records once (so we can reuse them for B and C)
    records = list(SeqIO.parse("dna.fasta", "fasta"))
    print(f"Loaded {len(records)} records from dna.fasta\n")

    # For each record: ID, length, first 10 bases
    print("ID\tlen\tfirst10")
    for rec in records:
        seq = rec.seq
        first10 = str(seq)[:10]
        print(f"{rec.id}\t{len(seq)}\t{first10}")
    print()  # blank line for readability

    """
    It means:
    print the record ID
    \t tab space
    print “len=…”
    \t tab space
    print “first10=…”
    """

    #3.3.2 
    # B) Reverse complements to a new FASTA (use Seq, SeqRecord, SeqIO)
    # https://biopython.org/wiki/Seq
    #   - For each original record, create the reverse complement of its sequence.
    #   - Make a new SeqRecord for the reverse complement.
    #   - Set the new ID to "<oldid>_rc" and the description to "reverse complement of <oldid>".
    #   - Write all reverse-complement records to a file named `dna_rc.fasta`.

    print("=== 3.3.2 B) Reverse complements → dna_rc.fasta ===")
    rc_records = []  # empty list to store new reverse-complement records

    for rec in records:  # rec = one SeqRecord from the FASTA
        seq = rec.seq
        rc_seq = seq.reverse_complement()  # get reverse complement of the sequence
        # build a brand-new SeqRecord for the reverse complement
        rc_rec = SeqRecord(
            rc_seq,
            id=f"{rec.id}_rc",
            description=f"reverse complement of {rec.id}"
        )
        rc_records.append(rc_rec)
        # small print so you see what happened for each sequence
        print(f"Made RC for {rec.id} → new id: {rc_rec.id}")

    # write all RC records to a FASTA
    SeqIO.write(rc_records, "dna_rc.fasta", "fasta")
    print(f"Wrote {len(rc_records)} reverse-complement records to dna_rc.fasta\n")

    # 3.3.3 
    # C) GC% annotation to a new FASTA (use SeqRecord, SeqIO, SeqUtils.gc_fraction)
    # https://biopython.org/docs/dev/Tutorial/chapter_seq_objects.html
    #   - GC% = 100 * (G+C)/len; gc_fraction returns 0..1 (fraction), so multiply by 100.
    #   - Round to 1 decimal place.
    #   - Put it in the description as "GC=<value>%".
    #   - Write to dna_with_gc.fasta.

    print("=== 3.3.3 C) GC% annotation → dna_with_gc.fasta ===")
    gc_records = []

    for rec in records:
        seq = rec.seq
        # gc_fraction ignores ambiguous bases if we say ambiguous="ignore"
        gc_pct = 100.0 * gc_fraction(seq, ambiguous="ignore")  # fraction→percent
        gc_pct = round(gc_pct, 1)  # one decimal place

        # Keep id, extend description. (Simple version: always show rec.id)
        desc_text = f"{rec.id} GC={gc_pct:.1f}%"

        gc_rec = SeqRecord(
            seq,                # original sequence
            id=rec.id,          # keep original id
            description=desc_text
        )
        gc_records.append(gc_rec)
        print(f"Annotated {rec.id} with GC={gc_pct:.1f}%")

    SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")
    print(f"Wrote {len(gc_records)} GC-annotated records to dna_with_gc.fasta\n")

    # tip for manual check (don’t run here, just a reminder):
    # In your terminal you can do:
    #   cat dna_rc.fasta | head -n 10
    #   cat dna_with_gc.fasta | head -n 10
   
    # 3.3.4 
    # D) Translation (optional) ===
    # https://biopython.org/docs/dev/api/Bio.Seq.html
    # - Translate each DNA sequence and print the first 10 amino acids.
    # - Then read 'dna_rc.fasta' back in and confirm IDs/descriptions look correct.

    print("=== 3.3.4 D) Translation (optional) ===")

    # Loop through the original records and translate them
    for rec in records:
        aa_seq = rec.seq.translate()      # translate DNA → protein
        first10aa = str(aa_seq)[:10]      # first 10 amino acids
        print(f"{rec.id}\tAA (first10)={first10aa}")

if __name__ == "__main__":
    main()

# Note:
# GC has 3 hydrogen bonds (vs AT with 2), so higher GC% often means stronger (more stable) duplexes.