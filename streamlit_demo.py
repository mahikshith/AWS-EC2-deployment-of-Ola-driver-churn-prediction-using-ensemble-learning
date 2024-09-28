
# col	                    feature_importance
# 7	Quarterly Rating	         0.576385
# 8	quarterly_rating_inc	     0.118021
# 4	Joining Designation	         0.081287
# 6	Total Business Value	     0.061696
# 5	Grade	                     0.056614
# 1	Gender	                     0.026204
# 0	Age	                         0.026035
# 9	monthly_income_increase	      0.018829
# 2	Education_Level	              0.018340
# 3	Income	                       0.016590 

import pandas as pd 
import streamlit as st 
import pickle
from sklearn.preprocessing import StandardScaler

model = pickle.load(open("demo_final_xgb.pkl","rb")) 


# Function to standardize and predict
def predict_churn(data):
    # Standardize all numerical features (including ordinal features)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    # Make prediction
    prediction = model.predict(data)

    return prediction[0]

# grade - [1,2,3,4,5] , Joining Designation -  [1,2,3,4,5] , Gender -  [0, 1], Education_Level - [0,1,2] 

# monthly_income_increase - [0 ,1], quarterly_rating_inc - [0 , 1], quarterly_rating - [1,2,3,4]

def main():
    st.title("OLA - Driver Churn Prediction")

    # Input fields arranged side-by-side
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age")
        gender = st.selectbox("Gender", [0,1])
        education_level = st.selectbox("Education Level", [0,1,2])
        income = st.number_input("Income")
        grade = st.selectbox("Grade", [1, 2, 3, 4,5])
    with col2:
        joining_designation = st.selectbox("Joining Designation", [1, 2, 3, 4, 5]) 
        total_business_value = st.number_input("Total Business Value")
        quarterly_rating = st.selectbox("Quarterly Rating", [1, 2, 3, 4])
        quarterly_rating_inc = st.selectbox("Quarterly Rating Increment", [0, 1])
        monthly_income_increase = st.selectbox("Monthly Income Increase", [0, 1])

    # Create a DataFrame with input values
    data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education_Level': [education_level],
        'Income': [income],
        'Joining Designation': [joining_designation],
        'Grade': [grade],
        'Total Business Value': [total_business_value],
        'Quarterly Rating': [quarterly_rating],
        'quarterly_rating_inc': [quarterly_rating_inc],
        'monthly_income_increase': [monthly_income_increase]
    })



    # Predict churn
    if st.button("Predict"):
        prediction = predict_churn(data)

        if prediction == 1:
            st.error("Driver-partner is likely to churn.")
        else:
            st.success("Driver-partner is not likely to churn.")

if __name__ == '__main__':
    main()