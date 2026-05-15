☕ Coffee Sales Analysis

A data analysis project built with Python, Pandas, Matplotlib, and Seaborn to explore coffee shop sales data and generate insights on revenue, product performance, and payment trends.

📌 Project Overview

This project analyzes transactional coffee sales data to answer key business questions such as:

What is the total revenue generated?
Which coffee items generate the highest revenue?
What are the top-selling coffee products?
How are customers paying (cash vs card)?
What patterns can be observed from the sales data?

The analysis includes data cleaning, aggregation, and visualizations to present meaningful insights.

📂 Dataset

The dataset used in this project is:

coffee_data.csv
Key Columns
date – Transaction date
datetime – Full timestamp
coffee_name – Name of the coffee product
money – Revenue from each transaction
cash_type – Payment method
card – Card information (missing values handled)
🛠️ Technologies Used
Python
Pandas
Matplotlib
Seaborn
Visual Studio Code
📈 Analysis Performed
1. Data Cleaning
Filled missing values in the card column with "Unknown".
Converted date and datetime columns to proper datetime format.
2. Total Revenue Calculation
Computed total sales revenue from all transactions.
3. Revenue by Coffee Item
Grouped data by coffee_name.
Calculated total revenue for each coffee product.
Sorted products by revenue.
4. Top 5 Coffee Products
Visualized the five highest revenue-generating items using a bar chart.
5. Payment Method Distribution
Displayed customer payment preferences using a pie chart.
📊 Visualizations

The project generates:

Bar Chart: Top 5 coffee products by revenue
Bar Chart: Revenue collected by each coffee item
Pie Chart: Payment method distribution
▶️ How to Run the Project
Clone the Repository
git clone https://github.com/DheerajKumar81/Coffee_sales_Analysis.git
cd Coffee_sales_Analysis
Install Dependencies
pip install pandas matplotlib seaborn
Run the Script
python analysis.py
📌 Sample Insights
Total revenue generated from coffee sales.
Identification of the most profitable coffee products.
Customer preference for different payment methods.
Comparative revenue contribution of all menu items.
📁 Project Structure
Coffee_sales_Analysis/
├── analysis.py
├── coffee_data.csv
├── README.md
└── requirements.txt
🚀 Future Enhancements
Monthly and daily sales trend analysis.
Best-selling items by quantity sold.
Time-based peak sales analysis.
Interactive dashboards using Plotly or Streamlit.
Forecasting future sales using machine learning models.
📚 Learning Outcomes

Through this project, I strengthened my understanding of:

Data cleaning and preprocessing
GroupBy operations in Pandas
Exploratory Data Analysis (EDA)
Data visualization
Business insight generation
👤 Author

Dheeraj Kumar

GitHub: DheerajKumar81 GitHub Profile
