
import pyvista as pv
import numpy as np
from pyvista import examples
from pathlib import Path
import shutil

# Download the files without loading them as a combined dataset
file_paths = examples.download_electronics_cooling(load=False)

# Copy the downloaded files into our project
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

meshes = {}

for file_path in file_paths:
    source = Path(file_path)
    destination = data_dir / source.name
    shutil.copy2(source, destination)

    # Read the VTK file
    mesh = pv.read(destination)

    meshes[source.suffix] = mesh

    print("\n" + "=" * 50)
    print("FILE:", source.name)
    print("TYPE:", type(mesh))
    print("POINTS:", mesh.n_points)
    print("CELLS:", mesh.n_cells)
    print("BOUNDS:", mesh.bounds)
    print("ARRAY NAMES:", mesh.array_names)

    # Inspect point data
    for name, array in mesh.point_data.items():
        values = np.asarray(array)
        print(
            f"Point | {name} | Shape: {values.shape} "
            f"| Min: {np.nanmin(values):.5f} "
            f"| Max: {np.nanmax(values):.5f}"
        )

    # Inspect cell data
    for name, array in mesh.cell_data.items():
        values = np.asarray(array)
        print(
            f"Cell  | {name} | Shape: {values.shape} "
            f"| Min: {np.nanmin(values):.5f} "
            f"| Max: {np.nanmax(values):.5f}"
        )