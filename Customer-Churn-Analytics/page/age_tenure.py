import streamlit as st

from utils.data_loader import load_data
from utils.filters import sidebar_filters
from utils.kpi import (
    total_customers,
    active_customers,
    overall_churn_rate,
    average_balance
)

from utils.charts import (
    AgeGroup_churn_chart,
    Average_balance_by_age,
    TenureGroup_churn_chart,
    age_tenure_heatmap,
    average_credit_by_agegroup,
    average_credit_by_tenuregroup,
    customer_by_age,
    customer_by_tenure,
)
def show_age_tenure():

    df = load_data()
    filtered_df = sidebar_filters(df)

    if st.button("🏠 Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("👥 Age & Tenure Analysis")

    # ---------------- KPI Cards ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total Customers", f"{total_customers(filtered_df):,}")
    col2.metric("✅ Active Customers", f"{active_customers(filtered_df):,}")
    col3.metric("📉 Churn Rate", f"{overall_churn_rate(filtered_df):.2f}%")
    col4.metric("💰 Avg Balance", f"€{average_balance(filtered_df):,.2f}")

    st.divider()
#    # ---------------- Row 1 ----------------
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.plotly_chart(
            AgeGroup_churn_chart(filtered_df),
            use_container_width=True,
            )
    with col2:
        with st.container(border=True):
            st.plotly_chart(
           customer_by_age(filtered_df),
            use_container_width=True,
            )
    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.plotly_chart(
           Average_balance_by_age(filtered_df),
            use_container_width=True,
            )
    with col4:
        with st.container(border=True):
            st.plotly_chart(
            TenureGroup_churn_chart(filtered_df),
            use_container_width=True,
            )
    col5, col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            st.plotly_chart(
            customer_by_tenure(filtered_df),
            use_container_width=True,
            )
    with col6:
        with st.container(border=True):
            st.plotly_chart(
            age_tenure_heatmap(filtered_df),
            use_container_width=True,
            )
    col7, col8 = st.columns(2)
    with col7:
        with st.container(border=True):
            st.plotly_chart(
            average_credit_by_agegroup(filtered_df),
            use_container_width=True,
            )
    with col8:
        with st.container(border=True):
            st.plotly_chart(
            average_credit_by_tenuregroup(filtered_df),
            use_container_width=True,
            )