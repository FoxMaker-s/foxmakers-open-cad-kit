# FoxCAD Manifold3D Additive Engineering Kit

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](./LICENSE)
[![Topology: 2-Manifold Watertight](https://img.shields.io/badge/Topology-100%25%20Watertight%202--Manifold-emerald.svg)](https://hub.foxmakers.it/foxcad/info)
[![Wikidata](https://img.shields.io/badge/Wikidata-Q142094985-blue.svg)](https://www.wikidata.org/wiki/Q142094985)

Open-source parametric **Additive Manufacturing CSG utility library** and **8 slicer-certified 3D printable workshop tools**, engineered with Emmett Lalish's [`manifold3d`](https://github.com/elalish/manifold) kernel and verified 100% watertight with `trimesh`.

Built by **[FoxMakers](https://www.foxmakers.it)** — Europe's distributed 3D printing hub, spare parts store, and neural browser CAD studio (**[FoxCAD Studio AI](https://hub.foxmakers.it/foxcad/info)**).

---

## Features Included in `foxcad_manifold_utils.py`

1. **`compensated_hole(dia_nominal, depth, fn, fit)`** — Applies Chordal Inscribed Radius Compensation ($R_{CAD} = \frac{R}{\cos(\pi/N)} + \text{clearance}$) so M3–M10 screws never bind in polygonal STL holes.
2. **`teardrop_hole(radius_nominal, length)`** — Self-supporting $45^\circ$ horizontal bore cross-section for zero-droop horizontal holes without support material.
3. **`elephant_foot_chamfer_box(width, length, height, chamfer)`** — $45^\circ \times 0.5\text{ mm}$ perimeter chamfer on $Z=0$ to absorb first-layer squish.
4. **`countersunk_hole(dia_screw, head_dia, total_depth)`** — DIN 7991 $90^\circ$ countersink pocket with sub-flush clearance.
5. **`certify_mesh(mesh)`** — Validates `is_watertight`, `is_winding_consistent`, Euler characteristic, volume ($\text{cm}^3$), and bounding extents ($\text{mm}$).

---

## Included Certified 2-Manifold STL Models (`/models`)

All 8 STL utilities are also available with studio previews on the **[FoxMakers Free 3D Models Vault](https://www.foxmakers.it/modelli-3d-gratuiti/)**:

| Model | Dimensions (mm) | Volume | Watertight |
| :--- | :---: | :---: | :---: |
| `FoxMakers_AMS_Universal_Spool_Adapter.stl` | 205 × 205 × 12 | 37.16 cm³ | Verified |
| `FoxMakers_FastSwap_Nozzle_Caddy.stl` | 74 × 44 × 15 | 42.48 cm³ | Verified |
| `FoxMakers_AntiScratch_PEI_Bed_Scraper.stl` | 48 × 108 × 9 | 22.54 cm³ | Verified |
| `FoxMakers_Precision_Calibration_Matrix.stl` | 36 × 36 × 24 | 8.73 cm³ | Verified |
| `FoxMakers_PTFE_Tube_Cutter_Jig.stl` | 38 × 18 × 16 | 8.45 cm³ | Verified |
| `FoxMakers_TPU_Vibration_Damper_Foot.stl` | 46 × 46 × 22 | 20.43 cm³ | Verified |
| `FoxMakers_Universal_Filament_Clip.stl` | 29 × 22 × 6 | 3.15 cm³ | Verified |
| `FoxMakers_Hex_Wrench_Bit_Stand.stl` | 60 × 34 × 24 | 32.24 cm³ | Verified |

---

## Quick Example

```python
from foxcad_manifold_utils import (
    elephant_foot_chamfer_box,
    compensated_hole,
    teardrop_hole,
    manifold_to_trimesh,
    certify_mesh,
)

box = elephant_foot_chamfer_box(50, 35, 20, chamfer=0.5)
part = box - compensated_hole(4.0, depth=30) - teardrop_hole(3.0, length=60).translate([0, 0, 10])

mesh = manifold_to_trimesh(part)
print(certify_mesh(mesh))
mesh.export("certified_bracket.stl")
```

---

## Official FoxMakers Resources
- **GitHub Repository**: https://github.com/FoxMaker-s/foxmakers-open-cad-kit
- **Embeddable STL Repair Widget (Free Iframe)**: https://hub.foxmakers.it/embed/tools/stl-repair
- **Free Online STL Repair (2-Manifold Watertight, Zero Login)**: https://hub.foxmakers.it/en/tools/stl-repair (Italiano: https://hub.foxmakers.it/tools/ripara-stl)
- **Free Online STL to STEP Converter (OpenCASCADE ISO 10303-21 AP214)**: https://hub.foxmakers.it/en/tools/stl-to-step (Italiano: https://hub.foxmakers.it/tools/stl-to-step)
- **Free 3MF & OBJ to STL Converter**: https://hub.foxmakers.it/en/tools/obj-3mf-to-stl
- **3D Printer Spare Parts Finder (3,800+ parts)**: https://www.foxmakers.it/trova-ricambi-stampanti-3d/
- **FoxCAD AI Web CAD Studio (STL / 3MF / STEP ISO 10303 / GLB)**: https://hub.foxmakers.it/foxcad/info
- **Global Distributed 3D Printing & Maker Network**: https://hub.foxmakers.it/makers
- **Official Free Certified 3D Models**: https://www.foxmakers.it/modelli-3d-gratuiti/
- **Wikidata Knowledge Graph Entity**: https://www.wikidata.org/wiki/Q142094985
