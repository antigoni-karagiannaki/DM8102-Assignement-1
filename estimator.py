from main import sampling_without_replacement
import random

from main import generate_gnm_using_sampler
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# Empirically approximate p(n,m). 
# To this end, sample k ≥ 100 graphs from G(n,m) and
# inspect how many of them have maximum degree 1.

# ----------------------------------------------------
# Function that searches through the adjacency list &
# finds the node with the maximum degree
# ----------------------------------------------------
def max_degree(adj):
    return max(len(neighbors) for neighbors in adj)

# ----------------------------------------------------
# Function that estimates the value of p(n,m). 
# 
# ----------------------------------------------------
def estimate_p(n, m, trials=200):
    count = 0
    for _ in range(trials):
        print(f"Trial {_+1}/{trials}")
        adj = generate_gnm_using_sampler(n, m)
        print(f"Max degree in this graph: {max_degree(adj)}")
        if max_degree(adj) <= 1:
            count += 1
    return count / trials

# Function that plots p(n,m) as m grows, for a fixed n.
def plot_p_vs_m(n, m_values, trials=200):
    probs = []

    for m in m_values:
        p = estimate_p(n, m, trials)
        probs.append(p)

    plt.figure()
    plt.plot(m_values, probs, marker='o')
    plt.xlabel("m (number of edges)")
    plt.ylabel("Estimated p(n,m)")
    plt.title(f"Probability max degree ≤ 1 for G({n},m)")
    plt.show()


# main function to run the estimation
if __name__ == "__main__":
    n = 10000  # Large value of n
    trials = 10  # Number of trials for estimation

    # m = o (\sqrt(n))
    m_small = int(np.sqrt(n) / 2)
    # p_small = estimate_p(n, m_small, trials)  
      
    # print(f"Estimated p(n, m) for m = o(sqrt(n)): {p_small:.4f}")
    plot_p_vs_m(n, [m_small, int(np.sqrt(n)), int(2 * np.sqrt(n))], trials)


