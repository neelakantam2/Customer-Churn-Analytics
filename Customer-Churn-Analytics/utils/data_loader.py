import pandas as pd
import numpy as np
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv("data/European_Bank_Cleaned.csv")

    df.drop(
        columns=[ "CustomerId"],
        inplace=True
    )

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0,30,45,60,100],
        labels=["<30","30-45","46-60","60+"]
    )

    df["Credit_Band"] = pd.cut(
        df["CreditScore"],
        bins=[0,500,700,900],
        labels=["Low","Medium","High"]
    )

    df["Balance_Segment"] = np.where(
        df["Balance"]==0,
        "Zero Balance",
        np.where(
            df["Balance"]<100000,
            "Low Balance",
            "High Balance"
        )
    )

    df["Tenure_Group"] = pd.cut(
        df["Tenure"],
        bins=[-1,2,6,10],
        labels=["New","Mid-Term","Long-Term"]
    )
    df["CustomerStatus"] = df["Exited"].map({
        0:"Active",
        1:"Churned"
    })

    df["EngagementStatus"] = df.apply(
    lambda x: "Highly Engaged"
    if (
        x["IsActiveMember"]==1
        and
        x["HasCrCard"]==1
        and
        x["NumOfProducts"]>1
    )
    else "Low Engagement",
    axis=1
    )

    df["HighValueCustomer"] = (
    (df["Balance"]>100000)
    &
    (df["EstimatedSalary"]>100000)
).map({
    True:"Yes",
    False:"No"
    })

    def customer_value(row):

        if row["Balance"]>100000 and row["NumOfProducts"]>=2:
            return "Premium"

        elif row["Balance"]>50000:
         return "Standard"

        else:
            return "Basic"

    df["CustomerValue"] = df.apply(customer_value,axis=1)

    def churn_risk(row):

        if (
            row["CreditScore"]<500
        and
        row["IsActiveMember"]==0
    ):
            return "High"

        elif row["CreditScore"]<650:
         return "Medium"

        else:
         return "Low"

    df["RiskLevel"] = df.apply(churn_risk,axis=1)

    df["ProductCategory"] = df["NumOfProducts"].map({
    1:"Single Product",
    2:"Two Products",
    3:"Three Products",
    4:"Four Products"
})  
    df["ActivityLabel"] = df["IsActiveMember"].map({
    0:"Inactive",
    1:"Active"
})  
    df["CreditCardStatus"] = df["HasCrCard"].map({
    0:"No Card",
    1:"Has Card"
})
    
    return df

















