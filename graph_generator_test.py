import unittest

from main import sampling_without_replacement
from measurement_tools import binomial_check
seed_val = 10

class TestGraphGenerator(unittest.TestCase):
    """
    The following function wheter a small sized stream is validated by the algorithm reservoir sampling
    """
    def test_small_stream_size(self,):
        S = [(0,1),(0,2)] # G(2,2)
        k = 1 #reservoir capacity
        sample = sampling_without_replacement(S,k,seed_val)
        self.assertTrue(sample == [(0,1)] or sample == [(0,2)]) 
        
    def test_repeated_elements_in_reservoir(self,):
        S = [(0,1),(0,3),(0,3)] # G(2,2)
        k = 2
        sample = sampling_without_replacement(S,k,seed_val)
        self.assertFalse(sample == [(0,3),(0,3)],"Test if there's repeated elements in the reservoir") 


    def test_reservoir_occurence_statistical(self):
        # n : nb of elements in the stream, k : capacity of the reservoir and number of iterations which will run
        n, k, iterations = 10, 3, 20000
        
        chosen_index = 0
        S = [(i, j) for i in range(n) for j in range(i + 1, n)] # Generates a list of edges without self loops and repetions
        
        appearing_count = 0

        sample = []
       
        sample = sampling_without_replacement(S, k,seed_val)
        chosen_sample = sample[chosen_index]
    
        for _ in range(iterations):
            sample = sampling_without_replacement(S, k,None) #counting appearences
            if chosen_sample in sample:
                appearing_count+=1
        self.assertTrue(binomial_check(appearing_count,iterations,k/len(S)),"Testing uniform occurency rate of the chosen element")

if __name__ == '__main__':
    
    unittest.main()
