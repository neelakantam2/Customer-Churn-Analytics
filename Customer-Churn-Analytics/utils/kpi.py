def total_customers(df):

    return len(df)
def total_churned_customers(df):

    return int(df["Exited"].sum())
def active_customers(df):

    return int((df["Exited"] == 0).sum())
def average_balance(df):

    if len(df) == 0:
        return 0

    return round(df["Balance"].mean(), 2)

def overall_churn_rate(df):

    if len(df) == 0:
        return 0

    return round((df["Exited"].sum() / len(df)) * 100, 2)


def segment_churn_rate(df):

    if len(df) == 0:
        return 0

    return round(df["Exited"].mean() * 100, 2)

def high_value_churn_ratio(df):
    high_value_df = high_value_customers(df)
    if len(high_value_df) > 0:
        high_value_churn_rate = (
            high_value_df["Exited"].mean() * 100
        )
    else:
     high_value_churn_rate = 0

    return high_value_churn_rate


def geographic_risk_index(df):

    geography = (
        df.groupby("Geography")["Exited"]
        .mean()
        .sort_values(ascending=False)
    )

    if geography.empty:
        return "N/A", 0

    return geography.index[0], round(geography.iloc[0] * 100, 2)


def engagement_drop_indicator(df):

    inactive = df[df["IsActiveMember"] == 0]

    if len(inactive) == 0:
        return 0

    return round(inactive["Exited"].mean() * 100, 2)
def high_value_customers(df):
    return df[
        (df["Balance"] >= 100000) &
        (df["CreditScore"] >= 700)
    ]