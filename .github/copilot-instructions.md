# GitHub Copilot Instructions for School-latex-documents

This repo is a single LaTeX workbook for **Wiskunde voor Systemen** and **Warmte en stromingen**.

## Available Tools & Capabilities

You have access to a comprehensive set of tools to manage this project:

### File Operations
- **read_file**: Read file contents with line ranges
- **create_file**: Create new files with content
- **replace_string_in_file**: Edit existing files (include 3-5 context lines before/after)
- **multi_replace_string_in_file**: Perform multiple edits efficiently in one call

### Search & Discovery
- **grep_search**: Fast text search with regex support (for file overviews)
- **semantic_search**: Natural language search across workspace
- **file_search**: Find files by glob patterns

### Project Structure
- **list_dir**: Browse directory contents
- **get_errors**: Check for compile/lint errors

### Document Organization
- **manage_todo_list**: Track multi-step work with write/read operations

### Documentation & Reference
- **mcp_context7_resolve-library-id**: Resolve package names to library IDs for documentation lookup
- **mcp_context7_get-library-docs**: Fetch up-to-date documentation for LaTeX packages, libraries, and reference materials
  - Use `mode='code'` for API references and code examples
  - Use `mode='info'` for conceptual guides and architectural questions
  - Useful for understanding `graphicx`, `tikz`, `amsmath`, and other packages used in the project

### Web Search Tools
- **mcp_web-search_full-web-search**: Comprehensive web search with full page content extraction. Use this for detailed research.
- **mcp_web-search_get-web-search-summaries**: Lightweight web search returning only snippets. Use for quick lookup.
- **mcp_web-search_get-single-web-page-content**: Extract full content from a specific URL.

**Preference**: Use `mcp_web-search_*` tools instead of firecrawl for web-related tasks.

**Best Practice**: For multiple independent edits, use `multi_replace_string_in_file` instead of sequential calls—it's more efficient.

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
- Each section should start with a `\subsection*{Belangrijke Formules}` that lists key equations and their purpose in Dutch.

## Document Structure

The main file is located in `Warmte en stromigen/Thermische_en_Fluidumwetenschappen.tex`:

- **Part 1: Stromingen** – Fluid mechanics theory (chapters 1–6)
- **Part 2: Warmte** – Thermodynamics and heat transfer theory (chapters 7–9)
- **Part 3: Oefeningen** – Exercises organized by topic:
  - Chapter: Oefeningen: Stromingen (subsections: Hydrostatica, Drijfvermogen, Bernoulli, Impulsbehoud, Stroming)
  - Chapter: Oefeningen: Warmte en Thermodynamica (subsections: Basisconcepten, Eerste Hoofdwet Gesloten, Eerste Hoofdwet Open, Tweede Hoofdwet)

Assets (images) are stored in `Warmte en stromigen/assets/`.

## Useful Resources

Check the folder you're working in for a txt file named `Links` containing useful links to websites for exercises or theory.

## File Editing Guidelines

When making changes:
1. Always include surrounding context (3-5 lines before/after) in oldString for precision
2. For multiple edits, batch them using `multi_replace_string_in_file`
3. Verify changes don't break LaTeX syntax by checking for missing braces, unmatched commands
4. If adding exercises, follow the established pattern: `\subsection{Opgave N: Titel}`
