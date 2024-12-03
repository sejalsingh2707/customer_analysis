from fastapi import FastAPI
import pandas as pd

app=FastAPI()



data=pd.read_csv(r"C:\Users\sejal\OneDrive\Desktop\customer_segmentation_project\data\segment_output.csv")
total_customers=len(data)

segment_stats=data.groupby('Segment').agg({
    'Monthly_Revenue':'mean',
    'CLTV':'mean',
    'Age':'mean',
    'Customer_ID':'count'
}).rename(columns={'Customer_ID':'Customer_Counts'}).round(2)

segment_stats["Percentage_of_Cust"]=(segment_stats['Customer_Counts']/total_customers*100).round(2)

segment_stats_dict=segment_stats.to_dict(orient='index')


cluster_data = [
    {
        "Cluster": 0,
        "Monthly_Revenue": 797.85,
        "CLTV": 12032.71,
        "Loyalty_Points": 513.29,
        "Retention_Offers_Availed": 1.73,
        "Recommendation": "Offer loyalty rewards and premium services to maintain engagement."
    },
    {
        "Cluster": 1,
        "Monthly_Revenue": 404.35,
        "CLTV": 8833.19,
        "Loyalty_Points": 477.93,
        "Retention_Offers_Availed": 3.27,
        "Recommendation": "Focus on retention campaigns and cross-sell opportunities."
    },
    {
        "Cluster": 2,
        "Monthly_Revenue": 329.56,
        "CLTV": 11693.38,
        "Loyalty_Points": 511.51,
        "Retention_Offers_Availed": 0.66,
        "Recommendation": "Engage with discounts or subscription renewal incentives."
    },
]


cluster_profile=pd.DataFrame(cluster_data)
cluster_profile.head(2)









