import math

# Example: Face-Centered Cubic (FCC) crystal
# Formula: APF = (Volume of atoms in unit cell) / (Volume of unit cell)

r = 0.125e-9  # atomic radius in meters (example)
atoms_per_cell = 4  # FCC has 4 atoms per unit cell

# Volume of atoms in unit cell (atoms_per_cell × volume of one sphere)
volume_atoms = atoms_per_cell * (4/3) * math.pi * (r ** 3)

# Volume of unit cell (for FCC: a = 2√2 * r)
a = 2 * math.sqrt(2) * r
volume_cell = a ** 3

apf = volume_atoms / volume_cell

print(f"Atomic Packing Factor (FCC) = {apf:.3f}")

import math

radius = 5e-9  # 5 nm particle
surface_area = 4 * math.pi * radius**2
volume = (4/3) * math.pi * radius**3
ratio = surface_area / volume

print(f"Surface Area-to-Volume Ratio = {ratio:.2e} 1/m")

import matplotlib.pyplot as plt

# Example data (strain vs stress)
strain = [0, 0.001, 0.002, 0.003, 0.004, 0.005]
stress = [0, 50, 100, 150, 200, 210]  # MPa

plt.plot(strain, stress, 'o-', label="Stress-Strain Curve")
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Simple Stress-Strain Curve")
plt.legend()
plt.grid(True)
plt.show()
