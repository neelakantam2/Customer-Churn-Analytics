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
    BalanceSegment_churn_chart,
    Geography_churn_chart,
    TenureGroup_churn_chart,
    TenureGroup_churn_chart,
    credit_score_chart,
    overall_churn_chart,
    churn_contribution_chart,
    churn_profile_chart
)

def show_overall():

    # Load data
    df = load_data()

    # Apply filters
    filtered_df = sidebar_filters(df)

    # Home button
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
        st.rerun()

    # KPI Calculations
    total = total_customers(filtered_df)
    active = active_customers(filtered_df)
    churn_rate = overall_churn_rate(filtered_df)
    avg_balance = average_balance(filtered_df)

    # Page Title
    st.title("📊 Overall Churn Summary")

    # KPI Row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="👥 Total Customers",
            value=f"{total:,}"
        )

    with col2:
        st.metric(
            label="✅ Active Customers",
            value=f"{active:,}"
        )

    with col3:
        st.metric(
            label="📉 Overall Churn Rate",
            value=f"{churn_rate:.2f}%"
        )

    with col4:
        st.metric(
            label="💰 Average Balance",
            value=f"€{avg_balance:,.2f}"
        )

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.plotly_chart(
            overall_churn_chart(filtered_df),
            use_container_width=True
    )

    with col2:
        with st.container(border=True):
            st.plotly_chart(
            Geography_churn_chart(filtered_df),
        use_container_width=True
    )

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.plotly_chart(
                AgeGroup_churn_chart(filtered_df),
                use_container_width=True
            )

    with col4:
        with st.container(border=True):
            st.plotly_chart(
                credit_score_chart(filtered_df),
                use_container_width=True
            )
    col5, col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            st.plotly_chart(
                TenureGroup_churn_chart(filtered_df),
        use_container_width=True
    )
    with col6:
        with st.container(border=True):
            st.plotly_chart(
                BalanceSegment_churn_chart(filtered_df),
                use_container_width=True
            )
    col7, col8 = st.columns(2)
    with col7:
        with st.container(border=True):
            st.plotly_chart(
                churn_contribution_chart(filtered_df),
                use_container_width=True
            )
    with col8:
        with st.container(border=True):
            st.plotly_chart(
                churn_profile_chart(filtered_df),
                use_container_width=True
            )
     