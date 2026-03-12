"""
Airbnb Market Dynamics & Pricing Optimization Pipeline
Objective: Extract pricing strategies, neighborhood revenue dynamics, and customer satisfaction metrics.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Data Ingestion & Setup
df = pd.read_csv('airbnblistings.csv')
sns.set_theme(style="whitegrid")
print(f"Data ingested. Processing {df.shape[0]} active market listings.")

# 2. Pricing Strategy: Revenue Potential by Property Type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[df['price'] < 500], x='room_type', y='price', palette='Set2')
plt.title('Pricing Strategy: Revenue Potential by Property Type (Amsterdam)')
plt.ylabel('Nightly Price ($)')
plt.xlabel('Property Classification')
plt.tight_layout()
plt.savefig('pricing_strategy.png')

# 3. Neighborhood Revenue Heatmap (Top 10 High-Density Zones)
top_neighborhoods = df['neighbourhood'].value_counts().nlargest(10).index
filtered_df = df[df['neighbourhood'].isin(top_neighborhoods)]

plt.figure(figsize=(12, 6))
sns.barplot(data=filtered_df, x='price', y='neighbourhood', hue='room_type', errorbar=None, palette='viridis')
plt.title('Market Dynamics: Average Price by Neighborhood and Room Type')
plt.xlabel('Average Nightly Price ($)')
plt.ylabel('Neighborhood Segment')
plt.legend(title='Property Type')
plt.tight_layout()
plt.savefig('neighborhood_dynamics.png')

# 4. Customer Satisfaction & Value Perception
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='review_scores_value', y='review_scores_rating', alpha=0.5, color='coral')
plt.title('Customer Satisfaction: Rating vs Perceived Value')
plt.xlabel('Value Score')
plt.ylabel('Overall Rating Score')
plt.tight_layout()
plt.savefig('customer_satisfaction.png')

print("Pipeline execution complete. Strategic assets generated.")
