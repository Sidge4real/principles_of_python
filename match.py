seq1 = 'atgcttca'
seq2 = 'atgctfca'

zip_seqs = zip(seq1,seq2) #pair sequals

enum_seqs = enumerate(zip_seqs) #add index per pair

for i, (a,b) in enum_seqs:
    if a != b:
        print(f'no match at index {i}') 