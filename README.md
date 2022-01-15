# <ins>**HateDetect**</ins>
# Description
This is software that takes in comments and checks whether that comment is in hate or not.

The code is written through **Python**.

## Objective

### [Hate Detect](https://github.com/blank0826/HateDetect/blob/master/Hate_Speech_Detection.py)
----
  **<ins>This program can be divided into 4 sections:</ins>** <br /><br />
  **<ins>1. Dataset**</ins><br/>
  It consisted of 7 columns which consisted of comments, whether it is hateful or can be used in normal language, count of how much of each category is in the comment.<br/>
  
  **<ins>2. Setting up Data;**</ins><br/>
    Store comments and counts in an array from the dataset. Map the comments based on the count in the dataset. Used stemmer and stopwords to remove any filler words in the comments.<br/>
  
  **<ins>3. Training and Testing of the Data**</ins><br/>
  Divide the dataset into 2 parts based on comments and labels. After that, create the matrix of tokenized counts using Count Vectorizer.<br/>
  Then use train_test_split to divide the data into training and testing be specifying that each of them has 33% of the data and the random state was set to 42 so that it gives almost the same answer in each execution.<br/>
  After division, use the training data to train the system ,and then later it can be used to check the comments.<br/>
  
  **<ins>4. hate_speech_detection() [Main Function]</ins>**<br/>
  This is the main function. Initially, streamlit is set up which is used for showing input and output in python code in the form of a website. Then we take input from the user and send it into the decision classifier to tell the category of the comment. Then output it into the website. <br/><br/>
  
  **Complete Documentation:** [Report](https://github.com/blank0826/HateDetect/blob/master/HateDetect%20Report.pdf)

# Local Setup

## Pre-Requisites
An IDE that supports Python.
## Installation and Execution
1. Pull this code into any folder.<br />
2. Open this folder in your preferred IDE.<br />
3. In the terminal, write <br/>
``
streamlit run Hate_Speech_Detection.py
``
5. The website will open. Enter any comment and the result will be given.<br />

# Screenshots
## **<ins>Output**</ins><br/><br/>

<img src="https://user-images.githubusercontent.com/33955028/149612902-a9e61fe6-5af9-4d39-b5e9-78a1b0fd9d4a.png" width="620" height="400">
<img src="https://user-images.githubusercontent.com/33955028/149612820-14f2cc35-3f39-4a0f-9ecd-f9fac62ba1e2.png" width="620" height="400">
  
# Contact
## [Aditya Srivastava](mailto:aditya26052002@gmail.com?subject=GitHub)
