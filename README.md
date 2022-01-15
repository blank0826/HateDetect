# <ins>**HateDetect**</ins>
# Description
This is a software that takes in comments and checks whether that comment is in hate or not.. 

The code is written through **Python**.

## Objective

### [Hate Detect](https://github.com/blank0826/HateDetect/blob/master/Hate_Speech_Detection.py)
----
  **<ins>This program can be divided into "" sections:</ins>** <br /><br />
  **<ins>1. Dataset**</ins><br/>
  It consisted of 7 columns which consisted of comments, whether it is hateful or can be used in normal language, count of how much of each category is in the comment.<br/>
  
  **<ins>2. Setting up Data;**</ins><br/>
    Store comments and counts in an array from the dataset. Map the comments based on the count in dataset. Used stemmer and stopwords to remove any filler words on the comments.<br/>
  
  **<ins>3. Training and Testing of the Data**</ins><br/>
  Divide the dataset into 2 parts based on comments and labels. After that, create the matrix of tokenized counts using Count Vectorizer.<br/>
  Then use train_test_split to divide the data into training and testing be specifying that each of them has 33% of the data and random state was set to 42 so that it gives almost the same answer in each execution.<br/>
  After divison, use the training data to train the system and then later it can be used to check the comments.<br/><br/>
  
  **<ins>4. hate_speech_detection() [Main Function]</ins>**<br/>
  This is the main function. Initally streamlit is set up which is used to for showing input and ouput in python code in the form of a website. Then we take input from the user and send it into the decision classifier to tell the category of the comment. Then output it into the website. <br/><br/>

# Local Setup

## Pre-Requisites
An IDE that supports Python.
## Installation and Execution
1. Pull this code into any folder.<br />
2. Open this folder in your preferred IDE.<br />
3. Build the Project.<br />
4. Run the [BlockWorldProgram](https://github.com/blank0826/Goal-Stack-Planner/blob/master/BlockWorldProgram.java) file.<br />

# Screenshots
## **<ins>TestCase**</ins><br/><br/>
<img src="https://user-images.githubusercontent.com/33955028/141432689-60a3673e-47cc-4476-98e4-bcfd705910c6.png" width="700" height="250">

## **<ins>Output**</ins><br/><br/>
<img src="https://user-images.githubusercontent.com/33955028/141425506-8601c350-959c-4e2f-8e59-efdac7d18b87.png" width="600" height="525">
<img src="https://user-images.githubusercontent.com/33955028/141425549-3ab7c648-cf70-43b5-be1e-e1533cffff84.png" width="500" height="525">
<img src="https://user-images.githubusercontent.com/33955028/141425600-a3cbab38-f1c5-4f2e-b890-e3838464e2c8.png" width="450" height="300">

___To check other displays see all the output files in the directory.___

  
# Contact
## [Aditya Srivastava](mailto:aditya26052002@gmail.com?subject=GitHub)
