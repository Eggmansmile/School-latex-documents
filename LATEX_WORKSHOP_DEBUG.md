# LaTeX Workshop Debugging Guide

## Issues Fixed

### 1. **Missing Packages Error**
**Problem:** When you build, LaTeX Workshop fails because packages are missing.

**Solution:** The configuration has been updated to use **latexmk** as the primary build tool, which automatically:
- Runs pdflatex multiple times if needed
- Handles package dependencies better
- Works more reliably with complex documents

### 2. **Configuration Changes Made**

Updated `.vscode/settings.json` to include:

- **latexmk recipe** (recommended): Uses `latexmk` which is more robust
- **pdflatex × 2 recipe**: Runs pdflatex twice for cross-references
- **Single pdflatex recipe**: Fallback option

## How to Build

### Option 1: Using Command Palette (Recommended)
1. Press `Ctrl+Shift+P`
2. Type: `LaTeX Workshop: Build with recipe`
3. Select **"latexmk (pdflatex)"**

### Option 2: Using Keyboard Shortcut
- Press `Ctrl+Alt+B` to build with the default recipe

### Option 3: Using the LaTeX Workshop Sidebar
1. Click the TeXify icon in the activity bar (left sidebar)
2. Click the "Build LaTeX project" button

## Troubleshooting

### If Build Still Fails:

1. **Check Output Log**
   - Click: View → Output
   - Select: "LaTeX Workshop" from dropdown
   - Look for error messages

2. **Clean Build Files**
   - Command Palette: `LaTeX Workshop: Clean up auxiliary files`
   - Then rebuild

3. **Check Installed Packages**
   - Open Terminal
   - Run: `tlmgr list --only-installed | find "enumitem"`
   - Verify packages are there

4. **View Root File**
   - Ensure your main file is: `Thermische_en_Fluidumwetenschappen.tex`
   - LaTeX Workshop should auto-detect it, but you can set it manually:
     - Command Palette: `LaTeX Workshop: Set root file`

### If You Get "pdflatex: command not found"

This means LaTeX is not in your system PATH:

**Solution:**
1. Find your TeX Live installation: `where pdflatex` (in PowerShell)
2. Add to environment variables or use full path in settings

## Build Process Explanation

**latexmk** does this automatically:
```
1. Run pdflatex → generates .aux, .toc files
2. Check if cross-references need updating
3. Run pdflatex again if needed
4. Generate final PDF
```

Without latexmk, you'd need to run pdflatex manually multiple times.

## Installed Packages

All required packages have been installed via `tlmgr`:
- enumitem
- pdfpages
- pgf (includes tikz)
- fancyhdr
- microtype
- soul
- mdframed
- needspace
- zref
- titlesec
- caption
- setspace
- parskip
- tcolorbox
- pdflscape
- wrapfig

## Settings Explanation

| Setting | Purpose |
|---------|---------|
| `autoBuild.run: "never"` | Don't build automatically; requires manual build |
| `view.pdf.viewer: "tab"` | Show PDF in VS Code tab (not external viewer) |
| `message.error.show: true` | Display error notifications |
| `linting.enabled: true` | Check for LaTeX syntax issues |

## Next Steps

1. **Open your LaTeX file**
2. **Use Ctrl+Alt+B to build**
3. **Check the Output panel for errors**
4. **If successful, PDF opens in a new tab**

If you still encounter issues, check the "LaTeX Workshop" output channel for detailed error messages.
