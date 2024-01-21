import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
df = pd.read_csv('./Datasets/IRIS.csv')

# Clustering models
kmeans_model = KMeans(n_clusters=3, random_state=42)
gmm_model = GaussianMixture(n_components=3, random_state=42)

# Features for clustering
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = df[features]

# Fit clustering models
kmeans_labels = kmeans_model.fit_predict(X)
gmm_labels = gmm_model.fit_predict(X)

# Decision Tree model
dt_model = DecisionTreeClassifier()
dt_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
dt_X = df[dt_features]
dt_y = df['species']
dt_model.fit(dt_X, dt_y)

# Streamlit App
st.set_page_config(page_title="Iris Flower Prediction", page_icon=":hibiscus:")
st.title("Iris Flower Prediction App")

# User Input for Measurements
sepal_length = st.slider("Sepal Length", float(df['sepal_length'].min()), float(df['sepal_length'].max()), float(df['sepal_length'].mean()))
sepal_width = st.slider("Sepal Width", float(df['sepal_width'].min()), float(df['sepal_width'].max()), float(df['sepal_width'].mean()))
petal_length = st.slider("Petal Length", float(df['petal_length'].min()), float(df['petal_length'].max()), float(df['petal_length'].mean()))
petal_width = st.slider("Petal Width", float(df['petal_width'].min()), float(df['petal_width'].max()), float(df['petal_width'].mean()))

# Display User Input
st.subheader("User Input:")
user_input = pd.DataFrame({
    'sepal_length': [sepal_length],
    'sepal_width': [sepal_width],
    'petal_length': [petal_length],
    'petal_width': [petal_width]
})
st.table(user_input)

# Clustering Predictions
st.subheader("Clustering Predictions:")
st.write("K-Means Cluster:", kmeans_model.predict(user_input[features])[0])
st.write("Gaussian Mixture Model Cluster:", gmm_model.predict(user_input[features])[0])

# Decision Tree Prediction
st.subheader("Decision Tree Prediction:")
dt_prediction = dt_model.predict(user_input[dt_features])[0]
st.write("Predicted Species:", dt_prediction)


# Custom CSS styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stAlert {
            background-color: #d9edf7 !important;
            color: #31708f !important;
            border-color: #bce8f1 !important;
        }
        .stTable {
            background-color: #ffffff;
            color: #555555;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Note: You can further customize the appearance and layout of the app based on your preferences.
