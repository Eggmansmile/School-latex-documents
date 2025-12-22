# .github/copilot-instructions.md

Purpose
- Help AI coding agents be immediately productive in this LaTeX repository (lecture notes, exercises, and summaries in Dutch).

Quick start (what to run)
- Build a single file (preferred for quick feedback):
  - VS Code task: **Build LaTeX (Active File)** (uses `pdflatex -interaction=nonstopmode -file-line-error ${fileBasename}`).
  - CLI: `pdflatex -interaction=nonstopmode -file-line-error "<filename>.tex"` (run twice to resolve cross-references).
- For full, multi-file workflows consider using `latexmk -pdf <mainfile>.tex` (not currently included in the repo).

Where to look first (entry points)
- Main pieces:
  - `math-systems/MATHSYS-Oefeningen-RubenRyckaert.tex` — large, canonical source for the math exercises (contains macros and style).
  - `Warmte en stromingen/Warmte en stromingen Samenvatting Ruben Ryckaert.tex` — thermal/fluid summary that uses `assets/` heavily and demonstrates symbol registration macros.
  - `Productietechnologie/ProductieTechnologie-Samenvatting-RubenRyckaert.tex` — placeholder file (empty) for production-technology notes.
- `README.md` contains high-level description and lists required packages (tikz, amsmath, amssymb, geometry, enumitem, hyperref, etc.).

Key repository conventions & patterns (do not change without verifying)
- Encoding and language:
  - Files use UTF-8 (`\usepackage[utf8]{inputenc}`) and Dutch (`\usepackage[dutch]{babel}` / plain `babel`), so preserve encoding and language when editing text.
- Custom styling macros:
  - Exercise and theory boxes: `\newtcolorbox{theorieblok}{...}`, `\newtcolorbox{oefenblok}{...}` — use these for consistent visual style.
  - Emphasis macros: `\concept{}`, `\belangrijk{}`, `\important{}` are used throughout; prefer these rather than ad-hoc formatting.
- Symbol registration (important pattern in `Warmte en stromingen`):
  - Use `\symS{<symbol>}{<name>}{<unit/notes>}` or `\symW{...}` to introduce symbols. This both shows an explanation and writes an entry to the `.aux` to build the formularium.
  - Avoid duplicating symbol entries; the helpers ensure first-time display only.
- Asset management:
  - All images/figures referenced relatively under `Warmte en stromingen/assets/` (subfolders: `slides/`, `wikipedia/`). Use the same path conventions and filenames; filenames may contain spaces — always quote paths in shell commands and escape properly in scripts.
  - Some PDFs are included (`\includepdf{...}` or `\includepdf[pages=...]{...}`); treat these as binary assets and do not attempt to edit them in-text.
- Filenames & spacing:
  - Several files include spaces and diacritics in names (`Warmte en stromingen Samenvatting Ruben Ryckaert.tex`). When scripting or writing commands, quote these paths.

Editing guidelines & safe PR scope
- Keep changes small and focused: fix typos, add or replace images, add exercises or examples, or add new symbols using the established macros.
- Do not change global package versions or the document class without testing all main files (build both `MATHSYS-...tex` and the Warmte file) — such changes can break layout project-wide.
- New images: place under `assets/` (prefer existing subfolders). Keep filenames descriptive and avoid extremely long names.

Examples (how to perform common tasks)
- Introduce a new symbol (thermal):

```tex
% inside Warmte en stromingen file
\symW{T}{Temperatuur}{K}
% this will show a small symbol box (first time) and register it for the formularium
```

- Add an exercise using existing boxes:

```tex
\begin{oefenblok}[Oefening 3.4]
Bereken de drukval in de buis bij ...
\end{oefenblok}
```

- Add a figure from `assets/slides`:

```tex
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.8\linewidth]{assets/slides/03_Pressure_drop_measurement_with_differential_manometer.png}
  \caption{Differentiële manometer — bron: slides}
  \label{fig:manometer}
\end{figure}
```

CI & automated builds
- A GitHub Actions workflow was added at `.github/workflows/latex-build.yml`. It runs on push and pull-request to `main`/`master`, uses `latexmk` to build the two main documents, and uploads the resulting PDFs as a single artifact named `built-pdfs`.
- The workflow installs a minimal TeX Live package set; if you need extra packages add them to the install step in the workflow.

