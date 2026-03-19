
import random 
import numpy as np
import matplotlib.pyplot as plt

def sampling_without_replacement(S, k , seed ):
    
    if seed  != None:
        random.seed(seed)

    """
    Universe S = all nodes of the grid graph G(n,m)
    Returns k randomly selected distinct nodes.
    """
    R = []
    while len(R) < k:
        x = random.randint(0, len(S)-1) #indeces
    
        if x not in R:
            R.append(x)
    
    result  = [S[i] for i in R]
    return result


# ----------------------------------------------------
# Function that used the sampling w/o replacement to 
# generate a G(n,m) Graph & returns its adjacency list
# n - number of nodes
# m - number of edges
# seed - num to rerun exact experiment
# ----------------------------------------------------
def generate_gnm_using_sampler(n, m, seed=None):
    # Universe of all possible edges
    S = [(u, v) for u in range(n) for v in range(u+1, n)]

    # Sample m edges using your function
    sampled_edges = sampling_without_replacement(S, m, seed)

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in sampled_edges:
        adj[u].append(v)
        adj[v].append(u)

    return adj   

# Function that plots the degree distribution of a G(n,m) graph.
def degree_distribution(n, m, k=200):
    degree_counts = {}

    for _ in range(k):
        G = generate_gnm_using_sampler(n, m)
        degrees = [len(neighbors) for neighbors in G]

        for d in degrees:
            degree_counts[d] = degree_counts.get(d, 0) + 1

    xs = sorted(degree_counts.keys())
    ys = [degree_counts[x] for x in xs]

    plt.figure()
    plt.bar(xs, ys)
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.title(f"Degree distribution in G({n},{m})")
    plt.show()


def main(): 
    # Example universe S : list of grid nodes
    S = [ (i,j)for i in range(3) for j in range(4)] # G(3,4)
    k = 5 
    result = sampling_without_replacement(S,k,10)
    print("Sampled nodes:",result)

    n=100  # number of nodes
    m=200  # number of edges
    adj = generate_gnm_using_sampler(n, m, seed=42)
    print("Adjacency list of G(n,m):")
        
    degree_distribution(n, m)



if __name__ == "__main__":
    main()
