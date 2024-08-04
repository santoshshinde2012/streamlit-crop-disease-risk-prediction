import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
from prediction_type import CropData
from components import rchart_events
from dataclasses import asdict

# Create a synthetic dataset
data = {
    'crop_name': ['wheat', 'rice', 'maize', 'wheat', 'rice', 'maize', 'wheat', 'rice', 'maize', 'wheat', 'rice', 'maize'],
    'temperature': [20, 25, 22, 21, 24, 23, 19, 26, 21, 20, 25, 22],
    'humidity': [30, 50, 45, 32, 48, 47, 31, 52, 44, 30, 50, 45],
    'soil_moisture': [40, 60, 55, 42, 58, 57, 41, 62, 54, 40, 60, 55],
    'disease_risk': ['low', 'high', 'medium', 'low', 'high', 'medium', 'low', 'high', 'medium', 'low', 'high', 'medium']
}

df = pd.DataFrame(data)

# Encode categorical variables
crop_label_encoder = LabelEncoder()
df['crop_name'] = crop_label_encoder.fit_transform(df['crop_name'])
risk_label_encoder = LabelEncoder()
df['disease_risk'] = risk_label_encoder.fit_transform(df['disease_risk'])

# Features and target variable
X = df[['crop_name', 'temperature', 'humidity', 'soil_moisture']]
y = df['disease_risk']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and scalers to avoid retraining
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('crop_label_encoder.pkl', 'wb') as f:
    pickle.dump(crop_label_encoder, f)
with open('risk_label_encoder.pkl', 'wb') as f:
    pickle.dump(risk_label_encoder, f)

# Load the saved model and scalers
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('crop_label_encoder.pkl', 'rb') as f:
        crop_label_encoder = pickle.load(f)
    with open('risk_label_encoder.pkl', 'rb') as f:
        risk_label_encoder = pickle.load(f)
    return model, scaler, crop_label_encoder, risk_label_encoder

model, scaler, crop_label_encoder, risk_label_encoder = load_model()

def predict_disease_risk(crop_name, temperature, humidity, soil_moisture):
    crop_name_encoded = crop_label_encoder.transform([crop_name])[0]
    features = scaler.transform([[crop_name_encoded, temperature, humidity, soil_moisture]])
    risk_encoded = model.predict(features)[0]
    risk = risk_label_encoder.inverse_transform([risk_encoded])[0]
    return risk

with st.sidebar:
    st.title('Crop Disease Risk Prediction')

    st.write("""
    This application predicts the risk of crop disease based on the entered crop details.
    """)

    crop_name = st.selectbox('Crop Name', ['wheat', 'rice', 'maize'])
    temperature = st.slider('Temperature', min_value=10, max_value=40, value=20)
    humidity = st.slider('Humidity', min_value=20, max_value=100, value=50)
    soil_moisture = st.slider('Soil Moisture', min_value=20, max_value=100, value=50)

# if st.sidebar.button('Predict Disease Risk'):
risk = predict_disease_risk(crop_name, temperature, humidity, soil_moisture)
crop_data = CropData(
    crop_name=crop_name,
    temperature=[temperature],
    humidity=[humidity],
    soil_moisture=[soil_moisture],
    risk_prediction=[risk]
)
crop_data_dict = asdict(crop_data)
rchart_events(crop_data_dict)