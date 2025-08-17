import streamlit as st
from frontend.ui import render_ui
from backend.processor import process_data
from backend.visualizer import generate_visualizations  # ✅ updated function name
from backend.nlp_engine import analyze_text
from backend.report_generator import generate_report
from backend.ai_query import handle_query

# 🎯 Page Setup
st.set_page_config(page_title="Intelligent Data Assistant", layout="wide")
render_ui()

# 📁 File Upload
uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])
if uploaded_file:
    # 🔍 Process Data
    df = process_data(uploaded_file)
    st.success("✅ File processed successfully!")
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # 💬 Ask a Question
    query = st.text_input("💡 Ask a question about your data")
    if query:
        response = handle_query(query, df)
        st.write(response)

    # 📊 Auto Visualizations
    st.subheader("📊 Auto Visualizations")
    max_charts = st.slider("🎛️ How many charts to generate?", 1, 10, 5)
    plots = generate_visualizations(df, max_charts=max_charts)
    for fig in plots:
        st.pyplot(fig)

    # 🧠 NLP Analysis
    st.subheader("🧠 Text Analysis")
    analyze_text(df)

    # 📄 Report Generation
    if st.button("📝 Generate Report"):
        generate_report(df, response)
else:
    st.info("📁 Please upload a CSV file to begin.")

