# -*- coding: utf-8 -*-
"""Neural Network

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16TSewbl6QaJE2E13VyUANegOJ7fhDDcL
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt


data = pd.read_csv("mushrooms.csv") # import data into pandas dataframe from csv file - code modified from https://www.kaggle.com/code/wenzhengding/mushroom-classification-using-neural-network/notebook
un_X = data.iloc[:,1:23] # retrieves values of specified indices for feature data (x)
un_y = data.iloc[:, 0] # retrieves values of specified indices for target data (y)
X = pd.get_dummies(un_X) # converts categorical data into dummy/indicator variables - Each variable is converted in as many 0/1 variables as there are different values
y = pd.get_dummies(un_y) # converts categorical data into dummy/indicator variables - Each variable is converted in as many 0/1 variables as there are different values
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3) # splits data into training and testing data for machine learning model

# defines fully-connected neural network for binary classification task
classifier=Sequential() 
classifier.add(Dense(32,activation='relu',input_dim=117))
classifier.add(Dense(2,activation='softmax'))
classifier.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

history = classifier.fit(X_train,y_train,batch_size=10,epochs=10, validation_split = 0.1) # trains model on training data with 10 epochs and 10% of the training data split for validation purposes

# plots the training and validation losses of the model as a function of epochs with appropriate labels and titles
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Loss', 'Validation Loss'], loc='upper left')
plt.show()

# plots the training and validation accuracies of the model as a function of epochs with appropriate labels and titles
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()