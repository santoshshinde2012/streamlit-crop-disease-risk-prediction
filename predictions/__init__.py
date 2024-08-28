import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Create a synthetic dataset
data = {
    'crop_name': ['wheat', 'rice', 'maize', 'wheat', 'rice', 'maize', 'wheat', 'rice', 'maize', 'wheat', 'rice', 'maize'],
    'temperature': [20, 25, 22, 21, 24, 23, 19, 26, 21, 20, 25, 22],
    'humidity': [30, 50, 45, 32, 48, 47, 31, 52, 44, 30, 50, 45],
    'soil_moisture': [40, 60, 55, 42, 58, 57, 41, 62, 54, 40, 60, 55],
    'disease_risk': ['low', 'high', 'medium', 'low', 'high', 'medium', 'low', 'high', 'medium', 'low', 'high', 'medium']
}

df = pd.DataFrame(data)

# Encode categorical variable for crop_name
crop_label_encoder = LabelEncoder()
df['crop_name'] = crop_label_encoder.fit_transform(df['crop_name'])

# Encode target variable
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

# Function to predict disease risk based on crop name and other features
def predict_disease_risk(crop_name, temperature, humidity, soil_moisture):
    # Encode the crop name
    crop_name_encoded = crop_label_encoder.transform([crop_name])[0]
    
    # Prepare the feature vector
    features = scaler.transform([[crop_name_encoded, temperature, humidity, soil_moisture]])
    
    # Predict the disease risk
    risk_encoded = model.predict(features)[0]
    
    # Decode the risk
    risk = risk_label_encoder.inverse_transform([risk_encoded])[0]
    
    return risk