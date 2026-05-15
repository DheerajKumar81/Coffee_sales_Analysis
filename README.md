<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Coffee Sales Analysis</title>
</head>
<body>

  <h1>☕ Coffee Sales Analysis</h1>

  <p>
    A data analysis project built with <strong>Python</strong>, <strong>Pandas</strong>,
    <strong>Matplotlib</strong>, and <strong>Seaborn</strong> to explore coffee shop sales
    data and generate insights on revenue, product performance, and payment trends.
  </p>

  <hr />

  <h2>📌 Project Overview</h2>
  <p>This project analyzes transactional coffee sales data to answer key business questions such as:</p>
  <ul>
    <li>What is the total revenue generated?</li>
    <li>Which coffee items generate the highest revenue?</li>
    <li>What are the top-selling coffee products?</li>
    <li>How are customers paying (cash vs card)?</li>
    <li>What patterns can be observed from the sales data?</li>
  </ul>

  <h2>📂 Dataset</h2>
  <p>The dataset used in this project is:</p>
  <pre><code>coffee_data.csv</code></pre>

  <h3>Key Columns</h3>
  <ul>
    <li><strong>date</strong> – Transaction date</li>
    <li><strong>datetime</strong> – Full timestamp</li>
    <li><strong>coffee_name</strong> – Name of the coffee product</li>
    <li><strong>money</strong> – Revenue from each transaction</li>
    <li><strong>cash_type</strong> – Payment method</li>
    <li><strong>card</strong> – Card information (missing values handled)</li>
  </ul>

  <h2>🛠️ Technologies Used</h2>
  <ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>Visual Studio Code</li>
  </ul>

  <h2>📈 Analysis Performed</h2>

  <h3>1. Data Cleaning</h3>
  <ul>
    <li>Filled missing values in the <code>card</code> column with <code>"Unknown"</code>.</li>
    <li>Converted <code>date</code> and <code>datetime</code> columns to datetime format.</li>
  </ul>

  <h3>2. Total Revenue Calculation</h3>
  <ul>
    <li>Computed total sales revenue from all transactions.</li>
  </ul>

  <h3>3. Revenue by Coffee Item</h3>
  <ul>
    <li>Grouped data by <code>coffee_name</code>.</li>
    <li>Calculated total revenue for each coffee product.</li>
    <li>Sorted products by revenue.</li>
  </ul>

  <h3>4. Top 5 Coffee Products</h3>
  <ul>
    <li>Visualized the five highest revenue-generating items using a bar chart.</li>
  </ul>

  <h3>5. Payment Method Distribution</h3>
  <ul>
    <li>Displayed customer payment preferences using a pie chart.</li>
  </ul>

  <h2>📊 Visualizations</h2>
  <ul>
    <li><strong>Bar Chart:</strong> Top 5 coffee products by revenue</li>
    <li><strong>Bar Chart:</strong> Revenue collected by each coffee item</li>
    <li><strong>Pie Chart:</strong> Payment method distribution</li>
  </ul>

  <h2>▶️ How to Run the Project</h2>

  <h3>Clone the Repository</h3>
  <pre><code>git clone https://github.com/DheerajKumar81/Coffee_sales_Analysis.git
cd Coffee_sales_Analysis</code></pre>

  <h3>Install Dependencies</h3>
  <pre><code>pip install pandas matplotlib seaborn</code></pre>

  <h3>Run the Script</h3>
  <pre><code>python analysis.py</code></pre>

  <h2>📌 Sample Insights</h2>
  <ul>
    <li>Total revenue generated from coffee sales.</li>
    <li>Identification of the most profitable coffee products.</li>
    <li>Customer preference for different payment methods.</li>
    <li>Comparative revenue contribution of all menu items.</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre><code>Coffee_sales_Analysis/
├── analysis.py
├── coffee_data.csv
├── README.md
└── requirements.txt</code></pre>

  <h2>🚀 Future Enhancements</h2>
  <ul>
    <li>Monthly and daily sales trend analysis.</li>
    <li>Best-selling items by quantity sold.</li>
    <li>Time-based peak sales analysis.</li>
    <li>Interactive dashboards using Plotly or Streamlit.</li>
    <li>Forecasting future sales using machine learning models.</li>
  </ul>

  <h2>📚 Learning Outcomes</h2>
  <ul>
    <li>Data cleaning and preprocessing</li>
    <li>GroupBy operations in Pandas</li>
    <li>Exploratory Data Analysis (EDA)</li>
    <li>Data visualization</li>
    <li>Business insight generation</li>
  </ul>

  <h2>👤 Author</h2>
  <p>
    <strong>Dheeraj Kumar</strong><br />
    GitHub:
    <a href="https://github.com/DheerajKumar81" target="_blank">
      https://github.com/DheerajKumar81
    </a>
  </p>

  <h2>⭐ If You Found This Project Useful</h2>
  <p>
    If you found this project helpful, consider starring the repository on
    <a href="https://github.com" target="_blank">GitHub</a>.
  </p>

</body>
</html>
