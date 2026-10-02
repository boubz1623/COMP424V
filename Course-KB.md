# COMP 424 Knowledge Base

The lecture PDFs are the instructor originals. The linked Markdown files make slide text searchable in Obsidian; use the PDFs to check diagrams, equations, and exact formatting.

## Lectures

| Lecture | Original slides | Searchable text |
| --- | --- | --- |
| 1. Introduction | [PDF](<slides/L1-Intro.pdf>) | [Text](<extract-slides/L1-Intro.md>) |
| 2. Uninformed Search | [PDF](<slides/L2 Uninformed Search.pdf>) | [Text](<extract-slides/L2 Uninformed Search.md>) |
| 3. Informed Search | [PDF](<slides/L3 Informed Search.pdf>) | [Text](<extract-slides/L3 Informed Search.md>) |
| 4. Optimization | [PDF](<slides/L4 Optimization.pdf>) | [Text](<extract-slides/L4 Optimization.md>) |
| 5. Constraint Satisfaction Problems | [PDF](<slides/L5 CSPs.pdf>) | [Text](<extract-slides/L5 CSPs.md>) |
| 6. Game Playing | [PDF](<slides/L6 Game Playing.pdf>) | [Text](<extract-slides/L6 Game Playing.md>) |
| 7. Alpha-beta | [PDF](<slides/L7 Alpha-beta.pdf>) | [Text](<extract-slides/L7 Alpha-beta.md>) |
| 8. Monte Carlo Tree Search | [PDF](<slides/L8 MCTS.pdf>) | [Text](<extract-slides/L8 MCTS.md>) |
| 9. Searching Under Uncertainty | [PDF](<slides/L9 Search With Uncertainty.pdf>) | [Text](<extract-slides/L9 Search With Uncertainty.md>) |

## Adding a lecture

Place the new instructor PDF in `slides/`, run `python extract_slides.py`, and add a row above. The script requires PyMuPDF (`pip install pymupdf`) and generates a separate Markdown file with one heading per slide.
