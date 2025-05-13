import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load and cache the iris data
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load data
df, target_name = load_data()

# Train the model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Sidebar inputs
st.sidebar.title("🌿 Input Flower Features")
sepal_length = st.sidebar.slider(
    "Sepal Length (cm)", 
    float(df['sepal length (cm)'].min()), 
    float(df['sepal length (cm)'].max())
)
sepal_width = st.sidebar.slider(
    "Sepal Width (cm)", 
    float(df['sepal width (cm)'].min()), 
    float(df['sepal width (cm)'].max())
)
petal_length = st.sidebar.slider(
    "Petal Length (cm)", 
    float(df['petal length (cm)'].min()), 
    float(df['petal length (cm)'].max())
)
petal_width = st.sidebar.slider(
    "Petal Width (cm)", 
    float(df['petal width (cm)'].min()), 
    float(df['petal width (cm)'].max())
)

# Prediction input
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
prediction_species = target_name[prediction[0]]

# Show prediction result
st.write("## 🔍 Prediction Result")
st.success(f"The predicted species is: **{prediction_species}**")

# About Iris dataset
st.write("## 🌸 About Iris Dataset")
st.markdown("""
The **Iris dataset** is a classic dataset used in machine learning. It contains measurements for three types of Iris flowers. 
The prediction is based on four features: *sepal length, sepal width, petal length, and petal width*.
""")

# Detailed species table with explanations
species_info_df = pd.DataFrame({
    'Species Name': ['Setosa', 'Versicolor', 'Virginica'],
    'Description': [
        'Small petals and sepals, very easy to classify.',
        'Medium-sized petals and sepals, more variation than Setosa.',
        'Largest petals and sepals, sometimes overlaps with Versicolor.'
    ]
})

st.write("## 🌼 Iris Flower Species Overview")
st.table(species_info_df)

# Random Forest Explanation
st.write("## 🌲 About the Random Forest Classifier")
st.markdown("""
- A **Random Forest** is an ensemble model made of many **decision trees**.
- Each tree makes its prediction, and the final result is decided by **majority vote**.
- It works well for classification problems like this one.

### ✅ Benefits of Random Forest:
- Handles noisy data well
- Reduces overfitting compared to a single decision tree
- Works for both numerical and categorical features
""")
