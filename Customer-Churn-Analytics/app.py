import streamlit as st
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="European Bank Analytics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# SESSION STATE
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ==========================================
# IMPORT PAGES
# ==========================================
from page.overall import show_overall
from page.geography import show_geography
from page.age_tenure import show_age_tenure
from page.high_value_customer import show_high_value

# ==========================================
# LOAD CSS
# ==========================================
def load_css():
    css_path = Path(__file__).parent / "style" / "style.css"

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# ==========================================
# HOME PAGE
# ==========================================
if st.session_state.page == "Home":

    st.markdown(
        '<div class="home-title">🏦 European Central Bank Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-subtitle">Customer Segmentation & Churn Pattern Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
    '<h3 class="dashboard-title">🚀 Choose a Dashboard</h3>',
    unsafe_allow_html=True
)

    # First Row
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.info("### 📊 Overall Summary\nExecutive KPI Dashboard")

        if st.button(
            "Open Overall Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "Overall"
            st.rerun()

    with col2:
        st.info("### 🌍 Geography visualization\nRegional Churn Analysis")

        if st.button(
            "Open Geography Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "Geography"
            st.rerun()

    st.write("")
    st.write("")

    # Second Row
    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.info("### 👥 Age & Tenure Analysis\nCustomer Demographics")

        if st.button(
            "Open Age Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "Age"
            st.rerun()

    with col4:
        st.info("### 💎 High-Value Customer Explorer\nHigh value Customer Analytics")

        if st.button(
            "Open High Value Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "High Value"
            st.rerun()

# ==========================================
# OTHER PAGES
# ==========================================
elif st.session_state.page == "Overall":
    show_overall()

elif st.session_state.page == "Geography":
    show_geography()

elif st.session_state.page == "Age":
    show_age_tenure()

elif st.session_state.page == "High Value":
    show_high_value()
