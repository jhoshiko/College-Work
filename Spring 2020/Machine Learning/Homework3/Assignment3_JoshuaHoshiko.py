# 
# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from imutils import paths
import numpy as np
import scipy.misc
import cv2
import os


Dataset_path = "../Homework3/animals/"
class_folders = os.listdir(Dataset_path)
data = []
labels = []
print("Processing images...")
print("Directory names:", class_folders)

# Load in the images
for class_name in class_folders:
    print("Loading:", class_name + "... ")
    # Get the names of all the images
    image_list = os.listdir(Dataset_path+class_name)
    # For each image, set a label and resize the image, then append onto the appropriate liast
    for image_name in image_list:
        image = cv2.imread(Dataset_path+class_name+"/"+image_name)
        label = class_name
        image = cv2.resize(image, (32, 32),interpolation=cv2.INTER_CUBIC)
        data.append(image)
        labels.append(label)
    print("Done!")

# Create tuple and taking the lists and making NP arrays
# We need to reshape the data and fit the labels as well        
data = np.array(data)
labels = np.array(labels)
data = data.reshape((data.shape[0], 3072))
le = LabelEncoder()
labels = le.fit_transform(labels)

# Split the data into the appropriate sizes
X_train, X_tv, y_train, y_tv = train_test_split(data, labels, test_size=0.30, random_state=0)
X_test, X_valid, y_test, y_valid = train_test_split(X_tv, y_tv, test_size=0.66, random_state=0)

# Prepare our k-values and distance metrics
k_values = [3, 5, 7]
distance_metrics = {1: "Manhattan", 2: "Euclidean"}
best_accuracy = 0
best_params = []

# Loop through and test all the different combinations of the distance metrics and k-values
print("Moving to test data with KNNClassifier...\n")
print("***Scoring based on accuracy***")
for l, type in distance_metrics.items():
    print("\n******** Current L-Type:", type, "********\n")
    for k in k_values:
        print("Current k-value:", k)
        model = KNeighborsClassifier(n_neighbors=k, p = l)
        model.fit(X_train, y_train)
        y_pred=model.predict(X_valid)
        tested_accuracy = accuracy_score(y_valid, y_pred)
        print("Accuracy:", tested_accuracy, "\n")
        
        if tested_accuracy > best_accuracy:
            best_accuracy = tested_accuracy
            best_params = [k, l]  
print("\nDetermined most accurate combination:", "k = " + str(best_params[0]), 
      "and distance-metric = " +  distance_metrics[best_params[1]])
print("\nPerforming final test with testing data...")
model = KNeighborsClassifier(n_neighbors=best_params[0], p = best_params[1])
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test), target_names=le.classes_))