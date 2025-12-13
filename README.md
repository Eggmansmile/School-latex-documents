# Wiskunde voor Systemen — Oefeningen & Oplossingen

## Overview

This repository contains a **comprehensive compilation of exercises and worked solutions** for the **"Wiskunde voor Systemen"** course at **KU Leuven**, part of the **Industrial Engineering (EM 2)** program.

The document provides systematic coverage of fundamental mathematical concepts for systems and signal processing, with a strong emphasis on **step-by-step derivations** and **formularium cross-references**.

---

## Document Structure

### Main Document
- **File:** `math-systems/MATHSYS_oefeningen.tex`
- **Format:** LaTeX (pdflatex)
- **Output:** `MATHSYS_oefeningen.pdf` (87 pages)
- **Language:** Dutch

### Contents

#### Part 1: Formularium (Reference)
A concise collection of standard formulas for:
- **Laplace Transform (LT):** Definition, properties, and common pairs
- **Fourier Transform (FTC):** Definitions, properties, and transform pairs
- **Fourier Series (FS):** Cartesian and complex forms, links to FTC

#### Part 2: Oefeningen (Exercises) — 8 Chapters

1. **Hoofdstuk 1:** Signalen en Systemen - Eerste Kennismaking
2. **Hoofdstuk 2:** Basissignalen en Bewerkingen
3. **Hoofdstuk 3:** Laplacetransformatie
4. **Hoofdstuk 4:** Fouriertransformatie
5. **Hoofdstuk 5:** Fourierreeksen
6. **Hoofdstuk 6:** LTC-Systemen
7. **Hoofdstuk 7:** Eigenwaarden en Eigenvectoren
8. **Hoofdstuk 8:** Examengerichte Oefeningen

**Total Exercises:** 44+ unique problems
- Core exercises: Traditional problem statements
- Starter exercises: Accessible entry-level variants
- Exam-level exercises: Advanced synthesis problems

#### Part 3: Oplossingen (Detailed Solutions)
Complete step-by-step solutions for all exercises, including:
- **Intermediate steps** showing all algebraic manipulations
- **Formularium references** (e.g., `\ref{form:laplace-prop}`) for direct lookup
- **Physical interpretations** connecting theory to applications
- **TikZ visualizations** for signal and frequency responses
- **Verification methods** confirming results

---

## Key Features

### 📐 Mathematical Rigor
- Comprehensive coverage of **Laplace and Fourier transforms**
- **Eigenvalue problems** and matrix diagonalization
- **System stability analysis** (BIBO criteria, pole locations)
- **Convolution and spectral analysis**

### 🎓 Pedagogical Design
- **Formularium first:** All solutions reference the standard formula sheet
- **Progressively structured:** From basics (signals) to advanced (Fourier analysis)
- **Variety of difficulty:** Starter → Standard → Exam-level exercises
- **Physical context:** Engineering interpretation of mathematical results

### 🎨 Professional Presentation
- **TikZ diagrams:** Step responses, frequency plots, signal sketches
- **Consistent notation:** Engineering standard (imaginary unit `j`, unit step `u(t)`)
- **Table formatting:** Tight spacing for formula collections
- **Dutch language:** Aligned with KU Leuven curriculum

---

## Building the Document

### Requirements
- **TeX Distribution:** MiKTeX or TeX Live
- **LaTeX Engine:** pdflatex
- **Packages Used:**
  - `tikz`, `amsmath`, `amssymb`, `enumitem`
  - `geometry`, `graphicx`, `hyperref`, `babel` (dutch)

### Compilation

```bash
cd math-systems/
pdflatex -interaction=nonstopmode MATHSYS_oefeningen.tex
```

To clean build artifacts:
```bash
rm -f *.aux *.log *.out *.toc *.synctex.gz
```

### Output
- **PDF:** `MATHSYS_oefeningen.pdf`
- **Pages:** 87 pages
- **Size:** ~740 KB

---

## Document Conventions

### Notation
- Imaginary unit: `j` (not `i`)
- Unit step: `u(t)`
- Impulse: `\delta(t)`
- Laplace transform: `\mathcal{L}\{\cdot\}` or `LT\{\cdot\}`
- Fourier transform: `\mathcal{F}\{\cdot\}` or `FTC\{\cdot\}`

### Formula References
When a solution uses a formularium formula, it includes:
```latex
\emph{Zie Formularium: afgeleide-eigenschap \ref{form:laplace-prop} en paren \ref{form:laplace-pairs}.}
```

### Solution Structure
Each solution follows:
1. **\textbf{Gegeven}** (Given) — Problem statement recap
2. **\textbf{Vraag}** (Question) — What to find (if detailed)
3. **\textbf{Oplossing}** (Solution) — Step-by-step work
4. **Verification** — Sanity checks or alternative methods

---

## Exercise Categories

### Core Topics
- **Laplace Transform:** Inverse transforms, initial/final value theorems, system analysis
- **Fourier Transform:** Duality, modulation, convolution theorem
- **Fourier Series:** Even/odd functions, symmetry exploitation, Parseval's theorem
- **LTC Systems:** Poles/zeros, stability, frequency response, cascade systems
- **Linear Algebra:** Eigenvalues, diagonalization, matrix exponentials

### Difficulty Levels
- **Starter:** Single-step calculations, basic definitions
- **Standard:** Multi-step derivations, combined concepts
- **Exam-level:** Synthesis problems, design-oriented questions

---

## File Organization

```
School-latex-documents/
├── math-systems/
│   ├── MATHSYS_oefeningen.tex     (Main document)
│   ├── MATHSYS_oefeningen.pdf     (Compiled output)
│   ├── Starterexercises.tex       (Starter exercise source)
│   └── output.txt                 (Compilation log)
└── README.md                      (This file)
```

---

## Educational Use

### For Students
- Use the **Formularium section** as a quick reference during problem-solving
- Study **worked solutions** to understand the methodology
- Attempt exercises before viewing solutions
- Use **Starter exercises** for confidence building

### For Instructors
- Adapt exercises for assignments or exams
- Modify numerical values while keeping the solution structure
- Cross-reference the formularium for consistency
- Supplement with additional context-specific applications

---

## Course Context

This document is part of the **Industrial Engineering (EM 2)** curriculum at **KU Leuven**, where **"Wiskunde voor Systemen"** provides foundational tools for:
- Automatic control and signal processing
- Electrical circuit analysis
- Mechanical system dynamics
- Communication systems
- Digital signal processing

---

## Version History

- **v1.0** (Dec 2025): Complete compilation with formularium, 8 chapters, 44+ exercises, and detailed solutions
  - Chapters 1-8 fully developed
  - 9 starter exercises integrated
  - 4 advanced variants (3.11, 3.12, 4.9, 4.10) added
  - All sections renamed with descriptive titles
  - TikZ visualizations throughout

---

## License & Attribution

This compilation was created for educational purposes at KU Leuven. 

- **Primary source:** KU Leuven ESAT course materials
- **Additional exercises:** Starter Oefeningen module
- **Formatting & solutions:** Systematic LaTeX compilation with step-by-step derivations

---

## Contact & Feedback

For questions, corrections, or suggestions regarding this exercise collection:
- Consult the **formularium** for reference definitions
- Review the **worked solutions** for methodology
- Cross-check numerical results using alternative methods

---

**Last Updated:** December 2025  
**Status:** Complete and production-ready ✓
