"""
Gerom Pagaduan
Dr. Jiang
Machine Learning
Mushroom Edibility Recognizer
1
"""

# Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

# load dataset and convert catagorical data to dummy variables
data = pd.read_csv("mushrooms.csv", header=0)
processed_data = pd.get_dummies(data, drop_first=True)
first_column = processed_data.iloc[:, 0]
#processed_data = processed_data.drop(processed_data.columns[[0]], axis=1)

# Changes it from a DataFrame to a Numpy.ndarray
X = processed_data.iloc[:, 1:].to_numpy()
y = processed_data.iloc[:, 0].to_numpy()
y = np.reshape(y, (8124, 1)) # Changes dimensions from (8124, ) to (8124, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=0)

processed_data.iloc[:, 0].to_csv("Y_Data-Frame.csv")
np.savetxt("Y_data.csv", y, delimiter=",")


# Define useful functions

# Activation function
def sigmoid(t):
    return 1 / (1 + np.exp(-t))


# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)


# Class definition
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 12)  # considering we have 42 nodes in the hidden layer
        self.weights2 = np.random.rand(12, 1) # output
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2

    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2 * (self.y - self.output) * sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2 * (self.y - self.output) *
                                                 sigmoid_derivative(self.output), self.weights2.T) *
                            sigmoid_derivative(self.layer1))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()

NN = NeuralNetwork(X, y)

for i in range(1500):  # trains the NN 1,500 times
    if i % 300 == 0:
        print("for iteration # " + str(i) + "\n")
        print("Input : \n" + str(X))
        print("Actual Output: \n" + str(y))
        print("Predicted Output: \n" + str(NN.feedforward()))
        print("Loss: \n" + str(np.mean(np.square(y - NN.feedforward()))))  # mean sum squared loss
        print("\n")
    NN.train(X, y)

# Test
h1 = sigmoid(np.dot(X_test, NN.weights1)) # [2 x 3] * [3 x 6]
y_pred = sigmoid(np.dot(h1, NN.weights2)) # [2 x 6] * [6 x 2]

print("\nX_test: \n", X_test)
print("\nWeight 1 dimensions: \n", NN.weights1)
print("\nHidden Layer 1: \n", h1)
print("\nWeight 2 dimensions: \n", NN.weights2)
print("\nHidden Layer 2: \n", y_pred)

print("\nTesting...\nPredicted Output: \n" + str(y_pred))
print("\nActual Output: \n" + str(y_test))

test_accuracy = metrics.accuracy_score(y_test, y_pred.round(), normalize = False)
print("\nAccuracy Score: " + str(test_accuracy))

print("\nConfusion Matrix: ")
cnf_matrix = metrics.confusion_matrix(y_test, y_pred.round())
print(cnf_matrix)
