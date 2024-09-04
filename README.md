# Customer Churn Prediction 

## Overview
This project demonstrates a basic approach to predicting customer churn using a Random Forest model in Python. It includes data preprocessing, model training, and evaluation.

## Project Structure
- **customer_churn_prediction.py**: The Python script containing the entire code for the project.
- **data/**: Folder containing the dataset.
- **requirements.txt**: Python packages required to run the script.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/aaryan505/customer-churn-prediction.git
2. Navigate to the project directory:
   cd customer-churn-prediction-basic
3. Install the required packages:
   pip install -r requirements.txt
4. Place your dataset (customer_data.csv) in the data/ folder.
5. Run the script
   python customer_churn_prediction.py
## Results
The model achieved an accuracy of 82.23% on the test set. Below is a classification report showing detailed performance metrics.
Model Accuracy: 82.23%
Classification Report:
              precision    recall  f1-score   support

           0       0.83      0.87      0.85       200
           1       0.79      0.74      0.77       100

    accuracy                           0.82       300
   macro avg       0.81      0.81      0.81       300
weighted avg       0.82      0.82      0.82       300
## Key Libraries
pandas
scikit-learn
## Dataset
The dataset used for this project is expected to be a CSV file containing customer data with features like Age, Income, CreditScore, Gender, and Churn.



   
