
# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from imutils import paths
import numpy as np
import pandas as pd
import scipy.misc
import cv2
import os

# Midterm project 4
# Joshua Hoshiko
# This project compares three classifiers, logistic regression, KNN, and support vector machine
# There are several variations in the dataset to compare and constrast different scenarios, 
# such as focusing on certain flower features or changing the size of the training slice.

# Logistic Regression    
def logistic_regression (x_train, y_train, x_test, y_test):
    logreg_model = LogisticRegression()
    logreg_model.fit(x_train,y_train)
    y_pred=logreg_model.predict(x_test)
    print("*****Logistic Regression*****")
    print(classification_report(y_test, y_pred))

# K-Nearest Neighbor    
def k_nearest_neighbor (x_train, y_train, x_test, y_test):
    le = LabelEncoder()
    labels = le.fit_transform(Y)
    KNN_model = KNeighborsClassifier(n_neighbors=5, p = 2)
    KNN_model.fit(x_train, y_train)
    print("*****K-Nearest Neighbor*****")
    print(classification_report(y_test, KNN_model.predict(x_test), target_names=le.classes_))

# Support Vector Machine
def support_vector_machine (x_train, y_train, x_test, y_test):
    Gamma = 0.001
    C = 1
    SVM_model = SVC(kernel='linear', C=C, gamma=Gamma)
    SVM_model.fit(x_train, y_train)
    print("*****Support Vector Machine*****")
    print(classification_report(y_test, SVM_model.predict(x_test)))

# Read in CSV data and name the columns appropriately 
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'label']
# load dataset
data = pd.read_csv("iris.csv", header=None, names=col_names)

# Load data into X and Y repectively. Create some partial feature versions of X data as well for testing
feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
feature_cols2 = ['sepal_length', 'sepal_width']
feature_cols3 = ['petal_length', 'petal_width']
X = data[feature_cols]
X2 = data[feature_cols2]
X3 = data[feature_cols3]
Y = data['label']

# Split the data into training and testing data with 70% training and 30% testing. All four features
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3, random_state=0)

# Split the data into training and testing data with 40% training and 60% testing. All four features
x_train2, x_test2, y_train2, y_test2 = train_test_split(X, Y, train_size=0.4, test_size=0.6, random_state=0)

# Split the data into training and testing data with 10% training and 90% testing. All four features
x_train3, x_test3, y_train3, y_test3 = train_test_split(X, Y, train_size=0.1, test_size=0.9, random_state=0)

# Split the data into training and testing data with 70% training and 30% testing. Only sepal features
x_train4, x_test4, y_train4, y_test4 = train_test_split(X2, Y, train_size=0.7, test_size=0.3, random_state=0)

# Split the data into training and testing data with 70% training and 30% testing. Only petal features
x_train5, x_test5, y_train5, y_test5 = train_test_split(X3, Y, train_size=0.7, test_size=0.3, random_state=0)

# print("x_train/x_test contents")
# print(x_train)
# print(x_test)
# 
# print("y_train/y_test contents")
# print(y_train)
# print(y_test)

# Test all four features with a 70% training and 30% testing split
print("Testing all four features with a 70% training and 30% testing split...") 
logistic_regression (x_train, y_train, x_test, y_test)
k_nearest_neighbor (x_train, y_train, x_test, y_test)
support_vector_machine(x_train, y_train, x_test, y_test)

# Test all four features with a 40% training and 60% testing split
print("Testing all four features with a 40% training and 60% testing split...") 
logistic_regression (x_train2, y_train2, x_test2, y_test2)
k_nearest_neighbor (x_train2, y_train2, x_test2, y_test2)
support_vector_machine(x_train2, y_train2, x_test2, y_test2)

# Test all four features with a 10% training and 90% testing split
print("\nTesting all four features with a 10% training and 90% testing split...")
logistic_regression (x_train3, y_train3, x_test3, y_test3)
k_nearest_neighbor (x_train3, y_train3, x_test3, y_test3)
support_vector_machine(x_train3, y_train3, x_test3, y_test3)

# Test only sepal features with a 70% training and 30% testing split
print("\nTesting only SEPAL features with a 70% training and 30% testing split...")
logistic_regression (x_train4, y_train4, x_test4, y_test4)
k_nearest_neighbor (x_train4, y_train4, x_test4, y_test4)
support_vector_machine(x_train4, y_train4, x_test4, y_test4)

# Test only petal features with a 70% training and 30% testing split
print("\nTesting only PETAL features with a 70% training and 30% testing split...")
logistic_regression (x_train5, y_train5, x_test5, y_test5)
k_nearest_neighbor (x_train5, y_train5, x_test5, y_test5)
support_vector_machine(x_train5, y_train5, x_test5, y_test5)

