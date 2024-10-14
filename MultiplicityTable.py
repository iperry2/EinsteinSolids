import math

def multiplicity(N, q):
    return math.comb(q + N - 1, q)

N_A = 3
N_B = 3
total_energy = 6  # total energy units

# Prepare a list to store the rows of the table
table_data = []

# Iterate over all possible values of qA and qB
for q_A in range(total_energy + 1):
    q_B = total_energy - q_A  # Since qA + qB must equal total_energy
    omega_A = multiplicity(N_A, q_A)
    omega_B = multiplicity(N_B, q_B)
    omega_total = omega_A * omega_B
    table_data.append((q_A, omega_A, q_B, omega_B, omega_total))

# Print the table header
print(f"{'qA':<5} {'ΩA':<10} {'qB':<5} {'ΩB':<10} {'Ω_total':<10}")
print("="*50)

# Print each row of the table
for q_A, omega_A, q_B, omega_B, omega_total in table_data:
    print(f"{q_A:<5} {omega_A:<10} {q_B:<5} {omega_B:<10} {omega_total:<10}")

# Calculate and print the total multiplicities
total_multiplicity = sum(omega_total for _, _, _, _, omega_total in table_data)
print(f"\nTotal Multiplicity: {total_multiplicity}")