Local dev convenience
- VS Code: `latex-workshop.latex.autoBuild.run` is set to `"onSave"` so saving a file triggers a quick build (use the `pdflatex × 2 (fast)` recipe or run the latexmk tasks below).
- Workspace tasks: Added two tasks you can run from Terminal → Run Task: **Build main PDFs (latexmk)** and **Build Warmte PDF (latexmk)**. These call `latexmk -pdf` for the corresponding main `.tex` files.

Pasting images quickly (LaTeX Utilities)
- We recommend the `LaTeX Utilities` extension (already in `.vscode/extensions.json`). Configure it to paste images directly into the project and emit an `\includegraphics` snippet:
  - Add to workspace settings (already applied):
    - `latex-utilities.formattedPaste.image.template`: "\\begin{figure}[ht]\\n  \\centering\\n  \\includegraphics[width=0.8\\textwidth]{${imageFilePath}}\\n  \\caption{${imageCaption}}\\n  \\label{fig:${imageFileName}}\\n\\end{figure}" (recommended — prevents `\centering` from leaking)
    - `latex-utilities.formattedPaste.image.path`: `"Productietechnologie/assets"` (default save location for pasted images)
    - `latex-utilities.formattedPaste.enabled`: `true`
  - Default shortcut (extension): `Ctrl+Shift+V` (or use the command palette: `LaTeX Utilities: Paste Image`).
  - Example: paste an image while editing `Productietechnologie/*.tex` — the extension saves the file under `Productietechnologie/assets/` and inserts `\includegraphics[width=\textwidth]{Productietechnologie/assets/<name>.png}`.

Tips
- If you prefer a different default folder per document, edit the `latex-utilities` settings per-workspace or per-language in VS Code.
- If the inserted path contains spaces, LaTeX will still accept it; the extension handles quoting by default, but you can wrap the path manually in `{}` if needed.

For AI coding agents / Copilot
- Use the practical template with examples at `latex_templates/template_examples.tex` — it contains snippets for **siunitx, cleveref, booktabs, subcaption, tcolorbox, pgfplots, listings, minted, biblatex, glossaries, multicol** and a small example `.bib` file.
- Agents may add snippets, small templates, or install packages (use `tlmgr install <package>`). When adding package loads prefer guarded forms (\IfFileExists{...}{...}{...}) so builds don't fail for collaborators.
- Useful tasks are already present: **Build LaTeX (latexmk - template)** and **Build LaTeX (latexmk - active file)**. For `minted` include `-shell-escape` in the pdflatex command (e.g., `latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode -file-line-error"`).
- When adding or updating templates, also update `README.md` and include a brief usage note and package install instructions; open an issue or PR for wider changes.

Repository limitations & things to know
- The documents are language-specific (Dutch). Prefer editing in Dutch for text changes unless the author requests otherwise.
- `Productietechnologie/ProductieTechnologie-Samenvatting-RubenRyckaert.tex` now contains a simple layout template with helper macros:
  - `\frm{Label}{math}{notes}` — register a formula and display a small boxed snippet where used; registered formulas are collected in the `formularium` section via a shared macro package `productie-macros.sty`.
  - `\fig[<width>]{path}{caption}{label}` — quick helper to include images (recommended place: `Productietechnologie/assets/`).
  - The template includes a TikZ placeholder figure and an example `Bernoulli` formula.
  - New: a shared macros file `Productietechnologie/productie-macros.sty` centralizes `\frm`, `\fig` and the `formularium` environment so all variants (Classic/Tufte/KOMA) can reuse them.
  Use the provided template as a starting point for adding chapters and figureacros:
  - `\frm{Label}{math}{notes}` — register a formula and display a small boxed snippet where used; registered formulas will be collected in the `formularium` section.
  - `\fig[<width>]{path}{caption}{label}` — quick helper to include images (recommended place: `Productietechnologie/assets/`).
  - The template includes a TikZ placeholder figure and an example `Bernoulli` formula.
  Use the provided template as a starting point for adding chapters and figures.

When in doubt
- Run the VS Code LaTeX build task and confirm PDFs compile without errors on both `MATHSYS-Oefeningen-RubenRyckaert.tex` and `Warmte en stromingen Samenvatting Ruben Ryckaert.tex`.
- Ask the repository owner for guidance before changing major layout or package choices.

If anything in these instructions is unclear or missing, please point out the area you'd like expanded and I will iterate. — Thanks!