import numpy as np


with open('/home/filipesku/dane/polish_corpus/d42200w500d.sspace') as file:
    file.readline() # first line is metadata

    # parsing to python dictionary
    d = {}

    for line in file:
        word, raw_text_vector = line.split('|')
        text_vector = raw_text_vector.split()
        vector = np.array(list(map(float, text_vector)))
        normalized_vector = vector / np.sum(vector ** 2) ** (1/2)
        d.update({word: normalized_vector})
