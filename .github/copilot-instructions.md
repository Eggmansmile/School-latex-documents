# GitHub Copilot Instructions for School-latex-documents

This repo is a single LaTeX workbook for **Wiskunde voor Systemen** and **Warmte en stromingen**.


## Build / preview
- VS Code LaTeX Workshop is fine; target engine is `pdflatex`.

## Document conventions (project-specific)
- Language is **Dutch** (`\usepackage[dutch]{babel}`) → keep all prose Dutch.
- Use **engineering notation**: imaginary unit `j` (not `i`), unit step `u(t)`, impulse `\delta(t)`.
- Prefer unnumbered display math with `\[ ... \]`.
- For tight formula tables, use local spacing blocks (pattern used throughout the formularium):
    ```latex
    \begingroup
    \setlength{\tabcolsep}{6pt}
    \renewcommand{\arraystretch}{1.35}
    \[
    \begin{array}{@{}lcl@{}}
    ...
    \end{array}
    \]
    \endgroup
    ```
- Diagrams are drawn inline with TikZ (common scale: `\begin{tikzpicture}[x=1.2cm,y=1.2cm]`).

## Solutions must be step-by-step
The exercises are stated earlier; worked solutions are under `\section{Oplossingen}` and typically follow:
`\textbf{Gegeven:}` → `\textbf{Vraag:}` → `\textbf{Oplossing:}`.

When adding/editing solutions:
- Show **concrete intermediate steps**, not only the final result.
- Prefer `\begin{enumerate}[label=(\alph*)]` for subquestions and `itemize` for short reasoning checks.

in the folder you're working check for a txt file named Links with usefull links to websites that can help you with the exercises or theory.
