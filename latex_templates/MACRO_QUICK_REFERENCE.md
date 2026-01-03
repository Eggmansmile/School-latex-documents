# School-Macros Quick Reference

## 📦 Essential Boxes (4 only!)
- `\begin{examenbox}` → Exam tips and important questions
- `\begin{warningbox}` → Critical warnings
- `\begin{theorieblok}` → Theory and definitions  
- `\begin{oefenblok}` → Exercises and examples

## 📊 Core Features
- `\frm{Label}{math}{notes}` → Adds formula to formularium
- `\sym{symbol}{name}{unit}` → Symbol with explanation (first use only)
- `\fig[width]{path}{caption}{label}` → Standard figure

## 📐 Math Shortcuts

### Derivatives
- `\dd{y}{x}` → dy/dx
- `\pd{f}{x}` → ∂f/∂x  
- `\dx, \dy, \dt` → Differential elements

### Vectors & Brackets
- `\vec{v}` → **v** (bold)
- `\uvec{n}` → **n̂** (unit vector)
- `\abs{x}` → |x|
- `\norm{v}` → ‖v‖
- `\paren{...}`, `\bracket{...}`, `\curlybrace{...}`

### Quick Fractions
- `\half, \third, \quarter` → ½, ⅓, ¼

### Number Sets
- `\RR, \NN, \ZZ, \QQ, \CC` → ℝ, ℕ, ℤ, ℚ, ℂ

## 🔢 Units (siunitx shortcuts)
- `\km, \kmh, \ms` → km, km/h, m/s
- `\degC` → °C
- `\kW, \MW` → kW, MW
- `\kPa, \MPa` → kPa, MPa

Usage: `\SI{100}{\km}` → 100 km

## ✏️ Emphasis
- `\concept{text}` → Blue bold for new concepts
- `\belangrijk{text}` → Red bold for important items

## 📋 Lists

### Bullet List (itemize)
```latex
\begin{itemize}
    \item First item
    \item Second item
\end{itemize}
```

### Numbered List (enumerate)
```latex
\begin{enumerate}
    \item First step
    \item Second step
\end{enumerate}
```

### Description List
```latex
\begin{description}
    \item[Term] Definition
    \item[Another] Description
\end{description}
```

## 📊 Tables

```latex
\begin{table}[H]
\centering
\caption{Table title}
\begin{tabular}{lcc}
\toprule
\textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
\midrule
Data 1 & Data 2 & Data 3 \\
More   & Data   & Here \\
\bottomrule
\end{tabular}
\end{table}
```

## 📈 Graphs (TikZ/pgfplots)

### Function Plot
```latex
\begin{tikzpicture}
\begin{axis}[
    xlabel={$x$},
    ylabel={$f(x)$},
    grid=major
]
\addplot[blue, thick, domain=0:4] {x^2};
\addlegendentry{$f(x) = x^2$}
\end{axis}
\end{tikzpicture}
```

### Data Plot
```latex
\begin{tikzpicture}
\begin{axis}[
    xlabel={Time [s]},
    ylabel={Speed [m/s]}
]
\addplot[mark=*, blue] coordinates {
    (0,0) (1,2) (2,4) (3,6)
};
\end{axis}
\end{tikzpicture}
```

### Simple Diagram
```latex
\begin{tikzpicture}
\draw[thick] (0,0) rectangle (2,1);
\draw[thick, fill=blue!20] (3,0.5) circle (0.5);
\draw[->, thick] (2,0.5) -- (2.5,0.5);
\end{tikzpicture}
```

## 🎯 Typical Workflow

```latex
\documentclass[a4paper,11pt]{report}
\usepackage{school-macros}
\usepackage{siunitx}

\begin{document}

\chapter{Chapter Title}

\frm{Energy}{E = mc^2}{Energy-mass equivalence}
\sym{v}{Velocity}{m/s}

\begin{examenbox}
Important exam tip...
\end{examenbox}

\begin{oefenblok}
Exercise content...
\end{oefenblok}

\appendix
\printsymbols
\printformularium

\end{document}
```

## ⚡ Remember
1. **Compile twice** for formularium and symbol list
2. Use `\frm` for all important formulas
3. Use `\sym` on first mention of symbols
4. Always use `\SI{value}{unit}` for units

---
**That's it! Simple, clean, effective.**
