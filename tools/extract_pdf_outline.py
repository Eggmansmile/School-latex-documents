from __future__ import annotations

import fitz  # PyMuPDF
from pathlib import Path


def print_doc_summary(path: Path, toc_limit: int = 60, sample_pages: int = 2, sample_lines: int = 35) -> None:
    print("=" * 100)
    print(path.name)
    if not path.exists():
        print("MISSING")
        return

    doc = fitz.open(path)
    print(f"pages: {doc.page_count}")

    toc = doc.get_toc(simple=True)
    print(f"toc entries: {len(toc)}")
    if toc:
        print("-- toc (first entries) --")
        for level, title, page in toc[:toc_limit]:
            indent = "  " * max(level - 1, 0)
            print(f"{indent}- p{page}: {title}")

    effective_sample_pages = doc.page_count if doc.page_count <= 8 else min(sample_pages, doc.page_count)
    for page_index in range(effective_sample_pages):
        text = doc.load_page(page_index).get_text("text")
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        print(f"\n-- page {page_index + 1} sample (first {sample_lines} lines) --")
        for ln in lines[:sample_lines]:
            print(ln)

    # Scan for likely exercise headings to infer structure when no TOC exists.
    needles = [
        "Hoofdstuk",
        "HOOFDSTUK",
        "Oefening",
        "OEFENING",
        "Vraag",
        "VRAAG",
        "Exercise",
        "Question",
    ]
    hits: list[tuple[int, str]] = []
    for page_index in range(doc.page_count):
        text = doc.load_page(page_index).get_text("text")
        for raw in text.splitlines():
            line = raw.strip()
            if not line:
                continue
            if any(n in line for n in needles):
                hits.append((page_index + 1, line))

    if hits:
        print("\n-- detected headings (first 120 hits) --")
        for page, line in hits[:120]:
            print(f"p{page}: {line}")

    doc.close()


def main() -> None:
    workspace_root = Path(__file__).resolve().parents[1]

    desired_names = {
        "MATHSYS_oefeningenbundel_2526.pdf",
        "MATHSYS_voorbeeldexamen.pdf",
        "MATHSYS_formularium.pdf",
    }

    found: dict[str, Path] = {}
    for pdf in workspace_root.rglob("*.pdf"):
        if pdf.name in desired_names:
            found[pdf.name] = pdf

    missing = sorted(desired_names - set(found.keys()))
    if missing:
        print("Missing PDFs (by name) under workspace:")
        for name in missing:
            print(f"- {name}")
        print("\nFound PDFs:")
    else:
        print("Found all target PDFs:\n")

    for name in sorted(found.keys()):
        print_doc_summary(found[name])


if __name__ == "__main__":
    main()
