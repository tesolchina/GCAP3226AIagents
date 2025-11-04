#!/usr/bin/env python3
"""
Plain PDF to Markdown converter

Goal: Extract raw text from a PDF and write it to a .md file without
introducing any additional content (no headers, no page labels, no metadata).

Notes:
- We rely on pdfplumber for text extraction as it generally preserves
  reading order well enough for academic PDFs.
- We do not inject any Markdown formatting. The output file has a .md
  extension so it renders in Markdown viewers, but the contents are plain text.
"""

import argparse
import os
from pathlib import Path
import sys

try:
    import pdfplumber
except Exception as exc:
    print("Error: pdfplumber is required. Install via 'pip install pdfplumber'.")
    print(f"Details: {exc}")
    sys.exit(1)


def convert_pdf_to_md_plain(pdf_path: str, output_path: str | None = None) -> str:
    """
    Convert a PDF to a Markdown (.md) file by extracting raw text only.

    - Does not add headers, footers, or any extra annotations
    - Preserves page text order as returned by pdfplumber
    - Inserts a single newline between pages to avoid accidental word joins

    Returns the path to the written markdown file.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if output_path is None:
        pdf_stem = Path(pdf_path).stem
        output_path = str(Path(pdf_path).with_name(f"{pdf_stem}.md"))

    collected: list[str] = []

    with pdfplumber.open(pdf_path) as pdf:
        for idx, page in enumerate(pdf.pages):
            # Basic text extraction without additional layout artifacts
            # Using default extract_text tends to balance fidelity and simplicity
            page_text = page.extract_text() or ""
            # Append page text; add a single newline between pages (but not extra labels)
            if idx > 0:
                collected.append("\n")
            collected.append(page_text)

    text = "".join(collected)

    # Ensure directory exists
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a PDF to a .md file by extracting raw text only (no added content)."
        )
    )
    parser.add_argument("pdf", help="Path to the source PDF file")
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output .md path. Defaults to the PDF name with .md in the same folder.",
    )
    args = parser.parse_args()

    try:
        out_path = convert_pdf_to_md_plain(args.pdf, args.output)
        print(out_path)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()


