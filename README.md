# PyVista CFD Data Exploration

This project explores CFD mesh data using **PyVista and NumPy**. The main goal was to understand how mesh data is stored, visualize physical fields and extract data for future machine learning applications.

## VTK, VTP and VTU

VTK is a file format family used to store and work with scientific data, including 3D meshes.

- **`.vtp` (VTK PolyData):** Stores surface-based geometry, such as the surfaces of electronic components.
- **`.vtu` (VTK Unstructured Grid):** Stores volume meshes, such as the surrounding air domain in a CFD simulation.

In this project, `structure.vtp` represents the component surfaces, while `air.vtu` represents the surrounding cooling air.

## Points, Cells and Connectivity

A mesh is mainly made up of points and cells.

- **Points:** Define the locations of the mesh in 3D space using X, Y and Z coordinates.
- **Cells:** Connect these points to form elements such as triangles, quadrilaterals and tetrahedra.
- **Connectivity:** Describes which points belong to each cell. It defines how the mesh is connected.

## Point Data vs Cell Data

- **Point Data:** Values are stored at individual mesh points, such as temperature or velocity at each point.
- **Cell Data:** Values are stored for each mesh cell, representing the corresponding element.

Cell data can be converted to point data using PyVista when needed.

## What I Did

- Loaded and inspected `.vtp` and `.vtu` files using PyVista.
- Explored mesh properties, arrays and data associations.
- Visualized temperature and velocity magnitude.
- Created slice and clip views.
- Compared point data and cell data.
- Extracted coordinates and physical fields into NumPy arrays.
- Saved and reloaded the extracted data using `.npz` format.

## Tools Used

- Python
- PyVista
- NumPy
- Matplotlib

