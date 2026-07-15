import streamlit as st

from utils.data_loader import load_data
from utils.filters import sidebar_filters
from utils.kpi import (
    total_customers,
    high_value_customers,
    high_value_churn_ratio,
    average_balance
)
from utils.charts import (
    high_value_geography,
    high_value_age,
    high_balance_churners, 
    salary_vs_balance_churn,
    revenue_risk_churn,
    financial_stability_heatmap



)
def show_high_value():

    df = load_data()

    filtered_df = sidebar_filters(df)

    if st.button("🏠 Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("💎 High-Value Customer Explorer")

 # ---------------- KPI Cards ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total Customers", f"{total_customers(filtered_df):,}")
    col2.metric("✅ High-Value Customers", f"{len(high_value_customers(filtered_df)):,}")
    col3.metric("📉 Churn Rate", f"{high_value_churn_ratio(filtered_df):.2f}%")
    col4.metric("💰 Avg Balance", f"€{average_balance(filtered_df):,.2f}")

#----------------- Row 1 ----------------
    col1, col2 = st. columns(2)
    with col1 :
         with st.container(border=True):
            st.plotly_chart(
            high_value_geography(filtered_df)  ,
            use_container_width= True
             )
    with col2:
        with st. container(border= True):
            st.plotly_chart(
            high_value_age(filtered_df),
            use_container_width= True
            )
    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            st.plotly_chart(
            high_balance_churners(filtered_df),
            use_container_width=True,
        )
    with col4:
        with st.container(border=True):
            st.plotly_chart(
            salary_vs_balance_churn(filtered_df),
            use_container_width= True
            )
    col5, col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            st.plotly_chart(
             revenue_risk_churn(filtered_df),
             use_container_width= True
            )
    with col6:
        with st.container(border=True):
            st.plotly_chart(
            financial_stability_heatmap(filtered_df),
            use_container_width=True
            )