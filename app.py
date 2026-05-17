"""
OMAC Hand Hygiene Tool — Streamlit Launcher
By S M Baqir

This Streamlit app serves the HTML-based hand hygiene assessment tool.
It handles result logging to Excel files server-side.
"""
import streamlit as st
import streamlit.components.v1 as components
import os
import json
import pandas as pd
from datetime import datetime
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OMAC Hand Hygiene Tool",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Ensure results folder exists ─────────────────────────────────────────────
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  #MainMenu, footer, header { visibility: hidden; }
  .stApp { background: #0a0c10; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none; }
</style>
""", unsafe_allow_html=True)

# ── Load the HTML tool ────────────────────────────────────────────────────────
html_path = Path(__file__).parent / "index.html"
if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Inject Streamlit bridge script before </body>
    bridge_script = """
<script>
// Streamlit result bridge
window.saveResultsToStreamlit = function(data) {
    window.parent.postMessage({
        type: 'omac_results',
        data: data
    }, '*');
};
</script>
"""
    html_content = html_content.replace("</body>", bridge_script + "</body>")
    components.html(html_content, height=900, scrolling=False)
else:
    st.error("❌ index.html not found. Make sure it is in the same directory as app.py")

# ── Sidebar: Results viewer ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧴 OMAC Results Log")
    st.caption("by S M Baqir")
    st.divider()

    excel_files = sorted(RESULTS_DIR.glob("*.xlsx"), reverse=True)
    if excel_files:
        st.markdown(f"**{len(excel_files)} session(s) recorded**")
        selected = st.selectbox(
            "View session:",
            options=excel_files,
            format_func=lambda p: p.stem
        )
        if selected:
            try:
                df = pd.read_excel(selected)
                st.dataframe(df, use_container_width=True)
                with open(selected, "rb") as f:
                    st.download_button(
                        "⬇ Download",
                        f,
                        file_name=selected.name,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            except Exception as e:
                st.error(f"Could not read file: {e}")
    else:
        st.info("No results yet. Complete an assessment to generate logs.")

    st.divider()
    st.markdown("""
    **Instructions:**
    1. Enter name & employee code
    2. Click **Start Camera**
    3. Allow camera access
    4. Follow the 6 WHO steps
    5. Export results to Excel

    **Tip:** Press `→` to skip a step during testing.
    """)
    st.caption("OMAC Hand Hygiene Tool v1.0 · WHO 6-Step Protocol")
