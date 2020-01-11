#! /usr/bin/env python3
# 1)Given a multi-line protein FASTA file (filename), returns an integer corresponding
#to the total number of protein sequences having a relative frequency higher or equal
#than a given threshold for a given residue
def count_sequences_by_residue_threshold(filename, residue, threshold=0.03):
    total = 0
    number_of_residues = 0
    length = 0
    # The first line is ignored because it will always be an id and its not needed
    seq_file = open(filename)
    seq_file.readline()
    for line in seq_file:
        # Once we reach the new protein, we calculate the threshold for this sequence
        if line[0] == ">":
            if (number_of_residues/length >= threshold):
                total += 1
            # Then reset the counters for the next sequences
            number_of_residues = 0
            length = 0
        else:
            # If it's the sequence, calculate the number of residues
            number_of_residues += line.count(residue)
            length += len(line)

    if (number_of_residues/length >= threshold):
        total += 1
    return total


#2) Given a protein FASTA file (filename), save on a file (output_filename) the protein identifier,
#the first N-aminoacids, the last M-aminoacids and the absolute frequency in the protein of
#each of the first N-aminoacids and the last M-aminoacids. The fields must be separated by a
#tabulator, and one protein by line. The first line must be a line with a summary formatted as
#follows (replace the values FILENAME, N and M with the corresponding values).
def print_sequence_tails(filename, output_filename, first_n=10, last_m=10):
    seq_file = open(filename)
    out_file = open(output_filename, "w")
    seq = ""
    line = seq_file.readline()
    id = line[1:-1]
    number_of_seqs = 1
    data = ""
    data += ("%s\t"%(id))
    for line in seq_file:
        if (line[0] == ">"):
            number_of_seqs += 1
            inital_aas = seq[:first_n]
            data += "%s\t"%(inital_aas)
            aas = seq[-last_m:]
            data += "%s\t"%(aas)
            text = ""
            used = ""
            for aa in inital_aas:
                if aa not in used:
                    text += "%s:%i,"%(aa, seq.count(aa))
                    used += aa
            for aa in aas:
                if aa not in used:
                    text += "%s:%i,"%(aa, seq.count(aa))
                    used += aa
            data += "%s\n"%(text[:-1])
            id = line[1:-1]
            data += "%s\t"%(id)
            seq = ""
        else:
            seq += line[:-1]
    aas = seq[:first_n]
    data += "%s\t"%(aas)
    aas = seq[-last_m:]
    data += "%s\t"%(aas)
    text = ""
    used = ""
    for aa in inital_aas:
        if aa not in used:
            text += "%s:%i,"%(aa, seq.count(aa))
            used += aa
    for aa in aas:
        if aa not in used:
            text += "%s:%i,"%(aa, seq.count(aa))
            used += aa
    data += "%s"%(text[:-1])
    seq_file.close()
    out_file.write("# The file %s contains %i proteins."%(filename, number_of_seqs))
    out_file.write(" Here we show the code of the protein, the first %i aminoacids of each protein and the last %i aminoacids\n" % (first_n, last_m))
    out_file.write(data)
    out_file.close()

print(count_sequences_by_residue_threshold("example_fasta_file.fa", "A", 0.03))
print_sequence_tails("example_fasta_file.fa", "result.tsv", 3, 3)
