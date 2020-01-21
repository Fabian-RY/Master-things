#! /usr/bin/env python3
"""
    @author: Fabián Robledo
"""

aminoacid_mw = {'A': 89.09, 'C': 121.16, 'E': 147.13, 'D': 133.1, 'G': 75.07, 'F': 165.19, 'I': 131.18, 'H': 155.16, 'K': 146.19, 'M': 149.21, 'L': 131.18, 'N': 132.12, 'Q': 146.15, 'P': 115.13, 'S': 105.09, 'R': 174.2, 'T': 119.12, 'W': 204.23, 'V': 117.15, 'Y': 181.19}

def FASTA_iterator(fasta_filename):
    seq = ""
    file = open(fasta_filename)
    id = file.readline()[1:].strip()
    for line in file:
        if line.startswith(">"):
            yield(id, seq)
            id = line[1:].strip()
            seq = ""
        else:
            seq += line.strip("\n")
    yield(id, seq)
    

def get_max_sequence_length_from_FASTA_file ( fasta_filename ):
    fasta_iterator = FASTA_iterator(fasta_filename)
    return max(map(lambda x: len(x[1]), fasta_iterator ))
 
def get_min_sequence_length_from_FASTA_file ( fasta_filename ):
    fasta_iterator = FASTA_iterator(fasta_filename)
    return min(map(lambda x: len(x[1]), fasta_iterator ))

def get_longest_sequences_from_FASTA_file( fasta_filename ):
    max_length = get_max_sequence_length_from_FASTA_file(fasta_filename)
    fasta_iterator = FASTA_iterator(fasta_filename)
    longest = filter(lambda x: max_length == len(x[1]), fasta_iterator)
    return sorted(longest, key= lambda x: x[0].lower())

def get_shortest_sequences_from_FASTA_file( fasta_filename ):
    min_length = get_min_sequence_length_from_FASTA_file(fasta_filename)
    fasta_iterator = FASTA_iterator(fasta_filename)
    longest = filter(lambda x: min_length == len(x[1]), fasta_iterator)
    return sorted(longest, key= lambda x: x[0].lower())

def get_molecular_weights( fasta_filename ):
    protein_iterator = FASTA_iterator(fasta_filename)
    weight = dict()
    for id_, prot in protein_iterator:
        weight[id_] = sum(aminoacid_mw[aa] for aa in prot)
    return weight
    
def get_sequence_with_max_molecular_weight( fasta_filename ):
    weights = get_molecular_weights(fasta_filename).items()
    max_weight = max(weights, key= lambda x: x[1])
    return max_weight

print(1, get_max_sequence_length_from_FASTA_file ("example_fasta_file.fa"))
print(2, get_min_sequence_length_from_FASTA_file ("example_fasta_file.fa"))
#print(3, get_longest_sequences_from_FASTA_file("example_fasta_file.fa"))
print(4, get_shortest_sequences_from_FASTA_file("example_fasta_file.fa"))
print(5, get_molecular_weights("example_fasta_file.fa"))
print(6, get_sequence_with_max_molecular_weight("example_fasta_file.fa"))