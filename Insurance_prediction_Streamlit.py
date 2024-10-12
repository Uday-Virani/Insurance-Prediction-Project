import streamlit as st
import pandas as pd
import joblib

# Load the saved model
scaler = joblib.load('Scaler.joblib')
model = joblib.load('Random_Forest_Classifier.joblib')

# Create a Streamlit app
st.title("<<< Insurance Prediction >>>")

# Create input fields for the user to enter data
st.subheader("Enter customer data:")
age = st.number_input("Age", min_value=18, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
driving_license = st.selectbox("Driving License", ["Yes", "No"])
region_code = st.number_input("Region Code", min_value=0, max_value=52)
previously_insured = st.selectbox("Previously Insured", ["Yes", "No"])
vehicle_age = st.selectbox("Vehicle Age", ["< 1 Year", "1-2 Year", "> 2 Years"])
vehicle_damage = st.selectbox("Vehicle Damage", ["Yes", "No"])
annual_premium = st.number_input("Annual Premium", min_value=0)
policy_sales_channel = st.number_input("Policy Sales Channel", min_value=0)
vintage = st.number_input("Vintage", min_value=0)

# Create a button to submit the data and get a prediction
if st.button("Get Prediction"):
    # Convert the input data into a Pandas DataFrame
    data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Driving_License": [driving_license],
        "Region_Code": [region_code],
        "Previously_Insured": [previously_insured],
        "Vehicle_Age": [vehicle_age],
        "Vehicle_Damage": [vehicle_damage],
        "Annual_Premium": [annual_premium],
        "Policy_Sales_Channel": [policy_sales_channel],
        "Vintage": [vintage]
    })

    # Convert categorical variables into numerical variables
    data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
    data['Driving_License'] = data['Driving_License'].map({'Yes': 1, 'No': 0})
    data['Previously_Insured'] = data['Previously_Insured'].map({'Yes': 1, 'No': 0})
    data['Vehicle_Age'] = data['Vehicle_Age'].map({'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2})
    data['Vehicle_Damage'] = data['Vehicle_Damage'].map({'Yes': 1, 'No': 0})

    # Create Age_Group by Range and also Create Dummy Columns of Age_Group
    data['Age_Group'] = pd.cut(data['Age'], bins=[18, 40, 60, 100], labels=['18-40', '40-60', '60+'])
    data = pd.get_dummies(data, columns=['Age_Group'], prefix='Age_Group')

    # Drop unnecessary columns
    data = data.drop(['Gender', 'Age', 'Driving_License', 'Region_Code', 'Vintage', 'Policy_Sales_Channel'], axis=1)

    # Scale the data using StandardScaler
    X_scaled = scaler.transform(data)

    # Make a prediction using the loaded model
    prediction = model.predict(X_scaled)

    # Display the prediction
    if prediction[0] == 1:
        st.write("The customer Renew insurance policy.")
    else:
        st.write("The customer Claim insurance policy.")