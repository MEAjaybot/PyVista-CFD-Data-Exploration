
import pyvista as pv

# Read surface mesh
mesh = pv.read("data/structure.vtp")

print("Before conversion")
print("Point arrays:", mesh.point_data.keys())
print("Cell arrays:", mesh.cell_data.keys())

# Convert cell data to point data
converted = mesh.cell_data_to_point_data()

print("\nAfter conversion")
print("Point arrays:", converted.point_data.keys())
print("Cell arrays:", converted.cell_data.keys())

# Compare temperature
print("\nOriginal cell temperature:",
      mesh.cell_data["T"].shape)

print("Converted point temperature:",
      converted.point_data["T"].shape)

# Visualize converted temperature
converted.plot(
    scalars="T",
    cmap="coolwarm"
)