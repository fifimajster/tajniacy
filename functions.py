from scipy import spatial
import numpy as np


def distance_metric(v1, v2):
    # return spatial.distance.cosine(v1, v2)
    return np.sum((v1 - v2) ** 2) ** 6

# def find_closest_for_vector(vector, n):
#     distances = []
#     for word, current_vect in d.items():
#         distances.append([distance_metric(vector, current_vect), word])
#     return sorted(distances)[:n]
#
#
# def find_closest_for_words(target_words, n, explicit=False):
#     vector = 0
#     for word in target_words:
#         vector += d[word]
#     vector /= len(target_words)
#     vector_word_pairs = find_closest_for_vector(vector, n)
# 
#     # parsing
#     if explicit:
#         return vector_word_pairs
#     found_words = np.array(vector_word_pairs)[:, 1]
#     filtered_words = [w for w in found_words if w not in target_words]
#     return ' '.join(filtered_words)


def find_closest_for_words_cumulative(target_words, n, explicit=False):
    distances = []
    for word, current_vect in d.items():
        distance = 0
        for target_word in target_words:
            distance += distance_metric(d[target_word], current_vect)
        distances.append([distance, word, ' '.join(target_words)])

    # parsing
    vector_word_pairs = sorted(distances)[:n]
    if explicit:
        return vector_word_pairs
    found_words = np.array(vector_word_pairs)[:, 1]
    filtered_words = [w for w in found_words if w not in target_words]
    return ' '.join(filtered_words)


def choose_n_elements_in_every_possible_way(list, n):
    max_mask = 2 ** len(list)
    for mask in range(max_mask):
        if bin(mask).count('1') != n:
            continue
        else:
            yield [list[i]
                   for i in range(len(list))
                   if (mask >> i) & 1]


def best_k_move(words, k, limit=40):
    words = words.split()
    results = []
    for combination in choose_n_elements_in_every_possible_way(words, k):
        results += find_closest_for_words_cumulative(combination, 20, explicit=True)
    return sorted(results)[:limit]




