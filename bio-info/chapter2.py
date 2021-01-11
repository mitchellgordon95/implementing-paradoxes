from chapter1 import kmers
from collections import Counter

def find_15mers(seqs):
    kmer_counts = Counter()
    for seq in seqs:
        kmer_counts.update(kmers(seqs,15))

    return kmer_counts
