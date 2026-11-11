"""Minimal example generating a watertight M4 bracket with FoxCAD Manifold3D utilities."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from foxcad_manifold_utils import (
    elephant_foot_chamfer_box,
    compensated_hole,
    teardrop_hole,
    manifold_to_trimesh,
    certify_mesh,
)

def main():
    box = elephant_foot_chamfer_box(50, 35, 20, chamfer=0.5)
    part = (
        box
        - compensated_hole(4.0, depth=30)
        - teardrop_hole(3.0, length=60).translate([0, 0, 10])
    )
    mesh = manifold_to_trimesh(part)
    stats = certify_mesh(mesh)
    print("Certification telemetry:", stats)
    mesh.export("certified_bracket.stl")

if __name__ == "__main__":
    main()
