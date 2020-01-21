#! /usr/bin/env python3

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
    for file_ in elements:
            specific[file_] = elements[file_]
            for file_2 in elements:
                if (file_ != file_2):
                    print(file_, file_2)
                    print(specific[file_], elements[file_2])
                    specific[file_] = specific[file_].difference(elements[file_2])
                    print(specific[file_])
    data["specific"] = specific
    return data
