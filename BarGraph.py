import math
import matplotlib.pyplot as plt

# Function to calculate the multiplicity
def multiplicity(N, q):
    return math.comb(q + N - 1, q)

# Define parameters for the two scenarios
q_total = 6  # Total energy units
scenarios = [
    {'NA': 3, 'NB': 3},  # Scenario 1: 3 oscillators in each solid
    {'NA': 6, 'NB': 4}   # Scenario 2: 6 oscillators in solid A, 4 in solid B
]

# Function to calculate and plot macrostates for a given scenario
def plot_macrostates(NA, NB, q_total):
    macrostates = []
    probabilities = []

    total_microstates = 0
    for qA in range(q_total + 1):  # Iterate over all possible qA (0 to q_total)
        qB = q_total - qA          # Remaining energy in solid B
        microstates_A = multiplicity(NA, qA)
        microstates_B = multiplicity(NB, qB)
        total_states = microstates_A * microstates_B  # Total states for this macrostate
        macrostates.append((qA, qB))
        probabilities.append(total_states)
        total_microstates += total_states

    # Normalize probabilities
    probabilities = [p / total_microstates for p in probabilities]

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.bar([str(m) for m in macrostates], probabilities, color='skyblue')
    plt.xlabel('Macrostates (qA, qB)')
    plt.ylabel('Probability')
    plt.title(f'Macrostates and Probabilities for N_A = {NA}, N_B = {NB}, q_total = {q_total}')
    plt.show()

    # Print most and least probable macrostates
    max_prob = max(probabilities)
    min_prob = min(probabilities)
    max_macrostate = macrostates[probabilities.index(max_prob)]
    min_macrostate = macrostates[probabilities.index(min_prob)]
    print(f'Most probable macrostate: {max_macrostate} with probability {max_prob:.4f}')
    print(f'Least probable macrostate: {min_macrostate} with probability {min_prob:.4f}')

# Run the function for both scenarios
for scenario in scenarios:
    print(f"\nScenario: N_A = {scenario['NA']}, N_B = {scenario['NB']}")
    plot_macrostates(scenario['NA'], scenario['NB'], q_total)
