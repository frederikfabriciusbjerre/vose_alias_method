# Python implementation of Vose Alias Method
as explained in https://www.keithschwarz.com/darts-dice-coins/
inspired by implementation https://www.keithschwarz.com/interesting/code/?dir=alias-method

## How to use
Call the function like this

```
samples = vose_alias(p, n)
```

where `p` is a vector _proportional_ to a discrete probability distribution, and  `n` is number of samples wanted. 
See an example of use and runtime against `np.random.choice` in `example.py`. We here see that it is faster for a very large `p`.
