# Reference Documents

## 1. Missouri S&T ME Catalog (2025-2026)
- **File:** `/Users/mahdi/Downloads/mechanicalengineeringMST.pdf`
- **Content:** Complete 11-page ME program catalog including:
  - Program overview, Mission Statement, PEOs, Student Outcomes (ABET SOs 1-7)
  - Full 4-year curriculum (128 credits)
  - 4 Emphasis Areas: Energy Conversion, Manufacturing Processes, Mechanical Design & Analysis, Systems Integration
  - Complete course descriptions with prerequisites for all MECH ENG courses (1720 through 5830)
  - Faculty listing with credentials and PhD institutions
  - Detailed footnotes on grade requirements, elective rules

### Key Details from PDF (supplements web data):
- **Emphasis area elective structure:** Each emphasis requires 4 specific courses substituted into the technical elective slots
- **Energy Conversion:** MECH ENG 5527/5519/5525/5131/5139 + additional from thermal list
- **Manufacturing:** MECH ENG 3653 + 3 from robotics/ML/CNC/automation list
- **Design & Analysis:** 1 design + 1 analysis from vibrations/FEA/composites/fatigue lists + 2 more
- **Systems Integration:** Replaces circuits and some electives with 3 circuits courses (ELEC ENG 2100/2101/2120) + systems management + systems technical elective
- **Faculty:** ~30 faculty members, mix of Professors, Associate Professors, Assistant Teaching Professors
- **PhD institutions:** Purdue, Michigan, MIT, Berkeley, Virginia Tech, Clemson, Texas A&M, Iowa State, etc.

## 2. DEEP Project Paper (Busch-Vishniac et al., 2011)
- **File:** `/Users/mahdi/Downloads/Deconstructing_Engineering_Education_Programmes_DEEP.pdf`
- **Citation:** Busch-Vishniac, I. et al. (2011). "Deconstructing Engineering Education Programmes: The DEEP Project to reform the mechanical engineering curriculum." European Journal of Engineering Education, 36(3), 269-283.
- **DOI:** 10.1080/03043797.2011.579590

### Key Findings Relevant to UMSL Curriculum Design:

**Goal:** Revise ME curriculum to attract/retain diverse students by reducing critical path lengths and increasing flexibility.

**Method:**
1. Dissected syllabi from 8 universities + MIT into 833 individual topics
2. Defined prerequisite/successor relationships between topics (not courses)
3. Used genetic algorithm to cluster topics into 12 new course-clusters (A-L)
4. Each cluster ~84 hours instruction (roughly a full-year course)

**Key Results:**
- Of ~1000 topics across 9 programs, only 70 were common to majority — ME programs are less standardized than assumed
- Traditional courses naturally form prerequisite chains that are hard to decouple
- The 12 clusters mix topics from different traditional subdisciplines (e.g., thermo + kinematics in same cluster)
- Cross-cluster dependencies reduced from 988 to 334 links
- Setting max 7 cross-cluster links gives 4-year flexibility with entry possible in year 2

**Table 3 - Traditional Course Topics Distributed Across DEEP Clusters:**
- Mathematics: clusters A, C, D, E, F, G
- Physics: clusters D, E
- Chemistry: clusters D, E
- Statics: clusters E, H, J
- Dynamics: clusters C, D, E
- Thermodynamics: clusters A, B
- Fluid mechanics: clusters A, H, J
- Heat transfer: clusters A
- Machine design: clusters C, F
- System dynamics: clusters A, C, F, J, L
- Design: clusters C, H, J, L
- Manufacturing: clusters G, I
- Material Science: clusters A, C, E, F, J
- Electrical engineering: clusters C, F, G, J

**Implications for UMSL:**
1. **Shorter critical paths = more accessible program** — UMSL should identify and minimize its longest prerequisite chains
2. **Topic-level thinking > course-level thinking** — When designing courses, think about which topics truly need to precede others
3. **Interdisciplinary clusters** increase flexibility — Consider courses that blend subdisciplines (e.g., UMSL's MENG 3360 "Machine Design and Manufacturing" already does this)
4. **Entry flexibility** matters for retention — The more independent course clusters are, the easier it is for students to recover from a failed course
5. **Diversity of applications** increases retention — Applications tied to environmental/health/social themes attract broader student demographics

**Cluster Characteristics (Table 1):**
| Cluster | Topics | Hours | Longest Chain | Neophyte Topics | Terminal Topics |
|---------|--------|-------|---------------|-----------------|-----------------|
| A | 98 | 96.25 | 11 | 8 | 49 |
| B | 69 | 84 | 12 | 10 | 19 |
| C | 91 | 115 | 12 | 6 | 41 |
| D | 65 | 85 | 5 | 9 | 24 |
| E | 72 | 105 | 6 | 3 | 39 |
| F | 75 | 82.25 | 6 | 5 | 31 |
| G | 41 | 52.5 | 3 | 12 | 17 |
| H | 75 | 95 | 17 | 3 | 25 |
| I | 76 | 93.75 | 8 | 8 | 42 |
| J | 74 | 107 | 9 | 8 | 31 |
| K | 79 | 85 | 7 | 16 | 33 |
| L | 67 | 93.5 | 9 | 11 | 27 |
