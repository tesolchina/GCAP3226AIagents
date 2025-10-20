#!/usr/bin/env python3
"""
Wrapper script to convert the specified Team3 Typhoon PDF to Markdown
using the plain extractor (no injected content).
"""

import os
from pathlib import Path
import sys

# Allow running directly regardless of CWD
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

sys.path.insert(0, str(SCRIPT_DIR))

from plain_pdf_to_md import convert_pdf_to_md_plain  # type: ignore


def main() -> None:
    pdf_path = (
        "/Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/"
        "2018TakagietalTrackanalysisandstormsurgeinvestigationof2017TyphoonHatowerethewarningsignalsissuedinMacauandHongKongtimedappropriately.pdf"
    )

    out_md = (
        "/Users/simonwang/Documents/Usage/GCAP3226/Team3_Typhoon/02_Data_Collection/"
        "2018TakagietalTrackanalysisandstormsurgeinvestigationof2017TyphoonHatowerethewarningsignalsissuedinMacauandHongKongtimedappropriately.md"
    )

    try:
        result = convert_pdf_to_md_plain(pdf_path, out_md)
        print(result)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()


