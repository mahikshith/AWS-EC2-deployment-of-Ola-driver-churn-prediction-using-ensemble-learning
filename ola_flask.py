from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model
model = pickle.load(open("demo_final_xgb.pkl", "rb"))

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Ola Driver Churn Prediction"

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  
    # use a list of JSON if we have multiple data points
    
    # Convert the data into a DataFrame
    input_data = pd.DataFrame({
        'Age': [data['Age']],
        'Gender': [data['Gender']],
        'Education_Level': [data['Education_Level']],
        'Income': [data['Income']],
        'Joining Designation': [data['Joining_Designation']],
        'Grade': [data['Grade']],
        'Total Business Value': [data['Total_Business_Value']],
        'Quarterly Rating': [data['Quarterly_Rating']],
        'quarterly_rating_inc': [data['quarterly_rating_inc']],
        'monthly_income_increase': [data['monthly_income_increase']]
    })

    # Standardize the input features 
    scaler = StandardScaler()
    input_data_scaled = scaler.fit_transform(input_data)

    # Make  prediction
    prediction = model.predict(input_data_scaled)

    # Return the prediction result
    result = int(prediction[0])
    if result == 1:
        return jsonify({'churn_prediction': 'Driver-partner is likely to churn.'})
    else:
        return jsonify({'churn_prediction': 'Driver-partner is not likely to churn.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
