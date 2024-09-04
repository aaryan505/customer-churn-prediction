# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
data = pd.read_csv('data/customer_data.csv')

# Data preprocessing
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
data.fillna(data.mean(), inplace=True)

# Feature selection
X = data[['Age', 'Income', 'CreditScore', 'Gender']]
y = data['Churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Display the results
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)
