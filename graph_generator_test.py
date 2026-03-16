import unittest
from main import sampling_without_replacement
import random

from tools import binomial_check
seed_val = 10
random.seed(seed_val)
class TestGraphGenerator(unittest.TestCase):

    def test_sampling_wo_replacement_smallstream(self,):
        S = [(0,1),(0,2)] # G(2,2)
        k = 1
        Sprime = sampling_without_replacement(S,k,seed_val)
        self.assertTrue(Sprime == [(0,1)] or Sprime == [(0,2)])
    
    def test_reservoir_statistical(self):
        #n -nb of elements in the stream, k -capacity of the reservoir and iteration nb
        n, k, iterations = 10, 3, 20000
        
        chosen_index = 0
        
        S = [ (i,j) for i in range(n) for j in range(n)] #(0,1) = (1,0) are different in python so not considered
        appearing_count = 0
        sample = []
        
        for _ in range(1):
            sample = sampling_without_replacement(S, k,seed_val)
            chosen_sample = sample[chosen_index]
        
        for _ in range(iterations):
            sample = sampling_without_replacement(S, k,seed_val)
            if chosen_sample in sample:
                appearing_count+=1
        binomial_check(appearing_count,n,k/n)
        


if __name__ == '__main__':
    unittest.main()
