# Clustering and Decision Tree Analysis on Iris Dataset

## Objective

The goal of this notebook is to explore morphological variations within the Iris species using unsupervised machine learning techniques. This analysis aims to benefit various stakeholders, including botanists, researchers, and horticulturists, by enhancing our understanding of the diversity present in Iris flowers.

## Data Import and Preliminary Analysis

- The dataset is imported and examined for basic statistics, class distribution, and missing values.
- The Iris dataset comprises 150 observations with features such as sepal length, sepal width, petal length, and petal width, categorized into three species: Iris-setosa, Iris-versicolor, and Iris-virginica.

### Check for Missing Values

- No missing values are found in the dataset.

## Exploratory Data Analysis

### Check for Outliers

- Box plots are used to identify outliers in sepal and petal measurements across different Iris species.
- Outliers are detected and subsequently handled through a combination of Winsorization and replacement with median values.

### Visualization of Outlier-Handled Data

- Box plots are re-visualized after handling outliers to ensure their successful removal.

## Clustering Techniques

### 1. K-Means Clustering

#### Elbow Method

- The Elbow Method is used to determine the optimal number of clusters.
- The bend in the graph suggests three clusters.

#### K-Means Training and Visualization

- The K-Means model is trained with three clusters.
- Resulting clusters are visualized along with centroids.

### 2. Hierarchical Clustering

#### Dendrogram Analysis

- A dendrogram is employed to identify the optimal number of clusters.
- The analysis supports the presence of three clusters.

#### Hierarchical Clustering Training and Visualization

- The Hierarchical Clustering model is trained with three clusters.
- Clusters are visualized.

### 3. Gaussian Mixture Model (GMM)

#### BIC for GMM

- Bayesian Information Criterion (BIC) is used to choose the optimal number of components.
- Three clusters are selected.

#### GMM Training and Visualization

- The GMM model is trained with three components.
- Resulting clusters are visualized.

## Decision Tree Analysis

- A Decision Tree is employed for classification tasks, both with and without pre-pruning.

### Post-Pruning Decision Tree

- A Decision Tree is visualized and analyzed before and after post-pruning.

### Pre-Pruning Decision Tree

- Grid Search Cross-Validation is utilized to find optimal hyperparameters for pre-pruning the Decision Tree.
- The pre-pruned tree is visualized and analyzed.

## Conclusion

This comprehensive analysis employs clustering techniques and Decision Tree analysis on the Iris dataset, providing valuable insights into the morphological variations of Iris flowers.

____

## Iris Flower Prediction App Documentation

### Overview:

The Iris Flower Prediction App is a simple web application developed using Streamlit. It allows users to input measurements of an Iris flower's sepal length, sepal width, petal length, and petal width. The app then predicts the Iris species using unsupervised clustering models (K-Means and Gaussian Mixture Model) and a supervised Decision Tree classifier.

### Prerequisites:

- Python installed on your machine.
- Pip (Python package installer) installed.

### Installation:

1. Clone or download the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Project_Directory
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App:

1. Open your terminal or command prompt.

2. Navigate to the project directory if not already there:

   ```bash
   cd Project_Directory
   ```

3. Run the Streamlit app using the following command:

   ```bash
   streamlit run app.py
   ```

4. After running the command, Streamlit will provide a local URL (usually http://localhost:8501) where you can access the app.

5. Open your web browser and enter the provided URL to view and interact with the Iris Flower Prediction App.

### How to Use the App:

1. Upon opening the app, you will see sliders in the sidebar for entering measurements.

2. Adjust the sliders to input Iris measurements for sepal length, sepal width, petal length, and petal width.

3. The app will display the user input in a table.

4. Predictions will be updated in real-time using both unsupervised clustering models and a supervised Decision Tree classifier.

5. The app provides information about the clustering predictions and the Decision Tree prediction.

### Additional Information:

- The app uses a clean and attractive interface with custom styling for better user experience.

- Feel free to explore the code in the `app.py` file to understand the implementation details and customize it further.

- The app can be customized by modifying the code, such as changing colors, adding features, or enhancing the user interface.

Enjoy using the Iris Flower Prediction App!