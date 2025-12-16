# Sales Data Exploratory Analysis and Visualization

## 🚀 Project Goal

The primary goal of this project is to conduct an **Exploratory Data Analysis (EDA)** on a sales transactions dataset. The analysis aims to extract insights into product performance, sales trends across categories, and customer payment behavior, using powerful visualization tools.

## 🗃️ Data Source

The analysis is performed on the dataset: `sales_data2.csv`.

## ⚙️ Key Steps and Methodology

The analysis follows a standard EDA workflow using Python:

### 1. Data Loading and Inspection
* The `sales_data2.csv` file is loaded into a pandas DataFrame.
* `df.info()` is used to check data types, missing values, and overall data structure integrity.

### 2. Data Organization and Inspection
* The data is sorted by `Category`, `Product`, and `Region` to facilitate structured inspection and analysis (`df_sorted`).
* The first 50 entries of the grouped columns are printed to visually confirm data quality and sorting.

### 3. Aggregation and Feature Extraction
The following key sales metrics are calculated using `df.groupby()`:
* **Total Sales by Product:** Sum of `Total` sales for each `Product`.
* **Max Sales by Category:** Maximum `Total` sale observed within each `Category`.
* **Payment Method Counts:** Frequency of each unique `PaymentMethod` used by customers.

### 4. Visualization

Three subplots are generated to clearly communicate the findings:

| Visualization | Data Source | Insight |
| :--- | :--- | :--- |
| **Total Sales** | `sales_by_total` (Sum) | Clearly displays the **most and least popular products** based on aggregate revenue. |
| **Category Sales** | `sales_by_Category` (Max) | Shows the highest single-transaction value achieved within each product category. |
| **Payment Method** | `payment_counts` (Count) | Visualizes customer preference and distribution across different **payment methods**. |

## 🛠️ Technologies Used

* **Python 3.x**
* **`pandas`:** For data loading, inspection, sorting, and aggregation (`groupby`).
* **`matplotlib`:** For defining the chart structure (`fig, axes`).
* **`seaborn`:** For generating professional, clear bar plots (`sns.barplot`).
