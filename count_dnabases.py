def count_dna_bases(dna):
    valid_bases = {'A', 'T', 'C', 'G'}
    
    if not set(dna).issubset(valid_bases):
        return "Error: DNA string contains invalid characters."
   
    base_count = {base: dna.count(base) for base in valid_bases}
    
    return base_count

dna_input = "ATGCGATAAGCTTAA"
result = count_dna_bases(dna_input)
print(result)
