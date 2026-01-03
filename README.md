# Wiskunde voor Systemen — Oefeningen & Oplossingen

## Beschrijving

Dit is een **samenstelling van universiteits-oefeningen in LaTeX** voor het vak **"Wiskunde voor Systemen"** & **Warmte en stromingen** aan **KU Leuven**, onderdeel van het **Industrieel Ingenieurschap (EM 2)** programma.

Het document bevat systematisch uitgewerkte oefeningen en gedetailleerde stap-voor-stap oplossingen voor alle behandelde onderwerpen.

---

## Inhoud Wiskunde

### Formularium
Een naslagwerk met standaardformules voor:
- Laplacetransformatie
- Fouriertransformatie
- Fourierreeksen

### 8 Hoofdstukken Oefeningen

1. **Signalen en Systemen - Eerste Kennismaking**
2. **Basissignalen en Bewerkingen**
3. **Laplacetransformatie**
4. **Fouriertransformatie**
5. **Fourierreeksen**
6. **LTC-Systemen**
7. **Eigenwaarden en Eigenvectoren**
8. **Examengerichte Oefeningen**

**Totaal:** 44+ oefeningen met volledige uitwerkingen

### Oplossingen
Bij elke oefening hoort een gedetailleerde oplossing met:
- Stap-voor-stap berekeningen
- Verwijzingen naar het formularium
- Grafische voorstellingen (TikZ-diagrammen)
- Verificatie van resultaten

---

## Document

- **Bestand:** `MATHSYS_oefeningen.tex`
- **Format:** LaTeX (pdflatex)
- **Output:** `MATHSYS_oefeningen.pdf`
- **Taal:** Nederlands
- **Omvang:** 87 pagina's

---

## Inhoud Warmte en Stormingen
### Formularium

### 2 Hoofdstukken Theorie, 1 hoofdstuk Oefeningen

### Oplossingen
Bij elke oefening hoort een gedetailleerde oplossing met:
- Stap-voor-stap berekeningen
- Verwijzingen naar het formularium
- Grafische voorstellingen (TikZ-diagrammen)
- Verificatie van resultaten

## document
- **Bestand:** `Thermische_en_Fluidumwetenschappen.tex`
- **Format:** LaTeX (pdflatex)
- **Output:** `Thermische_en_Fluidumwetenschappen.pdf`

- **Taal:** Nederlands

**Benodigde pakketten:** tikz, amsmath, amssymb, geometry, enumitem, hyperref

---
---

## Toekomstige Uitbreidingen

Geplande toevoegingen voor komende versies:
- **Wisselstromingen (AC-circuits)** — Impedantie, faserespons, resonantie

---

**Datum:** December 2025  
**Status:** Compleet ✓

---

## LaTeX voorbeelden & template 📐
In de map `latex_templates/` vind je een kant-en-klare template met korte, praktische voorbeelden die je direct kunt hergebruiken:

- **Bestand:** `latex_templates/template_examples.tex`
- **Inbegrepen voorbeelden:**
  - Eenheden met `siunitx` (gebruik `\SI{120}{\milli\metre\per\minute}`)
  - Slimme verwijzingen met `cleveref` (gebruik `\cref{fig:label}`)
  - Professionele tabellen met `booktabs`
  - Subfiguren met `subcaption`
  - In-line theorieboxen met `tcolorbox`
  - Aangepaste opsommingen met `enumitem`

Snelle build-commando's (aanbevolen):

- `latexmk -pdf latex_templates/template_examples.tex`  (handig: verzorgt meerdere runs automatisch)
- of: `pdflatex -interaction=nonstopmode -file-line-error latex_templates/template_examples.tex` (run 2× als je referenties wilt updaten)

Aanbevolen TeX-packages (kan met `tlmgr` worden geïnstalleerd):

```
tlmgr install siunitx cleveref tcolorbox booktabs subcaption enumitem microtype latexmk latexindent chktex
```

Opmerking: het hoofddocument laadt sommige van deze pakketten op een beveiligde manier (guarded) zodat het nog steeds compileert als een pakket ontbreekt — maar het is aanbevolen om de hierboven genoemde pakketten te installeren voor volledige functionaliteit.

Extra voorbeelden die ik heb toegevoegd aan `latex_templates/template_examples.tex`:

