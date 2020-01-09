#! /usr/bin/env python3

def count_sequences_by_residue_threshold(filename, residue, threshold=0.03):
    total = 0
    number_of_residues = 0
    length = 0
    seq_file = open(filename)
    seq_file.readline()
    for line in seq_file:
        if line[0] == ">":
            if (number_of_residues/length >= threshold):
                total += 1
            number_of_residues = 0
            length = 0
        else:
            for seq_residue in line:
                if seq_residue == residue:
                    number_of_residues += 1
                length += 1

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
    out_file.write("%s\t"%(id))
    for line in seq_file:
        if (line[0] == ">"):
            inital_aas = seq[:first_n]
            out_file.write("%s\t"%(inital_aas))
            aas = seq[-last_m:]
            out_file.write("%s\t"%(aas))
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
            out_file.write("%s\n"%(text[:-1]))
            id = line[1:-1]
            out_file.write("%s\t"%(id))
            seq = ""
        else:
            seq += line[:-1]
    aas = seq[:first_n]
    out_file.write("%s\t"%(aas))
    text = ""
    for aa in aas:
        text += "%s:%i,"%(aa, seq.count(aa))
    out_file.write("%s"%(text[:-1]))
    seq_file.close()
    out_file.close()


print(count_sequences_by_residue_threshold("example_fasta_file.fa", "A", 0.03))
print_sequence_tails("example_fasta_file.fa", "result.tsv")
