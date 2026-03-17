
import random 

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


def main(): 
    # Example universe S : list of grid nodes
    S = [ (i,j)for i in range(3) for j in range(4)] # G(3,4)
    k = 5 
    result = sampling_without_replacement(S,k,10)
    print("Sampled nodes:",result)

if __name__ == "__main__":
    main()
