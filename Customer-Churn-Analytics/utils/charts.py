import pandas as pd

import plotly.express as px


# ==========================================================
# Create High Value Customer column if it doesn't exist
# ==========================================================
def _prepare_dataframe(df):

    df = df.copy()

    if "HighValueCustomer" not in df.columns:
        df["HighValueCustomer"] = df["Balance"].apply(
            lambda x: "High Value" if x >= 100000 else "Regular"
        )

    return df


# ==========================================================
# 1. Overall Churn Rate (Donut Chart)
# ==========================================================
def overall_churn_chart(df):

    if df.empty:
        return px.pie(title="No data available")

    churn = (
        df["Exited"]
        .value_counts()
        .rename(index={0: "Retained", 1: "Churned"})
        .reset_index()
    )

    churn.columns = ["Status", "Customers"]

    fig = px.pie(
        churn,
        names="Status",
        values="Customers",
        hole=0.60,
        color="Status",
        color_discrete_map={
            "Retained": "#2E86DE",
            "Churned": "#E74C3C"
        },
        title="Overall Churn Rate"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        legend_title=""
    )
    fig.update_layout(
    width=450,
    height=450,
    title={
            "text":"Overall Churn Rate",
            "x": 0.25,
            "font":{"size":20}
        },)
    fig = apply_chart_theme(fig)
    return fig


