import numpy as np

def vose_alias(p, size):
    d = len(p)
    probability = np.zeros(d)
    alias = np.zeros(d, dtype = np.ulonglong) #maybe another integer type?
    average = 1.0 / d

    # copy p as we will make changes to it
    probs = np.copy(p)

    small = []
    large = []

    # build alias table
    for i in range(d):
        if probs[i] >= average:
            large.append(i)
        else:
            small.append(i)
    while len(small) > 0 and len(large) > 0:
        less = small.pop()
        more = large.pop()
        probability[less] = probs[less] * d
        alias[less] = more
        probs[more] = (probs[more] + probs[less]) - average

        if probs[more] >= average:
            large.append(more)
        else:
            small.append(more)
    while len(small) > 0:
        less = small.pop()
        probability[less] = 1.0
    while len(large) > 0:                    
        more = large.pop()
        probability[more] = 1.0

    # sample from alias table
    columns = np.random.randint(0, (len(probability) - 1), size = size)
    uniform_samples = np.random.random_sample(size)
    coin_tosses = uniform_samples < probability[columns]
    idx = np.where(coin_tosses == True, np.array(columns, dtype = int), np.array((alias[columns]), dtype = int))
    return idx
