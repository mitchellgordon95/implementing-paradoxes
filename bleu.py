from collections import Counter
import math

def ngrams(sentence, n):
    words = sentence.split()
    ngram_counts = Counter()
    for i in range(len(words)):
        if i + n > len(words):
            break
        ngram_counts[' '.join(words[i:i+n])] += 1
    return ngram_counts


def modified_ngram_prec(sentence, refs, n):
    sentence_ngrams = ngrams(sentence.lower(), n)
    max_ref_ngrams = Counter()
    for ref in refs:
        for ngram, count in ngrams(ref.lower(), n).items():
            max_ref_ngrams[ngram] = max(count, max_ref_ngrams[ngram])

    clipped_correct, total = 0, 0
    for ngram, count in sentence_ngrams.items():
        total += count
        if ngram in max_ref_ngrams:
            clipped_correct += min(count, max_ref_ngrams[ngram])

    return clipped_correct, total


def bleu(corpus):
    # The total number of unigrams, bigrams, trigrams, and 4-grams in our candidate sentences.
    total_ngrams = [0,0,0,0]
    # The number of those ngrams that also occur in any reference (associated with the candidate),
    # clipped to the number of times the ngram occurs in a single reference (associated with the candidate).
    clipped_correct = [0,0,0,0]
    # The sum of all the candidate lengths and the closest length references, respectively.
    candidate_lens, best_ref_lens = 0, 0

    for candidate, refs in corpus:
        for n in range(4):
            correct, total = modified_ngram_prec(candidate, refs, n+1)
            clipped_correct[n] += correct
            total_ngrams[n] += total

        candidate_len = len(candidate.split())

        best_len, best_diff = float('inf'), float('inf')
        for ref in refs:
            ref_len = len(ref.split())
            diff = abs(ref_len - candidate_len)
            if diff < best_diff:
                best_len = ref_len
                best_diff = diff
            elif diff == best_diff and ref_len < best_len:
                best_len = ref_len

        candidate_lens += candidate_len
        best_ref_lens += best_len

    # Geometric average over the precisions for unigrams, bigrams, etc.
    precs = [correct / total for correct, total in zip(clipped_correct, total_ngrams)]
    geom_avg_prec = math.exp(sum([math.log(prec) if prec > 0 else float('-inf') for prec in precs]) / 4)

    brev_penalty = math.exp(1 - best_ref_lens / candidate_lens) if best_ref_lens > candidate_lens else 1

    return brev_penalty * geom_avg_prec


print(
    bleu([
        ("the the the the the the the",
            ["the cat is on the mat",
            "there is a cat on the mat"]),
        ("It is a guide to action which ensures that the military always obeys the commands of the party",
            ["It is a guide to action that ensures that the military will forever heed Party commands",
            "It is the guiding principle which guarantees the military forces always being under the command of the Party",
            "It is the practical guide for the army always to heed the directions of the party"]),
        ])
)
