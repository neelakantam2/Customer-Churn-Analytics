import streamlit as st

def sidebar_filters(df):
    import base64
    def get_logo():
        with open("assets/logo.png", "rb") as IMG:
            return base64.b64encode(IMG.read()).decode()
    logo = get_logo()
    st.sidebar.markdown(
    f"""
    <div style="display:flex; justify-content:center; margin-bottom:20px;">
        <img src="data:image/png;base64,{logo}"
             style="
                width:200px;
                height:20cg0px;
                border-radius:50%;
                object-fit:cover;
                background:white;
                padding:10px;
                border:3px solid white;
                box-shadow:0 4px 10px rgba(0,0,0,0.15);
             ">
    </div>
    """,
    unsafe_allow_html=True
)
    st.sidebar.header("Filters")
    
    # Geography Filter
    geography = st.sidebar.multiselect(
        "🌍 Geography",
        options=sorted(df["Geography"].unique()),
        default=sorted(df["Geography"].unique())
    )
    # Gender Filter
    gender = st.sidebar.multiselect(
        "Gender",
        sorted(df["Gender"].unique()),
        default=sorted(df["Gender"].unique())
    )
    # Age Group Filter
    age_group = st.sidebar.multiselect(
        "🎂 Age Group",
        options=df["Age_Group"].dropna().unique().tolist(),
        default=df["Age_Group"].dropna().unique().tolist()
    )

    # Credit Score Band Filter
    credit_band = st.sidebar.multiselect(
        "💳 Credit Score Band",
        options=df["Credit_Band"].dropna().unique().tolist(),
        default=df["Credit_Band"].dropna().unique().tolist()
    )

    # Tenure Group Filter
    tenure_group = st.sidebar.multiselect(
        "📅 Tenure Group",
        options=df["Tenure_Group"].dropna().unique().tolist(),
        default=df["Tenure_Group"].dropna().unique().tolist()
    )

    # Balance Segment Filter
    balance_segment = st.sidebar.multiselect(
        "💰 Balance Segment",
        options=df["Balance_Segment"].unique().tolist(),
        default=df["Balance_Segment"].unique().tolist()
    )
    customer_status = st.sidebar.multiselect(
        "Customer Status",
        sorted(df["CustomerStatus"].unique()),
        default=sorted(df["CustomerStatus"].unique())
    )
     # Apply Filters
    filtered_df = df[
        (df["Geography"].isin(geography)) &
        (df["Gender"].isin(gender)) &
        (df["CustomerStatus"].isin(customer_status)) &
        (df["Age_Group"].isin(age_group)) &
        (df["Credit_Band"].isin(credit_band)) &
        (df["Tenure_Group"].isin(tenure_group)) &
        (df["Balance_Segment"].isin(balance_segment))

    ]
    return filtered_df