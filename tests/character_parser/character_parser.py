import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(project_root)

import unittest

from src.utils.character_sheet_parser import parse_pdf

filename = "Lalkish Alistair_printed.pdf"
filepath = os.path.join(current_dir, filename)

print(f"{parse_pdf(filepath)}")

#
# filename = "Lalkish Alistair.pdf"
# filepath = os.path.join(current_dir, filename)
#
# print(f"{parse_pdf(filepath)}")
