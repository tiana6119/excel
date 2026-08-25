📊 Excel Data Analysis & Dashboard Project

## 📌 Project Overview
This project showcases an end-to-end data analysis workflow in Microsoft Excel, transforming raw data into business insights. It covers data cleaning, pivot table analysis, dynamic lookup modeling, and key visual dashboard design.


 🛠️ Data Activities & Methodology

1. Data Cleaning & Formatting
- Standardized `Date` column formats (`YYYY-MM-DD`).
- Formatted financial metrics (`Cost`, `Revenue`, `Profit`) as currency.
- Applied **Conditional Formatting** to auto-highlight high-profit items (>$1,000 in green) and loss margins (negative profit in red).
- Deduplicated raw records to ensure data integrity.

 2. Pivot Table & Regional Sales Analysis
- Structured interactive Pivot Tables to break down revenue across `Country` (Rows) and `Product_Category` (Columns).
- Sorted total revenue in descending order to identify top-performing markets.
- Used **Data Bars** inside the Pivot Table for quick data visualization.

 3. Dynamic Lookups & Pricing Models
- Created a calculated field for discounted pricing (`Revenue * 0.9`).
- Implemented `XLOOKUP` / `VLOOKUP` functions to dynamically pull product pricing from reference tables (e.g., matching unit prices for items like *"Hitch Rack - 4-Bike"*).

4. Executive KPI Dashboard
- Developed summary KPI cards tracking **Total Revenue**, **Total Profit**, and **Total Orders**.
- Applied custom profit margin formulas: `(Profit / Revenue) * 100`.
- Used conditional logic to highlight healthy margins (>20%) and low-margin alerts (<10%).
- Built a **Revenue vs. Profit Bar Chart** to compare overall financial performance.




## 🔧 Skills & Tools Applied
- **Tool:** Microsoft Excel
- **Formulas:** `XLOOKUP`, `VLOOKUP`, Arithmetic Calculations, Profit Margin Logic
- **Features:** Conditional Formatting, Pivot Tables, Data Bars, KPI Cards, Bar Charts
