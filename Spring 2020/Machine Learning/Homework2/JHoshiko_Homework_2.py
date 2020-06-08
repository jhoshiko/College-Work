import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Read in CSV data and name the columns appropriately 
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("pima-indians-diabetes-database.csv", header=None, names=col_names)

# Select five features from the dataset. Get the results as well
feature_cols = ['pregnant', 'age', 'bp', 'insulin', 'skin']
X = pima[feature_cols]
Y = pima['label']

# Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.6, test_size=0.4, random_state=0)

print("x_train/x_test contents")
print(x_train)
print(x_test)

print("y_train/y_test contents")
print(y_train)
print(y_test)

# Use logistic regression using the training data
logreg = LogisticRegression()
# fit the model with data
logreg.fit(x_train,y_train)

# Make predictions about the test values using the model that was generated
y_pred=logreg.predict(x_test)
print(y_pred)

# Create the confusion matrix from comparing the predicted values and the actual values
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

## Generate a heat map using the confusion matrix
class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
#sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
sns.heatmap(cnf_matrix, annot=True, cmap="YlGnBu" ,fmt='g')
#ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

# Generate the ROC curve. Also print the accuracy, precision, and recall
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
print(metrics.classification_report(y_test,y_pred))
plt.figure()
y_pred_proba = logreg.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()