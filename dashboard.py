import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Business KPI Dashboard", page_icon="📊", layout="wide")

# Title
st.title("📊 Business KPI Dashboard Generator")
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("Upload your business data (CSV file)", type=['csv'])

if uploaded_file is not None:
    # Read the data
    df = pd.read_csv(uploaded_file)

    # Show raw data (optional)
    with st.expander("📋 View Raw Data"):
        st.dataframe(df)

    # Calculate KPIs
    st.header("🎯 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_revenue = df['Revenue'].sum()
        st.metric("Total Revenue", f"${total_revenue:,.2f}")

    with col2:
        total_customers = df['Customers'].sum()
        st.metric("Total Customers", f"{total_customers:,}")

    with col3:
        avg_satisfaction = df['Satisfaction'].mean()
        st.metric("Avg Satisfaction", f"{avg_satisfaction:.1f}/5")

    with col4:
        total_sales = df['Sales'].sum()
        st.metric("Total Sales", f"{total_sales:,}")

    st.markdown("---")

    # Charts section
    st.header("📈 Visual Insights")

    # Row 1: Revenue and Sales trends
    col1, col2 = st.columns(2)

    with col1:
        fig_revenue = px.line(df, x='Month', y='Revenue',
                             title='Monthly Revenue Trend',
                             markers=True)
        fig_revenue.update_traces(line_color='#00CC96')
        st.plotly_chart(fig_revenue, use_container_width=True)

    with col2:
        fig_sales = px.bar(df, x='Month', y='Sales',
                          title='Monthly Sales Volume',
                          color='Sales',
                          color_continuous_scale='Blues')
        st.plotly_chart(fig_sales, use_container_width=True)

    # Row 2: Customer and Satisfaction analysis
    col1, col2 = st.columns(2)

    with col1:
        fig_customers = px.area(df, x='Month', y='Customers',
                               title='Customer Growth',
                               color_discrete_sequence=['#EF553B'])
        st.plotly_chart(fig_customers, use_container_width=True)

    with col2:
        fig_satisfaction = px.line(df, x='Month', y='Satisfaction',
                                  title='Customer Satisfaction Score',
                                  markers=True,
                                  line_shape='spline')
        fig_satisfaction.update_traces(line_color='#FFA15A')
        st.plotly_chart(fig_satisfaction, use_container_width=True)

    st.markdown("---")

    # Summary insights
    st.header("💡 Insights Summary")

    # Calculate some insights
    revenue_growth = ((df['Revenue'].iloc[-1] - df['Revenue'].iloc[0]) / df['Revenue'].iloc[0]) * 100
    best_month = df.loc[df['Revenue'].idxmax(), 'Month']
    worst_month = df.loc[df['Revenue'].idxmin(), 'Month']

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(f"📈 Revenue Growth: {revenue_growth:.1f}%")

    with col2:
        st.success(f"🏆 Best Month: {best_month}")

    with col3:
        st.warning(f"⚠️ Weakest Month: {worst_month}")

else:
    # Instructions when no file is uploaded
    st.info("👆 Please upload a CSV file to generate your dashboard")

    st.markdown("""
    ### 📝 Required CSV Format:
    Your CSV file should have these columns:
    - **Month**: Month name (e.g., January, February)
    - **Revenue**: Revenue amount
    - **Sales**: Number of sales
    - **Customers**: Number of customers
    - **Satisfaction**: Customer satisfaction score (1-5)

    ### 💡 Tip:
    Check out `sample_data.csv` for an example!
    """)
