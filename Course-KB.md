# COMP 424 Knowledge Base

The lecture PDFs are the instructor originals. The linked Markdown files make slide text searchable in Obsidian; use the PDFs to check diagrams, equations, and exact formatting.

## Lectures

| Lecture | Original slides | Searchable text |
| --- | --- | --- |
| 1. Introduction | [PDF](<slides/L1-Intro.pdf>) | [Text](<extract-slides/L1-Intro.md>) |
| 2. Uninformed Search | [PDF](<slides/L2 Uninformed Search.pdf>) | [Text](<extract-slides/L2 Uninformed Search.md>) |
| 3. Informed Search | [PDF](<slides/L3 Informed Search.pdf>) | [Text](<extract-slides/L3 Informed Search.md>) |
| 4. Optimization | [PDF](<slides/L4 Optimization.pdf>) | [Text](<extract-slides/L4 Optimization.md>) |

## Adding a lecture

Place the new instructor PDF in `slides/`, run `python extract_slides.py`, and add a row above. The script requires PyMuPDF (`pip install pymupdf`) and generates a separate Markdown file with one heading per slide.
