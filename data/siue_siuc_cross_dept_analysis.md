# Cross-Department Analysis: SIUE and SIUC

## Source: Archive 3.zip (285.PNG = SIUE, 286.PNG = SIUC)

## SIUE Cross-Department Graph (285.PNG)
This graph shows ALL courses across ME, ECE, and CE at SIUE with prerequisite links.

### Root Nodes (no prerequisites):
- MATH 150 (Calculus I) — the single root for almost everything

### First-Level Branches from MATH 150:
- PHYS 141 (Physics I)
- MATH 152 (Calculus II)

### Second Level:
- PHYS 142 (Physics II) — from PHYS 141 + MATH 152
- MATH 250 (Calculus III) — from MATH 152

### Key Shared Courses (serve multiple departments):
| Course | Used By |
|--------|---------|
| MATH 150 → 152 → 250 → 305 | ME, ECE, CE (all) |
| PHYS 141/142 | ME, ECE, CE (all) |
| ECE/ME 210 (Circuits) | ME + ECE |
| CE/ME 240 (Statics) | ME + CE |
| CE/ME 242 (Mechanics of Solids) | ME + CE |
| MATH 305 (Diff Eq) | ME, ECE, CE (all) |

### Department-Specific Branches:
**ME Branch:** ME 262 → ME 350, ME 310 → ME 312, ME 315 → ME 410, ME 356 → ME 356L, ME 380 → ME 482 → ME 484
**ECE Branch:** ECE 211, ECE 282, ECE 326 → ECE 340 → ECE 341, ECE 351, ECE 365 → ECE 404 → ECE 405
**CE Branch:** CE 206, CE 330 → CE 330L, CE 315, CE 354, CE 342 → CE 348, CE 380 → CE 380D, CE 498

### Critical Shared Nodes (bottlenecks affecting all 3 departments):
1. **MATH 250** — gates CE/ME 240, ECE/ME 210, MATH 305
2. **CE/ME 240 (Statics)** — gates ME 262, CE/ME 242, CE 206
3. **CE/ME 242 (Mech. of Solids)** — gates ME 380, CE 330, CE 315, CE 354, CE 342, ME 370

## SIUC Cross-Department Graph (286.PNG)
Similar structure but with SIUC course numbering. Shows the same pattern of shared math/physics foundation branching into department-specific courses.

## Implications for UMSL
UMSL has all 3 programs (ME, EE, CE). The shared course structure should be similar:

### UMSL Shared Courses (estimated from current catalog):
| Course | ME | EE | CE | Notes |
|--------|----|----|----|----|
| MATH 1800-2020 (Calc sequence + DiffEq) | Yes | Yes | Yes | Foundation for all |
| PHYS 2111/2112 (Physics I & II) | Yes | Yes | Yes | Foundation for all |
| CHEM (Chemistry) | Yes | Maybe | Yes | Depends on CE curriculum |
| ENGR 1414 (Intro Design) | Yes | Yes | Yes | Shared first-year |
| ENGR 2310 (Statics) | Yes | No | Yes | ME + CE shared |
| ENGR 2320 (Dynamics) | Yes | No | Maybe | ME, possibly CE |
| ENGR 2332 (Mechanics of Materials) | Yes | No | Yes | ME + CE shared |
| EENG 2310 (Circuit Analysis) | Yes | Yes | No | ME + EE shared |
| CMP SCI 1250 (Computing) | Yes | Yes | Yes | Shared |
| ENGR 2022 (Eng Economics) | Yes | Yes | Yes | Shared |
| ENGR 2330 (Thermodynamics) | Yes | No | No | ME only |
| PHIL 2259 (Ethics) | Yes | Yes | Yes | Shared |
| ENGL 1100/3130 (Writing) | Yes | Yes | Yes | Shared |
