import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ১. data set load
df = pd.read_csv('ecommerce_behaviour.csv')

# ২. make matrix (Conversion and Cart Abandonment)
df['Is_Purchased'] = df['Purchased'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Is_Cart_Added'] = df['Cart_Added'].apply(lambda x: 1 if x == 'Yes' else 0)

# ৩. costomer behavior analysis
source_analysis = df.groupby('Traffic_Source').agg(
    Total_Users=('User_ID', 'count'),
    Avg_Session_Min=('Session_Duration_Min', 'mean'),
    Avg_Pages_Viewed=('Pages_Viewed', 'mean'),
    Total_Purchases=('Is_Purchased', 'sum'),
    Total_Revenue_INR=('Order_Value_INR', 'sum')
).reset_index()

source_analysis['Conversion_Rate (%)'] = (source_analysis['Total_Purchases'] / source_analysis['Total_Users']) * 100

print("--- Marketing & E-Commerce Behaviour Summary ---")
print(source_analysis.round(2))

# ৪. devise marketing (Mobile vs Desktop)
device_summary = df.groupby('Device')['Order_Value_INR'].agg(['count', 'mean', 'sum'])
print("\n--- Device Performance ---")
print(device_summary.round(2))

# ৫. vesiulition
plt.figure(figsize=(9, 5))
sns.barplot(data=source_analysis, x='Traffic_Source', y='Conversion_Rate (%)', palette='magma')
plt.title('Conversion Rate by Marketing Traffic Source', fontsize=14, fontweight='bold')
plt.xlabel('Traffic Source', fontsize=12)
plt.ylabel('Conversion Rate (%)', fontsize=12)
plt.tight_layout()
plt.savefig('traffic_conversion.png', dpi=300)
print("\nAnalysis complete and chart saved!")
