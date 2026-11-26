
import pyvista as pv
import numpy as np
from pathlib import Path

plots_dir = Path("plots")
plots_dir.mkdir(exist_ok=True)

# Read volume mesh
mesh = pv.read("data/air.vtu")

# 1. Temperature visualization
plotter = pv.Plotter(off_screen=True)

plotter.add_mesh(
    mesh,
    scalars="T",
    cmap="coolwarm",
    show_edges=False,
    scalar_bar_args={"title": "Temperature (K)"}
)

plotter.add_text("CFD Temperature Distribution")
plotter.camera_position = "iso"

plotter.screenshot(plots_dir / "temperature.png")
plotter.close()


# 2. Velocity magnitude
mesh["velocity_magnitude"] = np.linalg.norm(
    mesh.point_data["U"],
    axis=1
)

plotter = pv.Plotter(off_screen=True)

plotter.add_mesh(
    mesh,
    scalars="velocity_magnitude",
    cmap="viridis",
    show_edges=False,
    scalar_bar_args={"title": "Velocity Magnitude (m/s)"}
)

plotter.add_text("CFD Velocity Magnitude")
plotter.camera_position = "iso"

plotter.screenshot(plots_dir / "velocity.png")
plotter.close()

print("Plots saved successfully!")
