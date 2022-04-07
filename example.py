import numpy as np
import time
from src.vose_alias import vose_alias

# create probabilities
p_len = 100000 # length of probability vector
p = np.random.random_sample(p_len)
p_norm = p/np.sum(p)

# number of samples
n = 100000000

# sample from alias
start = time.time()
a = vose_alias(p_norm, n)
end = time.time()
t1 = end - start

# sample with np.random.choice
start = time.time()
b = np.random.choice(len(p), n, p = p_norm)
end = time.time()
t2 = end - start

# print executing times
print(t1)
print(t2)
