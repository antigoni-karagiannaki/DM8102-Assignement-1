import random as rd 
import math
def draw_skip_distance(p):
    if(p == 0):
        return float("inf")
    if(p == 1):
        return 1
    
    u = rd.random()
    jump_val = math.ceil((math.log(1-u)-1)/math.log(1-p))
    return jump_val
    
def append_edge(E,i,j):
    
    if(i == j):
       return E;

    if(i+1 not in E.keys()):
        E[i+1]=[j+1,]
    else:
        E[i+1].append(j+1)
    if(j+1 not in E.keys()):
       E[j+1]=[i+1,]
    else:
        E[j+1].append(i+1)
    return E

def generate_graph(n, p):
    E = {}

    k = -1
    while True:
        
        l = draw_skip_distance(p)
        if (l == float("inf")):
            return;
        k = k+l+1
        if k < n*n: #(n *(n-1))//2
            i,j = math.floor(k/n),k%n
            print(f"{i+1} and {j+1}")
            E = append_edge(E,i,j) # Adjacency Matrix doesnt scale up well
        else:
            return E

print(generate_graph(3,0.5))
