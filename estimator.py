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
    return max(len(neighbors) for neighbors in adj.values())

# ----------------------------------------------------
# Function that estimates the value of p(n,m). 
# 
# ----------------------------------------------------
def estimate_p(n, m, trials=200):
    count = 0
    for _ in range(trials):
        adj = generate_gnm_using_sampler(n, m)
        if max_degree(adj) <= 1:
            count += 1
    return count / trials





#Felipe was there B)




# --- APOTHEKE - old code

# # Function that creates the adjacency list for the graph G(n,m)
# # where 
# # - n :
# # - m : 

# def grid_graph_adj(n, m):
#     adj = {}
#     for i in range(n):
#         for j in range(m):
#             nbrs = []
#             if i > 0:       nbrs.append((i-1, j))
#             if i < n-1:     nbrs.append((i+1, j))
#             if j > 0:       nbrs.append((i, j-1))
#             if j < m-1:     nbrs.append((i, j+1))
#             adj[(i, j)] = nbrs
#     return adj

# # absolute cinema!!!
# def induced_subgraph(adj, nodes):
#     sub = {}
#     for u in nodes:
#         sub[u] = [v for v in adj[u] if v in nodes]
#     return sub

# # Function 
# # Input:
# # Output:
# #
# def estimator_p(n,m, k, experiments = 100):
#     S = [(i, j) for i in range(n) for j in range(m)] # UNIVERSE

#     full_adj = grid_graph_adj(n, m)  # CREATE ADJACENCY LIST 
#     suc = 0 # counter
    
#     for exp in range(experiments):
#         sampled_nodes = sampling_without_replacement(S, k, seed=exp) 
#         sub_adj = induced_subgraph(full_adj, sampled_nodes) 
#         if max_degree(sub_adj) == 1: 
#             #True
#             suc += 1 # counter for nodes with the degree we want
#     probability_n_m = suc/k
#     return probability_n_m
# Function that creates the adjacency list for the graph G(n,m)
# where 
# - n :
# - m : 

def grid_graph_adj(n, m):
    adj = {}
    for i in range(n):
        for j in range(m):
            nbrs = []
            if i > 0:       nbrs.append((i-1, j))
            if i < n-1:     nbrs.append((i+1, j))
            if j > 0:       nbrs.append((i, j-1))
            if j < m-1:     nbrs.append((i, j+1))
            adj[(i, j)] = nbrs
    return adj


# absolute cinema!!!
def induced_subgraph(adj, nodes):
    sub = {}
    for u in nodes:
        sub[u] = [v for v in adj[u] if v in nodes]
    return sub


# Function 
# Input:
# Output:
#
def estimator_p(n,m, k, experiments =100):
    S = [(i, j) for i in range(n) for j in range(m)] # UNIVERSE

    full_adj = grid_graph_adj(n, m)  # CREATE ADJACENCY LIST 
    suc = 0 # counter
    
    for exp in range(experiments):
        sampled_nodes = sampling_without_replacement(S, k, seed=exp) 
        sub_adj = induced_subgraph(full_adj, sampled_nodes) 
        if max_degree(sub_adj) == 1: 
            #True
            suc += 1 # counter for nodes with the degree we want
    probability_n_m = suc/k
    return probability_n_m

