
import numpy as np
import matplotlib.pyplot as plt

from gnp_generator import dfs_connected_components, generate_GNP_graph



def experiment_vary_p():
    n = 10_000  # Large enough to see the transition
    repetitions = 5
    
    # Range of np values to test (centered around 1)
    np_values = np.linspace(0.5, 1.5, 21)
    p_values = np_values / n
    
    avg_largest = []
    avg_second = []
    std_largest = []
    
    print(f"Running Experiment 1: Varying p for n={n}...")
    for p in p_values:
        largest_sizes = []
        second_sizes = []
        
        for _ in range(repetitions):
            # 1. Generate Graph
            adj = generate_GNP_graph(n, p)
            # 2. Find Components
            comps = dfs_connected_components(adj, 1)
            
            largest_sizes.append(len(comps[0]))
            second_sizes.append(len(comps[1]))
            
        avg_largest.append(np.mean(largest_sizes))
        avg_second.append(np.mean(second_sizes))
        std_largest.append(np.std(largest_sizes))

    # --- Plotting Experiment 1 ---
    plt.figure(figsize=(10, 6))
    
    # Line 1: Largest with Error Bars
    plt.errorbar(np_values, avg_largest, yerr=std_largest, label='Largest Component', 
                 fmt='-o', capsize=5, color='royalblue')
    
    # Line 2: Second Largest
    plt.plot(np_values, avg_second, label='2nd Largest Component', 
             linestyle='--', color='darkorange')
    
    # Critical Threshold Reference
    plt.axvline(x=1, color='red', linestyle=':', label='Critical Threshold (np=1)')
    
    plt.title(f'Phase Transition in $G({n}, p)$ (Avg over {repetitions} runs)')
    plt.xlabel('Average Degree ($np$)')
    plt.ylabel('Component Size')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    plt.tight_layout()
    plt.savefig("FiguringOutNames.png")

# --- 3. Scaling Experiment (Varying n, Fixed Regime) ---
def experiment_vary_n():
    """
    Tests the scaling predictions (O(log n) vs O(n2/3) vs O(n))
    """
    n_values = [250, 500, 1000, 2000] # Adjust based on computation speed
    repetitions = 5
    
    # Define our regimes
    regimes = {
        'Subcritical (np=0.8)': 0.8,
        'Critical (np=1.0)': 1.0,
        'Supercritical (np=1.2)': 1.2
    }
    
    results = {regime: [] for regime in regimes}
    
    print(f"\nRunning Experiment 2: Varying n for Scaling Analysis...")
    for n in n_values:
        for regime, np_target in regimes.items():
            p = np_target / n
            largest_sizes = []
            
            for _ in range(repetitions):
                adj = generate_GNP_graph(n, p)
                comps = dfs_connected_components(adj, 1)
                largest_sizes.append(len(comps[0]))
            
            avg_size = np.mean(largest_sizes)
            results[regime].append(avg_size)

    # --- Plotting Experiment 2 (Log-Log) ---
    plt.figure(figsize=(10, 6))
    
    colors = {'Subcritical (np=0.8)': 'forestgreen', 
              'Critical (np=1.0)': 'purple', 
              'Supercritical (np=1.2)': 'crimson'}
    
    for regime, avg_sizes in results.items():
        plt.loglog(n_values, avg_sizes, label=regime, marker='s', color=colors[regime])
    
    # Add reference slopes for comparison
    # We use loglog so the power laws appear as straight lines
    n_ref = np.array(n_values)
    
    # Slope 1 (Linear O(n)) - Supercritical target
    plt.loglog(n_ref, n_ref * (avg_sizes[-1]/n_ref[-1]) * 0.8, 
               linestyle=':', color='black', alpha=0.5, label='Reference: Slope 1 (O(n))')
    
    # Slope 2/3 (O(n^2/3)) - Critical target
    plt.loglog(n_ref, n_ref**(2/3) * (results['Critical (np=1.0)'][-1]/(n_ref[-1]**(2/3))), 
               linestyle=':', color='gray', alpha=0.5, label='Reference: Slope 2/3 ($O(n^{2/3})$)')

    plt.title('Component Size Scaling across Regimes')
    plt.xlabel('Number of Nodes ($n$) (Log Scale)')
    plt.ylabel('Average Largest Component Size (Log Scale)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    plt.tight_layout()
    plt.savefig("dude.png")

def main():
    experiment_vary_p()
    experiment_vary_n()

if __name__ == "__main__":
    main()
