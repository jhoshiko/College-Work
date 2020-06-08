
"""
Created on Tuesday Oct 2, 2018
@author: Madhuri Suthar, UCLA
"""

"""
Joshua Hoshiko
Homework 5

"""

# Imports
import numpy as np
import pandas as pd 

data = pd.read_csv("mushrooms.csv", header=0)
processed_data = pd.get_dummies(data, drop_first=True)

X = processed_data.iloc[: , 1:].to_numpy()
y = processed_data.iloc[: , 0].to_numpy()

# Define useful functions    

# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))

# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)

# Class definition
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        self.weights1= np.random.rand(self.input.shape[1],42)
        self.weights2 = np.random.rand(6,1)
        self.y = y
        self.output = np. zeros(y.shape)
        
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
        
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2*(self.y -self.output)*sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2*(self.y -self.output)*
                                                 sigmoid_derivative(self.output), self.weights2.T)*
                                                 sigmoid_derivative(self.layer1))
    
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()
     
    def test(self, X):
        self.layer1 = sigmoid(np.dot(X, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
        

NN = NeuralNetwork(X,y)
for i in range(1500): # trains the NN 1,000 times
    if i % 300 ==0: 
        print ("for iteration # " + str(i) + "\n")
        print ("Input : \n" + str(X))
        print ("Actual Output: \n" + str(y))
        print ("Predicted Output: \n" + str(NN.feedforward()))
        print ("Loss: \n" + str(np.mean(np.square(y - NN.feedforward())))) # mean sum squared loss
        print ("\n")
  
    NN.train(X, y)
    
X_test=np.array(([0,0,0],[1,1,1]), dtype=float)
print ("Testing with X_test:\n" + str(X_test))
print ("Predicted Output: \n" + str(NN.test(X_test)))
    
    