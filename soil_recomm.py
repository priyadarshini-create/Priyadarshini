import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import base64


st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Soil Recommendation"}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('12.jpg')


# Read the CSV file
data = pd.read_excel('tree_soil_recommendation_dataset (11).xlsx')
st.write(data)

# Display the content
missing_values = data.isnull().sum()

# Display columns with missing values
st.write("Missing values in each column:")
st.write(missing_values)

# Display total missing values in the dataset
total_missing = data.isnull().sum().sum()
st.write(f"Total missing values: {total_missing}")
# Display the first few rows
st.write("Original Data:")
st.write(data.head())

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Example: Encoding 'Tree Recommendation' column
data['Tree Recommendation'] = label_encoder.fit_transform(data['Tree Recommendation'])

st.write("\nData After Label Encoding:")
st.write(data.head())

# Separate features (X) and target (y)
X = data.drop(columns=['Tree Recommendation'])
y = data['Tree Recommendation']

# Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the results
st.write("X_train:", X_train.head())
st.write("X_test:", X_test.head())
st.write("y_train:", y_train.head())


# Initialize Decision Tree Classifier
model_dt = DecisionTreeClassifier()
model_dt.fit(X_train, y_train)
predictions_dt = model_dt.predict(X_test)
accuracy_dt = accuracy_score(y_test, predictions_dt)

# Initialize Random Forest Classifier
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
predictions_rf = model_rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, predictions_rf)

# Initialize Naive Bayes Classifier
model_nb = GaussianNB()
model_nb.fit(X_train, y_train)
predictions_nb = model_nb.predict(X_test)
accuracy_nb = accuracy_score(y_test, predictions_nb)

# Initialize AdaBoost Classifier
model_ab = AdaBoostClassifier(n_estimators=50, random_state=42)
model_ab.fit(X_train, y_train)
predictions_ab = model_ab.predict(X_test)
accuracy_ab = accuracy_score(y_test, predictions_ab)

# Add checkboxes for displaying accuracy results
show_dt = st.checkbox('Show Decision Tree Accuracy')
show_rf = st.checkbox('Show Random Forest Accuracy')
show_nb = st.checkbox('Show Naive Bayes Accuracy')
show_ab = st.checkbox('Show AdaBoost Accuracy')

if show_dt:
    st.write(f"DecisionTree Accuracy: {accuracy_dt * 100:.2f}%")

if show_rf:
    st.write(f"RandomForest Accuracy: {accuracy_rf * 100:.2f}%")

if show_nb:
    st.write(f"Naive Bayes Accuracy: {accuracy_nb * 100:.2f}%")

if show_ab:
    st.write(f"AdaBoost Accuracy: {accuracy_ab * 100:.2f}%")

# Button for triggering soil recommendation
b1 = st.button('Recommendation')
if b1:
    import subprocess
    subprocess.run(['streamlit', 'run', 'cropsoil.py'])
