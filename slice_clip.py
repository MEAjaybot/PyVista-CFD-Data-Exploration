
import pyvista as pv
from pathlib import Path

mesh = pv.read("data/air.vtu")

Path("plots").mkdir(exist_ok=True)

# Slice through the middle along the X direction
center_x = (mesh.bounds[0] + mesh.bounds[1]) / 2

sliced = mesh.slice(
    normal="x",
    origin=(center_x, 0, 0)
)

print("Slice points:", sliced.n_points)
print("Slice cells:", sliced.n_cells)

sliced.plot(
    scalars="U",
    cmap="coolwarm",
    show_edges=False,
    screenshot="plots/temperature_slice.png"
)
# Clip the mesh through the middle
clipped = mesh.clip(
    normal="x",
    origin=(center_x, 0, 0)
)

print("Clipped points:", clipped.n_points)
print("Clipped cells:", clipped.n_cells)

clipped.plot(
    scalars="U",
    cmap="coolwarm",
    show_edges=False,
    screenshot="plots/temperature_clipped.png"
)