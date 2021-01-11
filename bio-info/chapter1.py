from collections import Counter
from itertools import combinations


def kmers(seq: str, k: int):
    """Counts the kmers in a sequence."""
    assert k <= len(seq)
    kmer_counts = Counter()
    for i in range(len(seq)):
        if i + k > len(seq):
            break
        kmer_counts[seq[i:i+k]] += 1
    return kmer_counts

def hamming(seq: str, d: int):
    """Iterates through all kmers exactly hamming distance d away from seq."""
    assert d <= len(seq)
    bps = list(seq)
    for mutation_indices in combinations(range(len(seq)), d):
        possible_muts = [set(['a', 'c', 'g', 't']) for _ in range(d)]
        for index, possible_mut in zip(mutation_indices, possible_muts):
            possible_mut.remove(bps[index])
        possible_muts = [list(x) for x in possible_muts]
        for mutation_num in range(3**d):
            out = bps.copy()
            for i in reversed(range(d)):
                assignment = mutation_num // 3**i
                mutation_num -= assignment * 3**i
                out[mutation_indices[i]] = possible_muts[i][assignment]
            yield ''.join(out)

def approx_count(seq: str, k: int, d: int):
    """Counts all kmers in seq with at most d mismatches."""
    assert d <= k and k <= len(seq)
    kmer_counts = kmers(seq, k)
    final_counts = Counter()
    for kmer, count in kmer_counts.items():
        for i in range(1, d+1):
            for mutation in hamming(kmer, i):
                final_counts[mutation] += count
    return final_counts + kmer_counts

if __name__ == "__main__":
    print(kmers("accctg", 1))
    print(kmers("accctg", 2))

    print(list(hamming('aaa', 2)))

    print(approx_count('acaca', 5, 2))

