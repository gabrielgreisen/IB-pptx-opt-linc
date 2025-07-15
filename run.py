"""
Easy runner for the buyers presentation tool.

Edit the parameters in the CONFIG SECTION below and run:

    python3 run.py

Your PowerPoint deck will be generated automatically.
"""

import pandas as pd
from pptx import Presentation
from dispatcher import run_strips_template

# ===============================
# 🔧 CONFIG SECTION - adjust here
# ===============================

EXCEL_FILE = "database_strips_v4stale.xlsx"
SHEET_NAME = "Python Strip Mask"
TEMPLATE_FILE = "template.pptx"
OUTPUT_FILE = "buyers_presentation.pptx"
TEMPLATE_NUMBER = 1
USECOLS = "B:L"

# ===============================
# 🚀 Loading data
# ===============================
print("📂 Loading Excel data...")
df = pd.read_excel(
    EXCEL_FILE,
    sheet_name=SHEET_NAME,
    header=1,   # headers in row 2
    usecols=USECOLS
)
df = df.dropna(subset=['pb_id'])

print(f"✅ Loaded {len(df)} buyers from '{EXCEL_FILE}'.")

# ===============================
# 🚀 Loading PowerPoint template
# ===============================
print("📂 Loading PowerPoint template...")
prs = Presentation(TEMPLATE_FILE)
print(f"✅ Found {len(prs.slide_layouts)} slide layouts in '{TEMPLATE_FILE}'.")
for i, layout in enumerate(prs.slide_layouts):
    print(f"   Layout {i}: {layout.name}")

# ===============================
# 🚀 Execute
# ===============================
print("🚀 Building presentation...")
run_strips_template(TEMPLATE_NUMBER, prs=prs, df=df)
prs.save(OUTPUT_FILE)
print(f"✅ Presentation saved as '{OUTPUT_FILE}'")
