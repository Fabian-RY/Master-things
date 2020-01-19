#! /usr/bin/env python3

def Fasta_iterator(fasta_filename):
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

def compare_fasta_file_identifiers( fasta_filenames_list ):
    data = {}
    frequency = {}
    elements = {}
    # Getting a dict with file as keys and a list of ID as values
    for file in fasta_filenames_list:
        elements[file] = set()
        for id, seq in Fasta_iterator(file):
            id = id.lower()
            frequency[id.lower()] = frequency.get(id, 0) + 1
            elements[file].add(id)
    # Union
    union_set = set()
    for set_ in elements.values():
        union_set = union_set.union(set_)
    # Intersection
    intersection = set(elements[file])
     # Necesitamos que tenga al menos un elemento
    for set_ in elements.values():
        intersection.intersection_update(set_)
    data["intersection"] = intersection
    data["union"] = union_set
    data["frequency"] = frequency
    # Check uniqus
    specific = {}
    for id in frequency:
        if frequency[id] == 1:
            for file_ in elements:
                if (not file_ in specific): specific[file_] = set()
                if id in elements[file_]: specific[file_].add(id)
    data["specific"] = specific
    return data

archivo_list=["fasta1.fa","fasta2.fa","fasta3.fa","fasta4.fa"]
print(compare_fasta_file_identifiers(archivo_list))
