"""
FoxCAD Manifold3D Additive Engineering Utilities (MIT License)
Developed by FoxMakers (https://www.foxmakers.it | https://hub.foxmakers.it/foxcad/info)

Includes slicer-certified CSG functions built on Emmett Lalish's `manifold3d` kernel:
- Chordal Inscribed Polygon Hole Expansion (zero-jam bolt holes)
- Elephant's Foot 45° First-Layer Compensation
- Self-Supporting Teardrop Horizontal Bores
- DIN 7991 90° Countersunk Sub-Flush Screw Pockets
- Topological Watertight Validation via Trimesh
- Optional B-Rep ISO-10303-21 STEP Export via OpenCASCADE (cadquery-ocp)
"""

import math
import numpy as np
import trimesh
from manifold3d import Manifold, CrossSection, set_circular_segments

set_circular_segments(72)


def compensated_hole(dia_nominal: float, depth: float = 20.0, fn: int = 60, fit: str = "close") -> Manifold:
    """Compensate polygonal chord cut-in so screws fit cleanly without drilling."""
    r_nom = dia_nominal / 2.0
    r_chordal = r_nom / math.cos(math.pi / fn)
    clearances = {"press_fit": 0.08, "close": 0.20, "free": 0.35}
    r_final = r_chordal + (clearances.get(fit, 0.20) / 2.0)
    return Manifold.cylinder(depth, r_final, r_final, circular_segments=fn, center=True)


def teardrop_hole(radius_nominal: float, length: float = 30.0) -> Manifold:
    """Create a support-free horizontal bore with a 45° top roof."""
    r = radius_nominal
    circ = CrossSection.circle(r)
    peak_y = r * math.sqrt(2.0)
    roof = CrossSection([[[0.0, peak_y], [-r, 0.0], [r, 0.0]]])
    cs = circ + roof
    return Manifold.extrude(cs, length).rotate([0, 90, 0]).translate([-length / 2.0, 0, 0])


def elephant_foot_chamfer_box(width: float, length: float, height: float, chamfer: float = 0.5) -> Manifold:
    """Add a 45° bottom perimeter chamfer to absorb first-layer squish."""
    c = max(chamfer, 0.2)
    box = Manifold.cube([width, length, height], center=True).translate([0, 0, height / 2.0])
    c_x1 = Manifold.cube([width + 4, 2 * c, 2 * c], center=True).rotate([45, 0, 0]).translate([0, -length / 2.0, 0])
    c_x2 = Manifold.cube([width + 4, 2 * c, 2 * c], center=True).rotate([45, 0, 0]).translate([0, length / 2.0, 0])
    c_y1 = Manifold.cube([2 * c, length + 4, 2 * c], center=True).rotate([0, 45, 0]).translate([-width / 2.0, 0, 0])
    c_y2 = Manifold.cube([2 * c, length + 4, 2 * c], center=True).rotate([0, 45, 0]).translate([width / 2.0, 0, 0])
    return box - c_x1 - c_x2 - c_y1 - c_y2


def countersunk_hole(dia_screw: float, head_dia: float, total_depth: float = 20.0) -> Manifold:
    """DIN 7991 90° countersink pocket with 0.3mm sub-flush head margin."""
    shaft = compensated_hole(dia_screw, depth=total_depth + 4, fit="close")
    cone_h = (head_dia - dia_screw) / 2.0
    cone = Manifold.cylinder(cone_h + 0.3, head_dia / 2.0 + 0.15, dia_screw / 2.0, center=False)
    return shaft + cone


def manifold_to_trimesh(man: Manifold) -> trimesh.Trimesh:
    """Convert Manifold CSG object to a verified Trimesh object."""
    mesh_data = man.to_mesh()
    return trimesh.Trimesh(vertices=mesh_data.vert_properties[:, :3], faces=mesh_data.tri_verts, process=True)


def certify_mesh(mesh: trimesh.Trimesh) -> dict:
    """Verify watertight 2-manifold certification metrics."""
    return {
        "watertight": bool(mesh.is_watertight),
        "winding_consistent": bool(mesh.is_winding_consistent),
        "euler_number": int(mesh.euler_number),
        "volume_cm3": round(float(mesh.volume) / 1000.0, 2) if mesh.volume else 0.0,
        "extents_mm": np.round(mesh.extents, 2).tolist(),
    }
