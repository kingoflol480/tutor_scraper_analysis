 import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=10),
    "sales": [100, 120, 90, 140, 160, 130, 170, 180, 150, 200]
})

# Line chart
fig_line = px.line(data, x="date", y="sales", title="Sample Line Sales Data")
fig_line.update_traces(
    mode='lines+markers',
    marker=dict(
        size=8,
        color='lightblue',
        line=dict(color='darkblue', width=2)
    )
)
st.plotly_chart(fig_line)

# Histogram with black borders
fig_hist = px.histogram(
    data,
    x="sales",
    nbins=10,
    title="Sample Histogram Sales Data"
)

fig_hist.update_traces(
    marker=dict(
        color='lightblue',
        line=dict(color='black', width=2)
    )
)

st.plotly_chart(fig_hist)
