import streamlit as st
import pandas as pd
from pptx import Presentation
from dispatcher import run_strips_template

st.title("📊 Buyers Presentation Tool")

# Upload or path input
excel_file = st.text_input("Excel file path", value="database_strips_v4stale.xlsx")
sheet_name = st.text_input("Sheet name", value="Python Strip Mask")
template_file = st.text_input("PPT template path", value="template.pptx")
output_file = st.text_input("Output PPT file name", value="buyers_presentation.pptx")

template_number = st.number_input("Template number", min_value=1, max_value=5, value=1, step=1)

if st.button("Run Presentation"):
    try:
        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name,
            header=1,
            usecols="B:L"
        ).dropna(subset=['pb_id'])
        st.success(f"✅ Loaded {len(df)} buyers from '{excel_file}'.")

        prs = Presentation(template_file)
        run_strips_template(template_number, prs=prs, df=df)
        prs.save(output_file)
        st.success(f"✅ Presentation saved as '{output_file}'.")
    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")