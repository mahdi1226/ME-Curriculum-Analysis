#!/usr/bin/env python3
"""Generate two PDF documents for UMSL ME course categorization."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)

# Colors
BLUE = HexColor("#0969da")
DARK = HexColor("#1f2328")
GRAY = HexColor("#656d76")
LIGHT_BG = HexColor("#f6f8fa")
BORDER = HexColor("#d1d9e0")
WHITE = white

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    'DocTitle', parent=styles['Title'], fontSize=22, textColor=DARK,
    spaceAfter=4, alignment=TA_LEFT
))
styles.add(ParagraphStyle(
    'DocSubtitle', parent=styles['Normal'], fontSize=12, textColor=GRAY,
    spaceAfter=20, alignment=TA_LEFT
))
styles.add(ParagraphStyle(
    'SectionHead', parent=styles['Heading2'], fontSize=16, textColor=BLUE,
    spaceBefore=24, spaceAfter=10, borderWidth=0
))
styles.add(ParagraphStyle(
    'CellText', parent=styles['Normal'], fontSize=9, leading=11, textColor=DARK
))
styles.add(ParagraphStyle(
    'CellBold', parent=styles['Normal'], fontSize=9, leading=11, textColor=DARK,
    fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'HeaderCell', parent=styles['Normal'], fontSize=9, leading=11,
    textColor=WHITE, fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'FooterNote', parent=styles['Normal'], fontSize=8, textColor=GRAY,
    spaceBefore=12, fontName='Helvetica-Oblique'
))


def make_table(data_rows, col_widths=None):
    """Create a styled table from data rows."""
    if col_widths is None:
        col_widths = [0.85*inch, 2.0*inch, 0.35*inch, 3.8*inch]

    header = [
        [Paragraph("Course", styles['HeaderCell']),
         Paragraph("Title", styles['HeaderCell']),
         Paragraph("Cr", styles['HeaderCell']),
         Paragraph("Description", styles['HeaderCell'])]
    ]

    rows = []
    for course, title, cr, desc in data_rows:
        rows.append([
            Paragraph(course, styles['CellBold']),
            Paragraph(title, styles['CellText']),
            Paragraph(str(cr), styles['CellText']),
            Paragraph(desc, styles['CellText']),
        ])

    table = Table(header + rows, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#24292f")),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]
    # Alternate row colors
    for i in range(1, len(rows) + 1):
        if i % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, i), (-1, i), LIGHT_BG))

    table.setStyle(TableStyle(style_cmds))
    return table


def build_pdf1():
    """PDF 1: Course Categories."""
    doc = SimpleDocTemplate(
        "/Users/mahdi/Desktop/ME_Graph/data/UMSL_ME_Course_Categories.pdf",
        pagesize=letter,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.7*inch, bottomMargin=0.6*inch
    )
    story = []

    # Title
    story.append(Paragraph("UMSL Mechanical Engineering", styles['DocTitle']))
    story.append(Paragraph("Course Categories", styles['DocTitle']))
    story.append(Paragraph("School of Engineering, 2025-2026 Catalog", styles['DocSubtitle']))

    # Table 1: Engineering Core
    story.append(Paragraph("Engineering Core Courses (27 credits)", styles['SectionHead']))
    story.append(make_table([
        ("ENGR 1414", "Elementary Engineering Design", 2,
         "Introduction to engineering design process, project planning, teamwork, and systems integration through design-build-test projects"),
        ("ENGR 2310", "Statics", 3,
         "Equilibrium of particles and rigid bodies; distributed forces, centroids, friction, and structural analysis"),
        ("ENGR 2320", "Dynamics", 3,
         "Kinematics and kinetics of particles and rigid bodies; work-energy and impulse-momentum methods"),
        ("ENGR 2330", "Introduction to Thermodynamics", 3,
         "Properties of substances, first and second laws of thermodynamics, entropy, ideal gas applications"),
        ("ENGR 2332", "Mechanics of Materials", 3,
         "Stress and strain in structural members: axial, torsion, bending, shear, combined loading, deflection"),
        ("ENGR 3300", "Applied Thermodynamics", 3,
         "Power and refrigeration cycles, gas mixtures, psychrometrics, combustion, exergy analysis"),
        ("ENGR 2022", "Engineering Economics and PM", 3,
         "Time value of money, economic analysis methods, depreciation, project management fundamentals"),
        ("EENG 2310", "Circuit Analysis I", 3,
         "DC and AC circuit analysis; Kirchhoff's laws, network theorems, transients, phasors, frequency response"),
        ("CMP SCI 1250", "Introduction to Computing", 3,
         "Python programming for engineers; data analysis, visualization, computational problem solving"),
        ("ENGR 4400", "FE Exam Review", 1,
         "Comprehensive review of all engineering topics for the Fundamentals of Engineering licensing exam"),
    ]))

    story.append(PageBreak())

    # Table 2: ME Core
    story.append(Paragraph("ME Core Courses (24 credits)", styles['SectionHead']))
    story.append(make_table([
        ("MENG 1204", "ME 3D Design (CAD)", 2,
         "Introduction to CAD using SolidWorks; 2D sketching, 3D solid modeling, assemblies, engineering drawings"),
        ("MENG 3330", "Instrumentation and Measurement", 3,
         "Measurement statistics, sensors (temperature, pressure, force, flow), signal conditioning, data acquisition"),
        ("MENG 3340", "Properties of Material and Testing", 3,
         "Crystal structure, phase diagrams, mechanical properties, failure modes, materials selection, testing methods"),
        ("MENG 3350/L", "System Dynamics and Control + Lab", 4,
         "System modeling, Laplace transforms, transfer functions, PID control, frequency response; lab experiments"),
        ("MENG 3360", "Machine Design and Manufacturing", 3,
         "Design of machine elements (shafts, bearings, gears, springs); fatigue analysis, manufacturing processes, DFM"),
        ("MENG 3370/L", "Fluid Mechanics + Lab", 4,
         "Fluid properties, statics, Bernoulli equation, conservation laws, dimensional analysis, pipe flow, external flow"),
        ("MENG 3380/L", "Heat Transfer + Lab", 4,
         "Steady/transient conduction, fins, forced/natural convection, radiation, heat exchangers"),
        ("MENG 3390", "Product Dev. and Prototyping Lab", 1,
         "Product development process, additive manufacturing, reverse engineering, rapid prototyping"),
    ]))

    story.append(Spacer(1, 20))

    # Table 3: ME Advanced
    story.append(Paragraph("ME Advanced / Elective Courses (10 credits)", styles['SectionHead']))
    story.append(make_table([
        ("MENG 4440", "Intro to Composite Materials", 3,
         "Fiber/matrix materials, micromechanics, laminate theory, failure criteria, manufacturing, testing"),
        ("MENG 4450", "Computational Fluid Dynamics", 3,
         "Governing equations, discretization, grid generation, turbulence models, commercial CFD software"),
        ("MENG 4460", "Renewable Energy Systems Lab", 1,
         "Hands-on lab with solar, wind, and fuel cell systems; data acquisition and efficiency analysis"),
        ("MENG 4490", "Advanced Manufacturing", 3,
         "CNC machining, advanced additive manufacturing, automation, Industry 4.0, smart manufacturing"),
    ]))

    story.append(Spacer(1, 20))

    # Table 4: Capstone
    story.append(Paragraph("Capstone / Design Courses (4 credits)", styles['SectionHead']))
    story.append(make_table([
        ("MENG 4980", "Senior Design I", 2,
         "First capstone: project planning, concept generation/selection, market analysis, preliminary design"),
        ("MENG 4990", "Senior Design II", 2,
         "Second capstone: detailed analysis, fabrication, testing, validation, documentation, final presentation"),
    ]))

    doc.build(story)
    print("PDF 1 created: UMSL_ME_Course_Categories.pdf")


def build_pdf2():
    """PDF 2: Courses by Subdiscipline."""
    doc = SimpleDocTemplate(
        "/Users/mahdi/Desktop/ME_Graph/data/UMSL_ME_Courses_by_Subdiscipline.pdf",
        pagesize=letter,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.7*inch, bottomMargin=0.6*inch
    )
    story = []

    # Title
    story.append(Paragraph("UMSL Mechanical Engineering", styles['DocTitle']))
    story.append(Paragraph("Courses by ME Subdiscipline", styles['DocTitle']))
    story.append(Paragraph("School of Engineering, 2025-2026 Catalog", styles['DocSubtitle']))

    # Table 1: Fluid Dynamics and Heat Transfer
    story.append(Paragraph("Fluid Dynamics and Heat Transfer (18 credits)", styles['SectionHead']))
    story.append(make_table([
        ("ENGR 2330", "Introduction to Thermodynamics", 3,
         "Properties of substances, first and second laws, entropy, ideal gas \u2014 foundation for all thermal/fluid courses"),
        ("ENGR 3300", "Applied Thermodynamics", 3,
         "Power/refrigeration cycles, gas mixtures, psychrometrics, combustion \u2014 builds on ENGR 2330"),
        ("MENG 3370/L", "Fluid Mechanics + Lab", 4,
         "Fluid statics, Bernoulli, conservation laws, pipe flow, external flow, dimensional analysis; lab experiments"),
        ("MENG 3380/L", "Heat Transfer + Lab", 4,
         "Conduction (steady/transient), convection (forced/natural), radiation, heat exchangers; lab experiments"),
        ("MENG 4450", "Computational Fluid Dynamics", 3,
         "Numerical solution of governing equations, discretization, turbulence modeling, commercial CFD software"),
        ("MENG 4460", "Renewable Energy Systems Lab", 1,
         "Solar, wind, and fuel cell energy systems \u2014 applied thermal/fluid concepts in renewable energy context"),
    ]))

    story.append(PageBreak())

    # Table 2: Solid Mechanics and Materials
    story.append(Paragraph("Solid Mechanics and Materials (16 credits)", styles['SectionHead']))
    story.append(make_table([
        ("ENGR 2310", "Statics", 3,
         "Equilibrium, trusses/frames, centroids, friction, moments of inertia \u2014 prerequisite for all solid mechanics"),
        ("ENGR 2332", "Mechanics of Materials", 3,
         "Stress/strain, axial loading, torsion, bending, shear, combined loading, beam deflection, buckling"),
        ("MENG 3340", "Properties of Material and Testing", 3,
         "Crystal structure, phase diagrams, mechanical properties, failure modes, materials selection, heat treatment"),
        ("MENG 3360", "Machine Design and Manufacturing", 3,
         "Machine element design (shafts, bearings, gears), fatigue analysis, safety factors, DFM"),
        ("MENG 4440", "Intro to Composite Materials", 3,
         "Fiber-reinforced composites: micromechanics, laminate theory (CLT), failure criteria, manufacturing"),
        ("MENG 3390", "Product Dev. and Prototyping Lab", 1,
         "Product development, additive manufacturing, reverse engineering \u2014 applied solid mechanics in prototyping"),
    ]))

    story.append(Spacer(1, 16))

    # Table 3: Manufacturing and Design
    story.append(Paragraph("Manufacturing and Design (13 credits)", styles['SectionHead']))
    story.append(make_table([
        ("MENG 1204", "ME 3D Design (CAD)", 2,
         "CAD fundamentals using SolidWorks: sketching, solid modeling, assemblies, engineering drawings, 3D printing"),
        ("MENG 3360", "Machine Design and Manufacturing", 3,
         "Machine element design combined with manufacturing processes overview, design for manufacturing"),
        ("MENG 3390", "Product Dev. and Prototyping Lab", 1,
         "Product development lifecycle, additive manufacturing, reverse engineering, rapid prototyping"),
        ("MENG 4490", "Advanced Manufacturing", 3,
         "CNC machining, advanced additive mfg, automation/robotics, Industry 4.0, smart manufacturing, quality control"),
        ("MENG 4980", "Senior Design I", 2,
         "Capstone design: project planning, concept generation, preliminary analysis, team-based open-ended design"),
        ("MENG 4990", "Senior Design II", 2,
         "Capstone continued: detailed analysis, fabrication, testing, validation, technical documentation"),
    ]))

    story.append(PageBreak())

    # Table 4: Controls, Dynamics, and Instrumentation
    story.append(Paragraph("Controls, Dynamics, and Instrumentation (13 credits)", styles['SectionHead']))
    story.append(make_table([
        ("ENGR 2320", "Dynamics", 3,
         "Particle/rigid body kinematics and kinetics, work-energy, impulse-momentum \u2014 foundation for controls"),
        ("EENG 2310", "Circuit Analysis I", 3,
         "DC/AC circuits, Kirchhoff's laws, transients, phasors \u2014 provides electrical foundation for instrumentation"),
        ("MENG 3330", "Instrumentation and Measurement", 3,
         "Sensors, signal conditioning, data acquisition, measurement uncertainty \u2014 bridge between circuits and ME"),
        ("MENG 3350/L", "System Dynamics and Control + Lab", 4,
         "System modeling, Laplace transforms, PID control, frequency response, root locus; controller design lab"),
    ]))

    story.append(PageBreak())

    # Table 5: Mathematics Foundation
    story.append(Paragraph("Mathematics Foundation (21 credits)", styles['SectionHead']))
    story.append(make_table([
        ("MATH 1800", "Analytic Geometry and Calculus I", 5,
         "Limits, derivatives, integrals of single-variable functions; applications to rates of change, optimization, area"),
        ("MATH 1900", "Analytic Geometry and Calculus II", 5,
         "Techniques of integration, sequences, series, parametric equations, polar coordinates"),
        ("MATH 2000", "Analytic Geometry and Calculus III", 5,
         "Vectors, partial derivatives, multiple integrals, vector calculus (Green's, Stokes', Divergence theorems)"),
        ("MATH 2020", "Introduction to Differential Equations", 3,
         "First/second order ODEs, Laplace transforms, systems of ODEs \u2014 essential for fluids, controls, heat transfer"),
        ("MATH 1320", "Intro to Probability and Statistics", 3,
         "Descriptive statistics, probability distributions, hypothesis testing, regression, confidence intervals"),
    ]))

    story.append(Spacer(1, 16))

    # Table 6: Physics and Chemistry
    story.append(Paragraph("Physics and Chemistry (14 credits)", styles['SectionHead']))
    story.append(make_table([
        ("PHYS 2111/L", "Physics I: Mechanics and Heat + Lab", 5,
         "Calculus-based mechanics: kinematics, Newton's laws, work-energy, momentum, rotational dynamics, oscillations"),
        ("PHYS 2112/L", "Physics II: E&M, Optics + Lab", 5,
         "Calculus-based E&M: electric fields, Gauss's law, circuits, magnetism, Faraday's law, EM waves, optics"),
        ("CHEM XXXX", "General Chemistry for Engineering", 4,
         "Atomic structure, bonding, stoichiometry, thermochemistry, states of matter, solutions, equilibria"),
    ]))

    story.append(Spacer(1, 16))

    # Table 7: General Education and Other Requirements
    story.append(Paragraph("General Education and Other Requirements (25 credits)", styles['SectionHead']))
    story.append(make_table([
        ("ENGL 1100", "First-Year Writing", 3,
         "College-level writing skills: argumentation, research, rhetoric, academic discourse"),
        ("ENGL 3130", "Technical Writing", 3,
         "Writing for engineering audiences: reports, proposals, documentation, technical communication"),
        ("PHIL 2259", "Engineering Ethics", 3,
         "Ethical theories, engineering codes of ethics, case studies, AI ethics, professional responsibility"),
        ("ENGR 1414", "Elementary Engineering Design", 2,
         "Introduction to design process, project planning, teamwork, systems integration \u2014 first-year experience"),
        ("ENGR 2022", "Engineering Economics and PM", 3,
         "Time value of money, economic analysis, depreciation, project management fundamentals"),
        ("ENGR 4400", "FE Exam Review", 1,
         "Comprehensive review of all ME topics for the Fundamentals of Engineering licensing exam"),
        ("INTDSC 1003", "First Year Experience", 1,
         "University transition: faculty expectations, support services, student life"),
        ("", "Core \u2014 American History/Government", 3,
         "General education requirement in American history or government"),
        ("", "Explore \u2014 Social Sciences (x2)", 6,
         "Two social science electives, one with global perspectives component"),
        ("", "Explore \u2014 Humanities & Fine Arts (x2)", 6,
         "Two humanities or fine arts electives for breadth"),
        ("", "Core \u2014 Communication Proficiency", 3,
         "Oral or written communication proficiency requirement"),
    ]))

    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "Note: Some courses appear in multiple categories (e.g., MENG 3360 appears in both "
        "Solid Mechanics and Manufacturing) because they span subdisciplines. This is consistent "
        "with the DEEP project's finding that traditional subdiscipline boundaries are somewhat artificial. "
        "The four ME subdiscipline tables above contain all ME-specific and engineering core courses. "
        "The remaining tables list the math/science foundation and general education courses that "
        "complete the 125-credit BSME degree.",
        styles['FooterNote']
    ))

    doc.build(story)
    print("PDF 2 created: UMSL_ME_Courses_by_Subdiscipline.pdf")


if __name__ == "__main__":
    build_pdf1()
    build_pdf2()
