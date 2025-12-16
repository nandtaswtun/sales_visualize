# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\archive\\sales_data2.csv')
df

# %%
print(df.info())

# %%
df_sorted = df.sort_values(by = ['Category','Product','Region'])
df_sorted

# %%
print(df[['Category','Product','Region']].head(50))

# %%
sales_by_total = df.groupby('Product')['Total'].sum()
sales_by_total

# %%
sales_by_Category = df.groupby('Category')['Total'].max()
sales_by_Category

# %%
payment_counts = df['PaymentMethod'].value_counts()
payment_counts

# %%
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(30,10))
sns.barplot(x=sales_by_total.index, y=sales_by_total.values, palette='viridis', ax=axes[0])
axes[0].set_title('Total Sales')
axes[0].set_xlabel('Product')
axes[0].set_ylabel('Total')
axes[0].tick_params(axis='x', rotation=45)

sns.barplot(x=sales_by_Category.index, y=sales_by_Category.values, palette='plasma', ax=axes[1])
axes[1].set_title('Category Sales')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Total')

sns.barplot(x=payment_counts.index, y=payment_counts.values, palette='viridis', ax=axes[2])
axes[2].set_title('Payment Method')
axes[2].set_xlabel('Payment')
axes[2].set_ylabel('Total')



