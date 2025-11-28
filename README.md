# Business KPI Dashboard Generator

A Python dashboard that turns business data into interactive visualizations using Streamlit 

## What This Does

This project takes CSV data with business metrics (revenue, sales, customers, satisfaction) and creates:
- **KPI Cards** showing key totals and averages
- **Interactive Charts** for trends over time
- **Automatic Insights** highlighting best/worst performance




## Setup Instructions

- `python` - To run the code
- `streamlit` - Creates the web dashboard
- `pandas` - Handles data processing
- `plotly` - Makes interactive charts




### Run the Dashboard
go to your terminal and run: python -m streamlit run dashboard.py

The dashboard will open in your browser at `http://localhost:8501`

## Using the Dashboard

Upload `sample_data.csv` (or your own CSV file)

## CSV File Format

Your CSV needs these columns:
- **Month**: Month name (January, February, etc.)
- **Revenue**: Revenue amount
- **Sales**: Number of sales
- **Customers**: Customer count
- **Satisfaction**: Rating from 1-5

Example:
```csv
Month,Revenue,Sales,Customers,Satisfaction
January,45000,320,1200,4.2
February,52000,380,1350,4.3
```

## What I Learned Building This

- How to use Streamlit for web dashboards
- Processing data with Pandas
- Creating visualizations with Plotly
- Reading and working with CSV files
- Calculating business metrics (KPIs)

## Screenshots

![Dashboard Overview](screenshot%201.png)

![Dashboard Charts](screenshot%202.png)
