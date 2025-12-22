# AGENTS.md

## Build Commands
- **Build single file**: `pdflatex -interaction=nonstopmode -file-line-error "<filename>.tex"` (run twice for cross-references)
- **Build with latexmk**: `latexmk -pdf "<filename>.tex"` (handles multi-pass automatically)
- **Build with minted**: `latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode -file-line-error" "<filename>.tex"`
- **CI builds all documents**: Uses `.github/workflows/latex-build.yml`

## Code Style Guidelines
- **Language**: Dutch content, UTF-8 encoding (`\usepackage[utf8]{inputenc}`), `babel` for Dutch
- **Custom macros**: Use `\frm{Label}{math}{notes}` for formulas, `\fig[width]{path}{caption}{label}` for figures
- **Symbol registration**: Use `\symS{symbol}{name}{unit}` or `\symW{...}` for thermal symbols
- **Exercise boxes**: Use `\begin{oefenblok}[Title]` and `\begin{theorieblok}[Title]`
- **Asset paths**: Images under `assets/` subfolders, quote paths with spaces
- **Formularium**: Automatic collection via `\frm` macro, requires double compile
- **Packages**: Required: tikz, amsmath, amssymb, geometry, enumitem, hyperref

## Entry Points
- Math exercises: `math-systems/MATHSYS-Oefeningen-RubenRyckaert.tex`
- Thermal/fluids: `Warmte en stromingen/Warmte en stromingen Samenvatting Ruben Ryckaert.tex`
- Production tech: `Productietechnologie/ProductieTechnologie-Samenvatting-RubenRyckaert.tex`
- Template examples: `latex_templates/template_examples.tex`