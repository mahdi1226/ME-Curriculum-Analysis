# ME Program Curriculum Analysis & Course Dependency Graph

An interactive web-based tool for analyzing and comparing Mechanical Engineering curricula across universities, with ABET compliance mapping, prerequisite dependency visualization, and AI-era curriculum recommendations.

**Built for:** Benchmarking a proposed UMSL (University of Missouri - St. Louis) ME program against peer institutions.

## Live Pages

Open `index.html` in any browser — no server required (D3.js loaded via CDN).

| Page | Description |
|------|-------------|
| **[Course Graph](index.html)** | Interactive prerequisite dependency graph. Click any course to see its syllabus, ABET mapping, prerequisites, and post-requisites. Switch between UMSL, Missouri S&T, SIUE, and SLU. |
| **[ABET Audit](abet.html)** | Credit hour audit, Student Outcome mapping, gap analysis, and accreditation timeline |
| **[AI & Ethics](ai-policy.html)** | ABET's AI policy, course-by-course AI integration plan, ethics in the AI era |
| **[DEEP Analysis](deep-analysis.html)** | Critical path analysis based on the DEEP project (Busch-Vishniac et al., 2011), bottleneck identification, flexibility recommendations |
| **[Syllabus Templates](syllabi.html)** | Expandable syllabi for every course with ABET outcome mapping, topic hours, cross-school equivalents |
| **[Cross-Department](cross-dept.html)** | Shared courses between ME, EE, and CE programs with resource implications |
| **[Proposed Curriculum](proposed-curriculum.html)** | Revised 4-year plan fixing ABET gaps (mechanisms, vibrations, elective flexibility) |

## Gephi Files

The `gephi/` directory contains `.gexf` files for all four schools, importable into [Gephi](https://gephi.org/) for network analysis:

- `umsl_me.gexf` — UMSL (42 nodes, 38 edges)
- `mst_me.gexf` — Missouri S&T (44 nodes, 64 edges)
- `siue_me.gexf` — SIUE (44 nodes, 52 edges)
- `slu_me.gexf` — SLU (42 nodes, 34 edges)
- `washu_me.gexf` — WashU/McKelvey (36 nodes, 42 edges)

Node attributes: `name`, `credits`, `category`, `semester`, `year`, `season`
Edge attributes: `type` (prerequisite / corequisite)

## Schools Compared

| School | Type | Total Credits | ME Courses | Prereq Edges |
|--------|------|---------------|------------|-------------|
| **UMSL** | Public (UM System) | 125 | 42 | 39 |
| **Missouri S&T** | Public (UM System) | 128 | 46 | 61 |
| **SIUE** | Public (SIU System) | 129 | 41 | 41 |
| **SLU** | Private (Jesuit) | 129 | 43 | 34 |
| **WashU** | Private (McKelvey) | 120 | 46 | 44 |

## Key Findings

### ABET Gaps in Current UMSL Program
1. **No Kinematics/Dynamics of Mechanisms course** — required by ABET ME program criteria
2. **No Vibrations course** — part of ABET "mechanical systems" breadth
3. **Zero technical elective flexibility** — all upper-division courses are fixed (peers offer 9-12 credits of choice)

### Critical Path Analysis
- UMSL's longest prerequisite chain: 7-8 courses (Calc I → ... → CFD/Capstone)
- Year 2 Spring is the critical bottleneck semester (4 gateway courses)
- Missouri S&T has nearly 2x the prerequisite edges of SLU (64 vs 34)

### AI-Era Recommendations
- Update ethics course with AI liability, algorithmic bias, autonomous systems
- Modernize computing course to Python + data science + ML concepts
- Add AI/ML content to manufacturing, CFD, and controls courses

## Course Graph Color Legend

| Color | Category | Description |
|-------|----------|-------------|
| Orange | Mathematics | Calculus I-III, Differential Equations, Statistics |
| Purple | Physics | Physics I (Mechanics), Physics II (E&M) |
| Green | Chemistry | General Chemistry for Engineering |
| Blue | Engineering Core | Statics, Dynamics, Mechanics of Materials, Thermodynamics |
| Red/Coral | ME Core | Fluids, Heat Transfer, Controls, Machine Design, Materials, Instrumentation |
| Pink | ME Advanced/Elective | Composites, CFD, Renewable Energy, Advanced Manufacturing |
| Light Blue | Electrical/CS | Circuit Analysis, Intro to Computing |
| Gray | General Education | English, Ethics, History, Humanities, Social Sciences |
| Gold/Yellow | Capstone/Design | Senior Design I & II |

**Line styles:** Solid lines = prerequisites, Dashed lines = co-requisites

## Research Foundation

This analysis draws on:
- **DEEP Project** — Busch-Vishniac et al. (2011), "Deconstructing Engineering Education Programmes," *European J. of Engineering Education*, 36(3), 269-283
- **CPN Analysis** — Yang, Gharebhaygloo et al. (2025), "Analysis of Student Progression Through Curricular Networks," *Electronics*, 14, 3016
- **ABET EAC Criteria** (2025-2026) for Mechanical and Similarly Named Engineering Programs

## Data Sources

All curriculum data was collected from official university catalogs (2025-2026):
- [Missouri S&T Catalog](https://catalog.mst.edu/)
- [SIUE Catalog](https://www.siue.edu/academics/undergraduate/)
- [SLU Catalog](https://catalog.slu.edu/)
- [UMSL Bulletin](https://bulletin.umsl.edu/)

## Tech Stack

- **D3.js v7** — Interactive graph visualization
- **Gephi GEXF** — Network analysis export format
- **Vanilla HTML/CSS/JS** — No build tools, no frameworks, opens directly in browser

## License

This project is for academic and educational purposes.
