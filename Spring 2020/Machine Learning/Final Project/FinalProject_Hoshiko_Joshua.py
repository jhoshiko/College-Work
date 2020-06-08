
# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import os

# Final Project
# Joshua Hoshiko
# This project compares three classifiers, logistic regression, KNN, and support vector machine
# There are several variations in the dataset to compare and constrast different scenarios
# Including different training and testing splits. There is also a full feature analysis as well.

# Logistic Regression    
def logistic_regression (x_train, y_train, x_test, y_test, class_names, full_report_bool):
    logreg_model = LogisticRegression()
    logreg_model.fit(x_train,y_train)
    y_pred=logreg_model.predict(x_test)
    print("*****Logistic Regression*****")
    if full_report_bool:
        print(classification_report(y_test, y_pred, target_names=class_names))
        print("Confusion-Matrix:")
        print(confusion_matrix(y_test, y_pred))
    else:
        print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
        print("Confusion-Matrix:")
        print(confusion_matrix(y_test, y_pred))

# K-Nearest Neighbor    
def k_nearest_neighbor (x_train, y_train, x_test, y_test, class_names, full_report_bool):
    le = LabelEncoder()
    labels = le.fit_transform(Y)
    KNN_model = KNeighborsClassifier(n_neighbors=5, p = 2)
    KNN_model.fit(x_train, y_train)
    print("*****K-Nearest Neighbor*****")
    if full_report_bool:
        print(classification_report(y_test, KNN_model.predict(x_test), target_names=class_names))
        print("Confusion-Matrix:")
        print(confusion_matrix(y_test, KNN_model.predict(x_test)))
    else:
        print("Accuracy:", round(accuracy_score(y_test, KNN_model.predict(x_test)), 4))
        print("Confusion-Matrix:")
        print(confusion_matrix(y_test, KNN_model.predict(x_test)))

# Support Vector Machine
def support_vector_machine (x_train, y_train, x_test, y_test, class_names, full_report_bool):
    Gamma = 0.001
    C = 1
    SVM_model = SVC(kernel='linear', C=C, gamma=Gamma)
    SVM_model.fit(x_train, y_train)
    print("*****Support Vector Machine*****")
    if full_report_bool:
        print(classification_report(y_test, SVM_model.predict(x_test), target_names=class_names))
        print("Confusion-Matrix:")
        print(confusion_matrix(y_test, SVM_model.predict(x_test)))
    else:
        print("Accuracy:", round(accuracy_score(y_test, SVM_model.predict(x_test)), 4))
        print("Confusion-Matrix:")
        print(confusion_matrix(y_test, SVM_model.predict(x_test)))

# Some values for the testing, such as the training percentages and class names
training_percentages = [.7, .4, .01]
class_names = ["Edible", "Poisonous"]
feature_train_percent = 0.7

# Feature names and dictionary for feature specific testing
cols = ['cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size',
    'gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring',
    'stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']
features_data = {}

# load dataset and convert catagorical data to dummy variables
data = pd.read_csv("mushrooms.csv", header=0)
print("\nGenerating dummy variable table...")
processed_data = pd.get_dummies(data, drop_first=True)
print(processed_data)   

# Split the data into X and Y components
print("\nSplitting data into X and Y components...")
X = processed_data.iloc[: , 1:]
Y = processed_data.iloc[: , 0]
print(X) 
print(Y)

# Loop through all desired testing percentages
for t_percent in training_percentages:
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=t_percent, test_size=1-t_percent, random_state=0)
    
    print("=================================================================================")
    print("Testing all features with a", str(round(t_percent*100))+"%", "training and", 
        str(round((1-t_percent)*100))+"%", "testing split...") 
    logistic_regression (x_train, y_train, x_test, y_test, class_names, True)
    k_nearest_neighbor (x_train, y_train, x_test, y_test, class_names, True)
    support_vector_machine(x_train, y_train, x_test, y_test, class_names, True)


# Individual feature testing
# First split the features to be individual dummied dataframes and then assign them a key in the dictionary
print("\nPreparing individual feature subsets")
for column in cols:
    feature_dummy = pd.get_dummies(data[column], drop_first=True)
    if not feature_dummy.empty:
        features_data[column] = feature_dummy

# For each dataframe in the dictionary, split it into training and testing data, test the data with all three models,
# and then print the results
for feature in features_data:
    X = features_data[feature]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=feature_train_percent,
         test_size=1-feature_train_percent, random_state=0)
    
    print("=================================================================================")
    print("Testing feature:", feature ,"with a", str(round(feature_train_percent*100))+"%", "training and", 
        str(round((1-feature_train_percent)*100))+"%", "testing split...") 
    logistic_regression (x_train, y_train, x_test, y_test, class_names, False)
    k_nearest_neighbor (x_train, y_train, x_test, y_test, class_names, False)
    support_vector_machine(x_train, y_train, x_test, y_test,class_names, False)
    

