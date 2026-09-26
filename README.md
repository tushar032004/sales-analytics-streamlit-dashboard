# 📊 Sales Analytics Dashboard

An interactive sales analytics dashboard built with **Python, Pandas, Plotly, and Streamlit**.

The project transforms raw retail sales data into an interactive dashboard that allows users to explore sales performance, customer segments, products, geographic trends, and shipping performance.

## 🌐 Live Demo

👉 [Open the Interactive Sales Analytics Dashboard](https://sales-analytics-app-dashboard-ktvz9o8vghbjqdpdxgvqle.streamlit.app/)

## 🚀 Features

- Interactive sales dashboard
- Dynamic KPI calculations
- Region filtering
- Category filtering
- Customer segment filtering
- Date-range filtering
- Monthly sales trend analysis
- Product and sub-category analysis
- Geographic sales analysis
- Shipping performance analysis
- Dynamic business insights
- Filtered data explorer
- CSV download functionality

## 📌 Key Performance Indicators

The dashboard tracks:

- Total Sales
- Total Orders
- Unique Customers
- Average Order Value

## 📊 Dashboard Analysis

The dashboard includes:

- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Sales by Sub-Category
- Top 10 Products by Sales
- Top 10 States by Sales
- Top 10 Cities by Sales
- Average Shipping Time by Shipping Mode

## 💡 Business Insights

With all records selected, the analysis shows:

- **Total Sales:** approximately $2.26 million
- **Unique Orders:** 4,922
- **Unique Customers:** 793
- **Average Order Value:** approximately $459.48
- **Highest-sales Category:** Technology
- **Highest-sales Region:** West
- **Largest Customer Segment by Sales:** Consumer
- **Highest-sales State:** California
- **Highest-sales City:** New York City

The dashboard recalculates its KPIs, charts, and business insights dynamically when filters are changed.

> **Note:** The dataset contains sales revenue but does not contain profit or cost information. Therefore, the dashboard analyzes sales performance rather than profitability.

## 🛠️ Technologies Used

- **Python** — application and analysis logic
- **Pandas** — data cleaning, transformation, and aggregation
- **Streamlit** — interactive dashboard
- **Plotly** — interactive data visualizations

## 📁 Project Structure

```text
sales-analytics-streamlit-dashboard/
│
├── data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv
│
├── screenshots/
│   └── dashboard.png
│
├── analysis.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> `.venv/` is used locally and excluded from Git using `.gitignore`.

## 🔄 Data Processing

The data preparation pipeline includes:

1. Loading the raw CSV dataset
2. Checking for duplicate records
3. Converting order and shipping dates
4. Handling missing postal codes
5. Validating sales values
6. Creating additional analytical features
7. Calculating shipping duration
8. Exporting a cleaned dataset for the dashboard

### Engineered Features

Additional columns created during preprocessing include:

- Order Year
- Order Month
- Month Name
- Year-Month
- Shipping Days

## 📈 Dataset Summary

The dataset contains:

- **9,800** transaction rows
- **4,922** unique orders
- **793** unique customers
- **$2.26M+** in total sales

The dataset includes information about:

- Orders
- Customers
- Products
- Categories and sub-categories
- Regions, states, and cities
- Shipping methods
- Sales revenue

## 📂 Dataset Source

This project uses the public **Superstore Sales Dataset** available on Kaggle.

Dataset: `rohitsahoo/sales-forecasting`

The dataset is used for educational and portfolio purposes.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/tushar032004/sales-analytics-streamlit-dashboard.git
```

### 2. Move into the project directory

```bash
cd sales-analytics-streamlit-dashboard
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Dashboard

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit address displayed in the terminal.

## 📊 Running the Data Analysis

To run the data-cleaning and analysis pipeline:

```bash
python analysis.py
```

This processes the raw dataset and generates:

```text
data/cleaned_sales_data.csv
```

The Streamlit application uses this cleaned dataset.

## 🎯 Project Purpose

This project was developed as an independent portfolio project to demonstrate practical skills in:

- Data cleaning and preprocessing
- Exploratory data analysis
- Business data analysis
- Pandas
- Data visualization
- Interactive dashboard development
- Streamlit
- Python application development

## 🔮 Possible Future Improvements

Potential extensions include:

- User-uploaded CSV analysis
- Automated column validation
- Additional time-series analysis
- Sales forecasting
- Customer-level analysis
- More advanced geographic visualizations

## 👤 Author

**Tushar Jaiswal**

Python Data Analysis | Streamlit Dashboards | Machine Learning
