import streamlit as st
import pandas as pd
from components import rchart_events
from dataclasses import asdict
from predictions import data
from predictions import predict_disease_risk
from crops import CropData
import altair as alt

def page_dataset_overview():
    st.title("Overview")

    df = pd.DataFrame(data)
    heatmap = alt.Chart(df).mark_rect().encode(
        x='temperature:O',
        y='humidity:O',
        color=alt.Color('disease_risk:N', scale=alt.Scale(domain=['low', 'medium', 'high'], range=['green', 'gray', 'red'])),
        tooltip=['temperature', 'humidity', 'soil_moisture']
    ).properties(width=600, height=400)

    st.altair_chart(heatmap)

def page_data_visualization():
    with st.sidebar:
        st.title('Crop Disease Risk Prediction')

        st.write("""
        This application predicts the risk of crop disease based on the entered crop details.
        """)

        crop_name = st.selectbox('Crop Name', ['wheat', 'rice', 'maize'])
        temperature = st.slider('Temperature', min_value=10, max_value=40, value=20)
        humidity = st.slider('Humidity', min_value=20, max_value=100, value=50)
        soil_moisture = st.slider('Soil Moisture', min_value=20, max_value=100, value=50)

    risk = predict_disease_risk(crop_name, temperature, humidity, soil_moisture)

    crop_data = CropData(
        crop_name=crop_name,
        temperature=[temperature],
        humidity=[humidity],
        soil_moisture=[soil_moisture],
        risk_prediction=[risk]
    )

    st.subheader("Crop Disease Risk Prediction - With Custom Component")

    crop_data_dict = asdict(crop_data)
    rchart_events(crop_data_dict)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dataset Overview", "Crop Disease Risk Prediction"])
    
    if page == "Dataset Overview":
        page_dataset_overview()
    elif page == "Crop Disease Risk Prediction":
        page_data_visualization()

if __name__ == "__main__":
    main()