# build.ps1
# Build script for School LaTeX documents using latexmk

param (
    [string]$File = "macro_usage_guide.tex"
)

Write-Host "Building $File..." -ForegroundColor Cyan

# Ensure output directory exists if we wanted one, but stay simple for now
# We use -pdf for PDF output, -interaction=nonstopmode to avoid hanging,
# and -file-line-error for easier debugging.
latexmk -pdf -interaction=nonstopmode -file-line-error -quiet $File

if ($LASTEXITCODE -eq 0) {
    Write-Host "Build Successful!" -ForegroundColor Green
} else {
    Write-Host "Build failed or finished with warnings. Check the log file." -ForegroundColor Red
}

# Cleanup auxiliary files but keep the PDF
latexmk -c -quiet $File
