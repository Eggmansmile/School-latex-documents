# GitHub Copilot Instructions for School-latex-documents

This repo is a single LaTeX workbook for **Wiskunde voor Systemen**.

## Where to edit
- Main source: `math-systems/MATHSYS_oefeningen.tex`
- Build artifacts (`.aux/.log/.out/.toc/.synctex.gz/.pdf`) live next to it.

## Build / preview
- Compile from `math-systems/`: `pdflatex MATHSYS_oefeningen.tex`
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

## Mandatory formularium references
If you use a formularium formula/property/pair, explicitly reference it with `\ref{...}` near the first use.

Use the existing labels in `MATHSYS_oefeningen.tex`:
- Laplace: definition `\ref{form:laplace-def}`, properties `\ref{form:laplace-prop}`, pairs `\ref{form:laplace-pairs}`
- Fourier transform: definition `\ref{form:ft-def}`, properties `\ref{form:ft-prop}`, pairs `\ref{form:ft-pairs}`
- Fourier series: `\ref{form:fs-cart}`, `\ref{form:fs-cplx}`, links `\ref{form:fs-ft-link}`

Recommended phrasing (already used in the document):
```latex
\emph{Zie Formularium: afgeleide-eigenschap \ref{form:laplace-prop} en paren \ref{form:laplace-pairs}.}
```

## Source for new exercises
- When adding new exercises, use `math-systems/MATHSYS_oefeningenbundel_2526.txt` as the primary source.
- If available, you may also use the extracted text reference `MATHSYS_oefeningenbundel_2526.txt` to quickly locate exercise numbers/pages and to help rephrase exercises (still: do not copy large blocks verbatim).
- Don’t paste large blocks verbatim from the PDF; rewrite exercise statements in your own words and keep them consistent with the existing style.
- In/near the exercise statement, include a short provenance note such as:
    ```latex
    \emph{Bron: Oefeningenbundel 25--26, oef. X (p.~Y).}
    ```
