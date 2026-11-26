import pyvista as pv
import numpy as np
from pathlib import Path


def load_case(path):

    # Read simulation mesh
    mesh = pv.read(path)

    # Extract point coordinates
    coords = mesh.points

    # Create dictionary
    data = {
        "coords": coords
    }

    # Extract every point-based field
    for name, array in mesh.point_data.items():
        data[name] = np.asarray(array)

    return data


# Load simulation
data = load_case("data/air.vtu")

# Inspect extracted arrays
for name, array in data.items():
    print(name, array.shape)


Path("outputs").mkdir(exist_ok=True)

# Save all arrays
np.savez_compressed(
    "outputs/air_data.npz",
    **data)

# Reload
loaded = np.load("outputs/air_data.npz")

# Compare shapes
for name in data:
    print(
        name,
        "Original:", data[name].shape,
        "Reloaded:", loaded[name].shape
    )

    assert np.array_equal(data[name], loaded[name])

print("All arrays match!")