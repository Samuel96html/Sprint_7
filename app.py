import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

car_data = pd.read_csv("vehicles_us.csv")
st.header('Relationship between Vehicle, Price and Mileage')
hist_button = st.button('Odometer Histogram')

if hist_button:
    st.write('Histogram of Odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Bar of fuel type')
if disp_button:
    st.write('Fuel Type Distribution')
    fig = px.bar(car_data, x='fuel', title='Fuel Type Distribution')
    st.plotly_chart(fig, use_container_width=True)


if st.checkbox('Show scatter plot'):
    st.write('Pie chart of transmission types')
    fig = px.pie(car_data, names='transmission', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

st.header("Compare Price by Manufacturer")
manufacturers = car_data['model'].unique()
selected = st.multiselect("Select up to two manufacturers",
                          manufacturers, default=manufacturers[:2])
filtered_data = car_data[car_data['model'].isin(selected)]
avg_prices = filtered_data.groupby('model')['price'].mean().reset_index()
fig = px.bar(avg_prices, x='model', y='price',
             title="Average Price Comparison")
st.plotly_chart(fig, use_container_width=True)
