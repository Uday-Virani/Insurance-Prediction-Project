## Insurance-Prediction-Project
**Machine Learning project**

This project aims to predict whether customers are likely to purchase vehicle insurance based on their attributes. Additionally, a Power BI dashboard was created for visual insights into the dataset.

## Dataset Description
The dataset contains various customer details and insurance-related features, which are used to predict customer interest in vehicle insurance.

## Key Features:
**id** : Unique identifier for each customer.  
**Gender** : Customer's gender.   
**Age** : Customer's age.  
**Driving_License** : Whether the customer holds a driving license (1 = Yes, 0 = No).   
**Region_Code** : Code representing the region the customer is from.   
**Previously_Insured** : Whether the customer already has insurance (1 = Yes, 0 = No).   
**Vehicle_Age** : Age of the customer's vehicle (< 1 Year, 1-2 Year, > 2 Years).   
**Vehicle_Damage** : Indicates if the customer’s vehicle was previously damaged (Yes, No).   
**Annual_Premium** : Amount the customer pays annually for insurance.   
**Policy_Sales_Channel** : Sales channel used to communicate with the customer.   
**Vintage** : Number of days the customer has been associated with the company.   
**Response** : Target variable indicating whether the customer is interested in purchasing vehicle insurance (1 = Yes, 0 = No).   

## Jupyter Notebook: Insurance_Customer_Prediction.ipynb
This notebook contains the complete machine learning pipeline, including:  

**Data Preprocessing** : Handling missing values, encoding categorical variables, and feature scaling.  
**Exploratory Data Analysis (EDA)** : Insights into the distribution of features and relationships between variables.  
**Model Building** : Training machine learning models (e.g., Logistic Regression, Decision Trees, Random Forest) to predict the likelihood of a customer purchasing insurance.  
**Hyperparameter Tuning** : Optimizing model performance using RandomizedSearchCV.  
**Model Evaluation** : Assessing model performance using metrics like accuracy, precision, recall, and F1-scores.   
**Model Save** : Model saved by using Joblib which can be used without retraining in future. 

## Streamlit App: Insurance_prediction_Streamlit.py
This is a web application built using Streamlit, which allows users to:  

Input customer details through an interactive interface.  
Get real-time predictions on whether a customer will purchase vehicle insurance.  

## To Run the Streamlit App:  
**Install Streamlit** : pip install streamlit  
**Execute the command** : streamlit run Insurance_prediction_Streamlit.py  
Use the app to predict insurance purchases based on new customer inputs.  

## Power BI Dashboard  
In addition to the machine learning models, a Power BI dashboard was developed to visualize and analyze the data. Key insights from the dashboard include:  

Distribution of customer age, gender, and regions.  
Correlation between vehicle age, damage history and Driving_License.  
Annual premiums and their impact on customer decisions.  

To explore the dashboard, open the Power BI report and interact with the visualizations for a better understanding of the data patterns.

