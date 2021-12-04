# streamlit run Hate_Speech_Detection.py
import string  # for string operations
import streamlit as st  # open-source link which shows data in the form of website
from PIL import Image
# get rid of ugly texts that does not help in detection
from nltk.corpus import stopwords
import nltk
import re  # regex
from nltk.util import pr
import pandas as pd  # for analyzing the data
import numpy as np  # provides masks and matrices for performing various maths operations

# Convert a collection of text documents to a matrix of token counts.
from sklearn.feature_extraction.text import CountVectorizer

# Split arrays or matrices into random train and test subsets
from sklearn.model_selection import train_test_split


# A Decision Tree is a simple representation for classifying examples.
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("dataset.csv")  # reads csv file

data["labels"] = data["class"].map(
    {0: "Hate Language Detected", 1: "Hate Language Detected", 2: "No Hate"})  # maps the classes to the three categories and store it in labels

# we will choose only comment and labels for training the hate speech model
data = data[["comment", "labels"]]

# break the world into its base mode.
stemmer = nltk.SnowballStemmer("english")
# remove all filter words Eg. this, is ,an ,how
stopword = set(stopwords.words('english'))


def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    # converts the word into its base mode.
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text


# cleans the comments from any un-necessary word for analysis.
data["comment"] = data["comment"].apply(clean)

# This is to split the dataset into training and testsets
x = np.array(data["comment"])  # this contains all the comments
y = np.array(data["labels"])  # this contains all the labels


# training the model
cv = CountVectorizer()
X = cv.fit_transform(x)  # Fit the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)  # test size shows proportion of X to be included if in fraction for int it is number of lements.
# random state controls shuffling of data before splitting. this is like the seed of rng. ensure same dataset can be used multiple times and get the same result.

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)  # Train Decision Tree Classifier
# Returns the mean accuracy on the given test data and labels.
clf.score(X_test, y_test)

image = Image.open('download.png')


def hate_speech_detection():

    st.markdown(""" <style>
    # MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .big-font {
        font-size:25px !important;
    }
    </style>
    <style>
    .title-font {
        font-size:65px !important;
    }
    </style> """, unsafe_allow_html=True)

    col1, col2 = st.columns([10, 6])

    with col1:
        st.markdown('<p class="title-font"><b>HateDetect<b></p>',
                    unsafe_allow_html=True)

    with col2:
        st.image("download.png", caption='')
    st.markdown('<p class="big-font"><b>Enter any comment:<b></p>',
                unsafe_allow_html=True)
    user = st.text_area("")
    if len(user) < 1:
        st.title("")
    else:
        sample = user
        data = cv.transform([sample]).toarray()
        a = clf.predict(data)  # Predict the response for test dataset
        st.title("Result: " + a)


hate_speech_detection()
