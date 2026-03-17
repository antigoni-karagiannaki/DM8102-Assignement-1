import math

"""
Home made binomial check in order to avoid installing scipy in order to use a single function
Keyword arguments:
success -- number of times a certain edge appeared in the reservoir during n trials
p -- probability of an edge being in the reservoir

Return: wheter the trials produced a element with the correct probability
"""


def binomial_check(successes, trials, p):
    mean = trials * p
    std_dev = math.sqrt(trials * p * (1 - p))

    z_score = abs(successes - mean) / std_dev
        
    #P(z_score < 3) is roughly p_value < 0.003
    return z_score < 3.0 

