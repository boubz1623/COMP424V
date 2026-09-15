"""Build searchable Markdown from the lecture PDFs in slides/.

Requires PyMuPDF: pip install pymupdf
"""

from pathlib import Path
import re

import pymupdf


ROOT = Path(__file__).resolve().parent
SLIDES = ROOT / "slides"
OUTPUT = ROOT / "extract-slides"


def extract(pdf_path: Path) -> Path:
    output_path = OUTPUT / f"{pdf_path.stem}.md"
    with pymupdf.open(pdf_path) as pdf:
        sections = [
            f"# {pdf_path.stem}",
            "",
            f"> Source: [original PDF](<../slides/{pdf_path.name}>) · {len(pdf)} slides. "
            "Text extraction may omit figures and alter equations; check the PDF.",
        ]
        for number, page in enumerate(pdf, start=1):
            content = page.get_text(sort=True).strip()
            # Code fences preserve approximate slide layout without treating source text as Markdown.
            fence = "`" * max(3, max((len(run) for run in re.findall(r"`+", content)), default=0) + 1)
            sections.extend(("", f"## Slide {number}", "", f"{fence}text", content or "[No extractable text on this slide.]", fence))
    OUTPUT.mkdir(exist_ok=True)
    output_path.write_text("\n".join(sections) + "\n", encoding="utf-8")
    return output_path


if __name__ == "__main__":
    for path in sorted(SLIDES.glob("*.pdf")):
        print(extract(path).relative_to(ROOT))
