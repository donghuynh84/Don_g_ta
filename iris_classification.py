import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Setting the screen size to maximum
st.set_page_config(layout="wide")
# col1 is the left hand sidebar
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1)) # 2 means the middle column is bigger than the right column

st.write("""
# Simple Iris Flower Prediction App
""")

st.sidebar.header("User Input Parameters")

# allowing users to select length of the features
def user_input_features():
    sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)
    # iris_class = st.sidebar.slider("Iris Class", 0, 1, 2)

# creating our data dictionary
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
            # 'Class': iris_class}
    features = pd.DataFrame(data, index=[0])
    return features

# our df is based on user input
df = user_input_features()
st.subheader("User Input Parameters")
st.write(df)
## Sidebar - allowing the user to select a classifier
your_classifier = col1.selectbox('Select a Classifier',
                                    ['RandomForest',"DecisionTree"])



iris = datasets.load_iris()
X = iris['data']
Y = iris['target']


# Random Forest Classifier
if your_classifier == "RandomForest":

    clf = RandomForestClassifier()
    clf.fit(X,Y)

    prediction = clf.predict(df)

    prediction_prob = clf.predict_proba(df)

    st.subheader("Class labels and their corresponding index number")
    st.write(iris.target_names)

    st.subheader("Prediction")
    st.write(iris.target_names[prediction])

    st. subheader("Prediction Probability")
    st.write(prediction_prob)
else: # Decision Tree Classifier
    clf = DecisionTreeClassifier(max_depth=5, random_state = 101, criterion='entropy')

    X, Y = iris['data'], iris['target']
    x_trn, x_test, y_trn, y_test = train_test_split(X,Y)
    clf.fit(x_trn,y_trn)
    prediction = clf.predict(x_test)
    accu = accuracy_score(y_test, prediction)

    st.subheader("Class labels and their corresponding index number")
    st.write(iris.target_names)

    st.subheader("Prediction")
    st.write(iris.target_names[prediction[0:3]])

    st. subheader("Accuracy Score")
    st.write(accu)