# ==========================================================
# 2. Geography-wise Churn Rate
# ==========================================================
def Geography_churn_chart(df):

    if df.empty:
        return px.bar(title="Geography-wise Churn Rate")

    df = _prepare_dataframe(df)

    segment = (
        df.groupby("Geography")["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )

    fig = px.bar(
        segment,
        x="Geography",
        y="Churn Rate",
        color="Geography",
        text_auto=".2f",
        title="Geography-wise Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
        yaxis_title="Churn Rate (%)",
        xaxis_title="Country"
    )
    fig.update_layout(
    width=450,
    height=450)
    fig.update_layout(
        title={
            "text": "Geography-wise Churn Rate",    
            "x": 0.45,
            "font":{"size":20}
        }  
    )
    fig = apply_chart_theme(fig)
    return fig

# ==========================================================
# 3. Age Group-wise Churn Rate
# ==========================================================

def AgeGroup_churn_chart(df):

    if df.empty:
        return px.bar(title=" Churn Rate by Age Group")

    df = _prepare_dataframe(df)

    segment = (
        df.groupby("Age_Group")["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )

    fig = px.bar(
        segment,
        x="Age_Group",
        y="Churn Rate",
        color="Age_Group",
        text_auto=".2f",
        title="Churn Rate by Age Group"
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
        yaxis_title="Churn Rate (%)",
        xaxis_title="Age Group"
    )
    fig.update_layout(
    width=450,
    height=450,
    title={
            "x": 0.5,
            "font":{"size":20}
        },)
    fig = apply_chart_theme(fig)
    return fig
# ==========================================================
# 4. Credit Score-wise Churn Rate
# ==========================================================
def credit_score_chart(df):

    if df.empty:
        return px.bar(title="Credit Score-wise Churn Rate")

    df = _prepare_dataframe(df)

    segment = (
        df.groupby("CreditScore")["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )

    fig = px.bar(
        segment,
        x="CreditScore",
        y="Churn Rate",
        color="CreditScore",
        text_auto=".2f",
        title="Credit Score-wise Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
        yaxis_title="Churn Rate (%)",
        xaxis_title="Credit Score"
    )
    fig.update_layout(
    width=450,
    height=450,
    title={
            "x": 0.5,
            "font":{"size":20}
        },)
    fig = apply_chart_theme(fig)
    return fig
# ==========================================================
# 5. Tenure Group-wise Churn Rate
# ==========================================================
def TenureGroup_churn_chart(df):

    if df.empty:
        return px.bar(title=" Churn Rate by tenure Group")

    df = _prepare_dataframe(df)

    segment = (
        df.groupby("Tenure_Group")["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )

    fig = px.bar(
        segment,
        x="Tenure_Group",
        y="Churn Rate",
        color="Tenure_Group",
        text_auto=".2f",
        title="Churn Rate by Tenure Group"
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
        yaxis_title="Churn Rate (%)",
        xaxis_title="Tenure Group",
        title={
            "x": 0.5,
            "font":{"size":20}
        },
    )
    fig.update_layout(
    width=450,
    height=450)
    fig = apply_chart_theme(fig)
    return fig
# ==========================================================
# 6. Balance Segment-wise Churn Rate
# ==========================================================
def BalanceSegment_churn_chart(df):

    if df.empty:
        return px.bar(title="Balance Segment-wise Churn Rate")

    df = _prepare_dataframe(df)

    segment = (
        df.groupby("Balance_Segment")["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )

    fig = px.bar(
        segment,
        x="Balance_Segment",
        y="Churn Rate",
        color="Balance_Segment",
        text_auto=".2f",
        title="Balance Segment-wise Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
        yaxis_title="Churn Rate (%)",
        xaxis_title="Balance Segment",
        title={
            "x": 0.5,
            "font":{"size":20}
        },
    )
    fig.update_layout(
    width=450,
    height=450)
    fig = apply_chart_theme(fig)
    return fig
# ==========================================================
# 3. Churn Contribution by Segment
# ==========================================================
def churn_contribution_chart(df):

    if df.empty:
        return px.bar(title="No data available")

    df = _prepare_dataframe(df)

    contribution = (
        df[df["Exited"] == 1]
        .groupby("HighValueCustomer")
        .size()
        .reset_index(name="Churned Customers")
    )

    fig = px.bar(
        contribution,
        x="HighValueCustomer",
        y="Churned Customers",
        color="HighValueCustomer",
        text="Churned Customers",
        title="Churn Contribution by Segment"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        width=450,
        showlegend=False,
        yaxis_title="Customers",
        xaxis_title="Customer Segment",
        title={
            "x": 0.5,
            "font":{"size":20}
        },
    )
    fig = apply_chart_theme(fig)
    return fig


# ==========================================================
# 4. Churned vs Retained Profiles
# ==========================================================
def churn_profile_chart(df):

    if df.empty:
        return px.bar(title="No data available")

    profile = (
        df.groupby("Exited")
        .agg(
            Average_Balance=("Balance", "mean")
        )
        .reset_index()
    )

    profile["Status"] = profile["Exited"].replace({
        0: "Retained",
        1: "Churned"
    })

    fig = px.bar(
        profile,
        x="Status",
        y="Average_Balance",
        color="Status",
        text_auto=".0f",
        title="Average Balance: Churned vs Retained"
    )
    
    fig.update_layout(
        template="plotly_white",
        height=450,
        width=450,
        yaxis_title="Average Balance (€)",
        xaxis_title="",
        title={
            "x": 0.5,
            "font":{"size":20}
        },
    )
    fig = apply_chart_theme(fig)
    return fig


#---------------------------------------------------------
#page 2 
#---------------------------------------------------------

def customer_distribution_country(df):

    # Count customers in each country
    country_df = (
        df["Geography"]
        .value_counts()
        .reset_index()
    )

    country_df.columns = ["Country", "Customers"]

    fig = px.pie(
        country_df,
        names="Country",
        values="Customers",
        hole=0.60,                     # Donut chart
        color="Country",
        color_discrete_map={
            "France": "#1E88E5",
            "Germany": "#43A047",
            "Spain": "#FB8C00"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Customers: %{value}<br>Percentage: %{percent}<extra></extra>"
    )

    fig.update_layout(
        title={
            "text": "Customer Distribution by Country",
            "x": 0.5,
            "font":{"size":20}
        },
        height=450,
        showlegend=True,
        legend_title="Country",
        margin=dict(t=60, b=20, l=20, r=20)
    )
    fig = apply_chart_theme(fig)
    return fig

    
def customers_churn_country(df):

    total = df.groupby("Geography").size().rename("Total")
    churned = df[df["Exited"] == 1].groupby("Geography").size().rename("Churned")

    chart_df = pd.concat([total, churned], axis=1).fillna(0).reset_index()
    chart_df = chart_df.melt(
        id_vars="Geography",
        var_name="Status",
        value_name="Customers"
    )

    fig = px.bar(
        chart_df,
        x="Geography",
        y="Customers",
        color="Status",
        barmode="group",
        text="Customers",
        color_discrete_map={
            "Total": "#1E88E5",
            "Churned": "#E53935"
        },
        title="Customers vs Churned by Country"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        height=450,
        title_x=0.15,
        xaxis_title="Country",
        yaxis_title="Customers"
    )
    fig.update_layout(
    title={
        "text": "Customers vs Churned by Country",
        "x": 0.45,
        "font":{"size":20}
    })
    fig = apply_chart_theme(fig)
    return fig

def churn_contribution_country(df):

    churn = (
        df[df["Exited"] == 1]
        .groupby("Geography")
        .size()
        .reset_index(name="Churned Customers")
    )

    fig = px.pie(
        churn,
        names="Geography",
        values="Churned Customers",
        hole=0.6,
        title="Churn Contribution by Country",
        color="Geography",
        color_discrete_map={
            "France": "#1E88E5",
            "Germany": "#43A047",
            "Spain": "#FB8C00"
        }
    )

    fig.update_traces(
        textinfo="percent+label",
        textposition="inside",
        hovertemplate="<b>%{label}</b><br>Churned: %{value}<br>Contribution: %{percent}<extra></extra>"
    )

    
    fig.update_layout(
        title={
            "text": "Churn Contribution by Country",
            "x": 0.35,
            "font":{"size":20}
        },
        height=450,
        showlegend=True,
        legend_title="Country",
        margin=dict(t=60, b=20, l=20, r=20)
    )
    fig = apply_chart_theme(fig)
    return fig
def age_group_by_geography(df):
    """
    Grouped Bar Chart: Age Group by Geography
    """

    age_geo = (
        df.groupby(["Age_Group", "Geography"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        age_geo,
        x="Age_Group",
        y="Customers",
        color="Geography",
        barmode="group",
        text="Customers",
        color_discrete_sequence=[
            "#1E3A8A",  # France - Blue
            "#DC2626",  # Germany - Red
            "#10B981"   # Spain - Green
        ],
        labels={
            "Age_Group": "Age Group",
            "Customers": "Number of Customers",
            "Geography": "Country"
        },
        title="Age Group Distribution by Geography"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        height=450,
        title_x=0.5,
        xaxis_title="Age Group",
        yaxis_title="Customers",
        legend_title="Country",
        bargap=0.25,
        font=dict(size=14)
    )

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(
        showgrid=True,
        gridcolor="lightgray"
    )
    fig.update_layout(
    title={
        "text": "Age Group Distribution by Geography",
        "x": 0.45,
        "font":{"size":20}
    }
    )
    fig = apply_chart_theme(fig)
    return fig

def gender_churn_chart(df):
    """
    Grouped Bar Chart: Gender-based Churn Differences
    """

    gender_churn = (
        df.groupby(["Gender", "Exited"])
        .size()
        .reset_index(name="Customers")
    )

    # Rename values for better readability
    gender_churn["Exited"] = gender_churn["Exited"].map({
        0: "Retained",
        1: "Churned"
    })

    fig = px.bar(
        gender_churn,
        x="Gender",
        y="Customers",
        color="Exited",
        barmode="group",
        text="Customers",
        title="Gender-based Churn Differences",
        color_discrete_map={
            "Retained": "#1E88E5",
            "Churned": "#E53935"
        }
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        title={
            "text": "Gender-based Churn Differences",
            "x": 0.5,
            "font":{"size":20}
        },
        xaxis_title="Gender",
        yaxis_title="Number of Customers",
        legend_title="Customer Status",
        template="plotly_white",
        height=500
    )
    fig = apply_chart_theme(fig)
    return fig
#--------------page 3-------------------------


#---------------------------------------------



def customer_by_age(df):
    """
    Customer Count by Age Group
    """

    age_count = (
        df.groupby(["Age_Group", "Exited"])
        .size()
        .reset_index(name="Customers")
    )

    # Rename Exited values
    age_count["Exited"] = age_count["Exited"].map({
        0: "Stayed",
        1: "Churned"
    })

    # Correct order of age groups
    age_order = ["<30", "30-45", "46-60", "60+"]

    fig = px.bar(
        age_count,
        x="Age_Group",
        y="Customers",
        color="Exited",
        text="Customers",
        category_orders={"Age_Group": age_order},
        color_discrete_map={
            "Stayed": "#1E88E5",
            "Churned": "#E53935"
        },
        title="Customer Count by Age Group"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title={
            "text": "Customer Count by Age Group",
            "x": 0.5,
            "font":{"size":20}
        },
        xaxis_title="Age Group",
        yaxis_title="Customer Count",
        barmode="stack",
        template="plotly_white",
        height=450,
        margin=dict(l=40, r=40, t=70, b=40)
    )
    fig = apply_chart_theme(fig)
    return fig


def Average_balance_by_age(df):
    """
    Average Balance by Age Group
    """

    avg_balance = (
        df.groupby("Age_Group")["Balance"]
        .mean()
        .reset_index()
    )

    # Keep age groups in correct order
    age_order = ["<30", "30-45", "46-60", "60+"]
    avg_balance["Age_Group"] = avg_balance["Age_Group"].astype(str)

    fig = px.bar(
        avg_balance,
        x="Age_Group",
        y="Balance",
        text="Balance",
        category_orders={"Age_Group": age_order},
        color="Balance",
        color_continuous_scale="Blues",
        title="Average Balance by Age Group"
    )

    fig.update_traces(
        texttemplate="$%{y:,.0f}",
        textposition="outside"
    )

    fig.update_layout(
        title={
            "text": "Average Balance by Age Group",
            "x": 0.5,
            "font":{"size":20}
        },
        xaxis_title="Age Group",
        yaxis_title="Average Balance",
        yaxis_tickprefix="$",
        template="plotly_white",
        height=450,
        showlegend=False,
        margin=dict(l=40, r=40, t=70, b=40)
    )
    fig = apply_chart_theme(fig)
    return fig

def customer_by_tenure(df):
    """
    Customer Count by Tenure Group
    """

    tenure_count = (
        df.groupby(["Tenure_Group", "Exited"])
        .size()
        .reset_index(name="Customers")
    )

    # Rename Exited values
    tenure_count["Exited"] = tenure_count["Exited"].map({
        0: "Stayed",
        1: "Churned"
    })

    # Correct order of tenure groups
    tenure_order = ["New", "Mid-Term", "Long-Term"]

    fig = px.bar(
        tenure_count,
        x="Tenure_Group",
        y="Customers",
        color="Exited",
        text="Customers",
        category_orders={"Tenure_Group": tenure_order},
        color_discrete_map={
            "Stayed": "#1E88E5",
            "Churned": "#E53935"
        },
        title="Customer Count by Tenure Group"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title={
            "text": "Customer Count by Tenure Group",
            "x": 0.5,
            "font":{"size":20}
        },
        xaxis_title="Tenure Group",
        yaxis_title="Customer Count",
        barmode="stack",
        template="plotly_white",
        height=450,
        margin=dict(l=40, r=40, t=70, b=40)
    )
    fig = apply_chart_theme(fig)
    return fig

def age_tenure_heatmap(df):
    """
    Heatmap: Churn Rate (%) by Age Group and Tenure Group
    """

    # Calculate churn rate
    heatmap_data = (
        df.groupby(["Age_Group", "Tenure_Group"])["Exited"]
        .mean()
        .reset_index()
    )

    # Convert to percentage
    heatmap_data["Churn_Rate"] = heatmap_data["Exited"] * 100

    # Pivot for heatmap
    heatmap_df = heatmap_data.pivot(
        index="Age_Group",
        columns="Tenure_Group",
        values="Churn_Rate"
    )

    # Order rows and columns
    age_order = ["<30", "30-45", "46-60", "60+"]
    tenure_order = ["New", "Mid-Term", "Long-Term"]

    heatmap_df = heatmap_df.reindex(index=age_order, columns=tenure_order)

    fig = px.imshow(
        heatmap_df,
        text_auto=".1f",
        color_continuous_scale="Reds",
        aspect="auto",
        labels=dict(
            x="Tenure Group",
            y="Age Group",
            color="Churn Rate (%)"
        ),
        title="Age Group vs Tenure Group Churn Rate (%)"
    )

    fig.update_layout(
        title={
            "text": "Age Group vs Tenure Group Churn Rate (%)",
            "x": 0.25,
            "font":{"size":20}
        },
        template="plotly_white",
        height=450
    )
    fig = apply_chart_theme(fig)
    return fig

def average_credit_by_agegroup(df):
    """
    Average Credit Score by Age Group
    """

    avg_credit = (
        df.groupby("Age_Group")["CreditScore"]
        .mean()
        .reset_index()
    )

    age_order = ["<30", "30-45", "46-60", "60+"]

    fig = px.bar(
        avg_credit,
        x="Age_Group",
        y="CreditScore",
        text="CreditScore",
        category_orders={"Age_Group": age_order},
        color="CreditScore",
        color_continuous_scale="Blues",
        title="Average Credit Score by Age Group"
    )

    fig.update_traces(
        texttemplate="%{y:.0f}",
        textposition="outside"
    )

    fig.update_layout(
        title={
            "font": {"size": 20},
            "x": 0.15
        },
        xaxis_title="Age Group",
        yaxis_title="Average Credit Score",
        template="plotly_white",
        height=500,
        showlegend=False
    )
    fig = apply_chart_theme(fig)
    return fig

def average_credit_by_tenuregroup(df):
    """
    Average Credit Score by Tenure Group
    """

    avg_credit = (
        df.groupby("Tenure_Group")["CreditScore"]
        .mean()
        .reset_index()
    )

    tenure_order = ["New", "Mid-Term", "Long-Term"]

    fig = px.bar(
        avg_credit,
        x="Tenure_Group",
        y="CreditScore",
        text="CreditScore",
        category_orders={"Tenure_Group": tenure_order},
        color="CreditScore",
        color_continuous_scale="Greens",
        title="Average Credit Score by Tenure Group"
    )

    fig.update_traces(
        texttemplate="%{y:.0f}",
        textposition="outside"
    )

    fig.update_layout(
       title={
            "font": {"size": 20},
            "x": 0.15
        },
        xaxis_title="Tenure Group",
        yaxis_title="Average Credit Score",
        template="plotly_white",
        height=500,
        showlegend=False
    )
    fig = apply_chart_theme(fig)
    return fig


#---------------------------------------------------------
# Page 4
#--------------------------------------------------------

def high_balance_churners(df):
    # Customer count by Balance Segment and Churn Status
    chart_df = (
        df.groupby(["Balance_Segment", "Exited"])
        .size()
        .reset_index(name="Customer Count")
    )

    # Rename churn labels
    chart_df["Status"] = chart_df["Exited"].map({
        0: "Stayed",
        1: "Churned"
    })

    fig = px.bar(
        chart_df,
        x="Balance_Segment",
        y="Customer Count",
        color="Status",
        barmode="stack",
        text="Customer Count",
        category_orders={
            "Balance_Segment": [
                "Zero Balance",
                "Low Balance",
                "High Balance"
            ]
        },
        color_discrete_map={
            "Stayed": "#1E88E5",
            "Churned": "#E53935"
        },
        title="High-Balance Churners"
    )

    fig.update_traces(textposition="inside")
    fig.update_layout(
        title={
            "text": "High-Balance Churners",
            "font": {"size": 24}, 
            "x" : 0.45
        })
    fig.update_layout(
        xaxis_title="Balance Segment",
        yaxis_title="Customer Count",
        legend_title="Status",
        height = 450,
        title_x=0.25,
        title = {
            "text" : "High-Balance Churners",
            "font": {"size":20},
            "x":0.25
        }
    )
    fig = apply_chart_theme(fig)
    return fig


def salary_vs_balance_churn(df):

    if df.empty:
        return px.scatter(title="Salary vs Balance Churn Pattern")

    fig = px.scatter(
        df,
        x="EstimatedSalary",
        y="Balance",
        color=df["Exited"].map({0: "Stayed", 1: "Churned"}),
        hover_data=["Geography", "Age", "CreditScore", "NumOfProducts"],
        opacity=0.7,
        color_discrete_map={
            "Stayed": "#1E88E5",
            "Churned": "#E53935"
        },
        title="Salary vs Balance Churn Pattern"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Estimated Salary",
        yaxis_title="Balance",
        legend_title="Customer Status",
        height=450,
        title={
            "text": "Salary vs Balance Churn Pattern",
            "font": {"size": 20},
            "x": 0.15
        }
    )
    fig = apply_chart_theme(fig)
    return fig

def revenue_risk_churn(df):

    if df.empty:
        return px.bar(title="Revenue Risk from Churn")

    # Keep only churned customers
    churn_df = df[df["Exited"] == 1]

    # Sum of balance lost by geography
    revenue_loss = (
        churn_df.groupby("Geography")["Balance"]
        .sum()
        .reset_index(name="Total Balance Lost")
    )

    fig = px.bar(
        revenue_loss,
        x="Geography",
        y="Total Balance Lost",
        color="Geography",
        text_auto=".2s",
        title="Revenue Risk from Churn by Geography"
    )

    fig.update_traces(
        texttemplate="%{y:,.0f}",
        textposition="outside"
    )

    fig.update_layout(
        title={
            "text": "Revenue Risk from Churn by Geography",
            "font": {"size": 20},
            "x": 0.15
        },
        template="plotly_white",
        height=450,
        width=450,
        showlegend=False,
        xaxis_title="Geography",
        yaxis_title="Total Balance Lost"
    )
    fig = apply_chart_theme(fig)
    return fig
    

def financial_stability_heatmap(df):

    if df.empty:
        return px.imshow([[0]], title="Financial Stability vs Churn")

    # Calculate churn rate
    heatmap_df = (
        df.groupby(["Balance_Segment", "Credit_Band"])["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )

    # Pivot table for heatmap
    pivot = heatmap_df.pivot(
        index="Balance_Segment",
        columns="Credit_Band",
        values="Churn Rate"
    )

    # Ensure correct order
    pivot = pivot.reindex(
        index=["Zero Balance", "Low Balance", "High Balance"],
        columns=["Low", "Medium", "High"]
    )

    fig = px.imshow(
        pivot,
        text_auto=".1f",
        color_continuous_scale="RdYlGn_r",
        aspect="auto",
        title="Financial Stability vs Churn"
    )

    fig.update_layout(
        template="plotly_white",
        width=450,
        height=450,
        title={
            "text": " (Balance × Credit Score) vs Churn ",
            "font": {"size": 20},
            "x": 0.13
        },
        xaxis_title="Credit Score Band",
        yaxis_title="Balance Segment",
        coloraxis_colorbar_title="Churn %"
    )
    fig = apply_chart_theme(fig)
    return fig

def high_value_geography(df):

    if df.empty:
        return px.bar(title="High-Value Customers by Geography")

    # High-value customers
    high_value = df[df["Balance_Segment"] == "High Balance"]

    geo = (
        high_value.groupby("Geography")
        .size()
        .reset_index(name="Customer Count")
    )

    fig = px.bar(
        geo,
        x="Geography",
        y="Customer Count",
        color="Geography",
        text="Customer Count",
        title="High-Value Customers by Geography"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        template="plotly_white",
        height=450,
        width=450,
        showlegend=False,
        xaxis_title="Geography",
        yaxis_title="High-Value Customer Count",
        title={
            "text": "High-Value Customers by Geography",
            "font": {"size": 20},
            "x": 0.5
        }
    )
    fig = apply_chart_theme(fig)
    return fig

def high_value_age(df):

    if df.empty:
        return px.bar(title="High-Value Customers by Age")

    high_value = df[df["Balance_Segment"] == "High Balance"]

    age = (
        high_value.groupby(["Age_Group", "Exited"])
        .size()
        .reset_index(name="Customer Count")
    )

    age["Status"] = age["Exited"].map({
        0: "Stayed",
        1: "Churned"
    })

    fig = px.bar(
        age,
        x="Age_Group",
        y="Customer Count",
        color="Status",
        barmode="group",
        text="Customer Count",
        color_discrete_map={
            "Stayed": "#1E88E5",
            "Churned": "#E53935"
        },
        title="High-Value Customers by Age Group"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5,
        title={
            "text": "High-Value Customers by Age Group",
            "font": {"size": 20},
            "x": 0.5
        }
    )
    fig = apply_chart_theme(fig)
    return fig

def apply_chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="#85bef8",
        plot_bgcolor="#A6A4A4",
        font=dict(color="#000000"),
        margin=dict(l=40, r=30, t=60, b=30),
        title_x=0.15
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor="#000000"
    )

    fig.update_yaxes(
        gridcolor="#878787",
        linecolor="#878787"
    )

    return fig


