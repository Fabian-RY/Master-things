#! /usr/bin/env python3

def calculate_aminoacid_frequencies(fasta_filename,
                                    subsequences_filename,
                                    number_of_repetitions,
                                    output_filename):
    """
    """
    total_at_least_N_repetitions = 0
    seqs = {}
    input = open(fasta_filename)
    for line in input:
        if line.startswith(">"):
            id = line.strip()[1:]
            seqs.setdefault(id, "")
        else:
            seqs[id] += line.strip()
    input.close()
    num_of_seqs = len(seqs)
    subseq_file = open(subsequences_filename)
    subseqs = []
    for line in subseq_file:
        subseq = line.strip()
        number_of_proteins_threshold = 0
        for seq in seqs.values():
            repetitions = seq.count(subseq)
            if (repetitions >= number_of_repetitions):
                number_of_proteins_threshold += 1
        subseqs.append([number_of_proteins_threshold, subseq])
    subseq_file.close()

    output = open(output_filename, "w")
    output.write("#Number of proteins: {:>12}\n".format(num_of_seqs))
    output.write("#Number of subsequences: {:>8}\n".format(len(subseqs)))
    output.write("subsequence proportions:\n")
    for number, subseq in sorted(subseqs, reverse=True):
        proportion = number/num_of_seqs
        output.write("{sub}\t{number}\t".format(sub=subseq, number=number))
        output.write("{0:.4f}\n".format(proportion))

#calculate_aminoacid_frequencies("example_fasta_file.fa", "sequence_fragments.txt", 10, "output.txt")