- **PGFPlots**: eenvoudige plots en `groupplots` voor meerdere subplots.
- **tcolorbox**: theorema-/definitieboxen (andere stijlen mogelijk met tcolorbox-libraries).
- **listings** (codeblokken) en optioneel **minted** (snelle highlight; vereist `--shell-escape` en Pygments).
- **glossaries**: definities en acroniemen (werkt beter als je `makeglossaries` of `makeindex` hebt).
- **biblatex**: voorbeeldbibliografie (vergt `biber` of `bibtex` afhankelijk van setup).
- **multicol**: eenvoudige cheat-sheet lay-outs.

Extra installatie/compile tips:

- Voor `minted` gebruik: compileer met `pdflatex -shell-escape` of `latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode -file-line-error"` en zorg dat Python/Pygments geïnstalleerd is.
- Voor `biblatex`/`biber`: gebruik `biber` in de build (or use `latexmk -pdf` which runs biber automatically if configured).
- Voor `glossaries`: run `makeglossaries <jobname>` after the first LaTeX run, or use `latexmk`.

Aanbevolen extra installatie-commando's:

```
tlmgr install pgfplots listings biblatex biber glossaries multicol
```

Als je wilt, kan ik:
- Deze snippets verder uitbreiden (bijv. een kant-en-klare minted-voorbeeldsectie met instructies), of
- Een VS Code task toevoegen die `latexmk` uitvoert met `-shell-escape` voor projecten die `minted` gebruiken.


---

## Productietechnologie

Kort overzicht van de map `Productietechnologie`:

- **Bestand:** `Productietechnologie/ProductieTechnologie-Samenvatting-RubenRyckaert.tex`
- **Inhoud:** samenvattingen, voorbeelden, en een `formularium`-sectie; afbeeldingen in `Productietechnologie/assets/`.
- **Macros:** `productie-macros.sty` bevat helpers zoals `\frm{...}`, `\fig[...]`, en `\autofig[...]` om formules en afbeeldingen consistent te registreren en in te voegen.
- **Benodigde pakketten (aanbevolen):** `tikz`, `tcolorbox`, `siunitx`, `pgfplots`, `booktabs`, `subcaption`, `listings`, `biblatex` (optioneel), `glossaries` (optioneel).
- **Build:** gebruik `latexmk -pdf` binnen de map of de bestaande VS Code tasks; voor `minted` gebruik `-shell-escape`, en voor bibliografieën gebruik `biber` (of laat `latexmk` dat afhandelen).
- **Tip:** voer `tlmgr install pgfplots tcolorbox siunitx listings biblatex glossaries` uit om volledige voorbeeldondersteuning te krijgen.

---

## Notes & Troubleshooting
- If you see the warning "No hyphenation patterns were preloaded for the language 'Dutch'", install the Dutch hyphenation package and rebuild the TeX formats. For TeX Live / TinyTeX you can try:

  - `tlmgr install hyphen-dutch` (or `hyphen-nl`) and then `fmtutil-sys --all` to rebuild formats.

- The `formularium` feature writes an external file `<jobname>.fmr` at the end of each run and reads it when you place `\begin{formularium} ... \end{formularium}`. Run `pdflatex` twice after adding/removing formulas so the entries appear in place.

## Unified Workflow & Templates (New)

Located in `latex_templates/`, this repository now features a streamlined workflow:

- **`school-macros.sty`**: A high-readability, minimalist package. It includes:
  - Custom boxes: `conceptbox`, `warningbox`, `examenbox`, `procesbox`, `oefenblok`, `theorieblok`.
  - Formula management: `\frm{Title}{Formula}{Note}` (automatically builds a formularium).
  - Symbol management: `\sym{Symbol}{Description}{Unit}` (automatically builds a symbol list).
  - Modern typography: Pre-configured with `microtype`, `lmodern`, and `parskip`.
- **`new_document_template.tex`**: A clean template to start new school summaries.
- **`macro_usage_guide.tex`**: A comprehensive guide and live demo of all available macros.

### Optimized Build Process
To ensure all cross-references, symbol lists, and the formularium are generated correctly with a single command:

1. Open PowerShell in the project directory.
2. Run the provided build script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File latex_templates/build.ps1 -File your_file.tex
   ```
   *Note: This script uses `latexmk` for a reliable multi-pass build and automatic cleanup.*

