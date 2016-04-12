from __future__ import division
import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import features

WRITE = "Output/Model-Summary.txt"
TARGET = "SeriousDlqin2yrs"

def get_train_test(configure = False):
	'''
	Reads in from global csv files, returns train, test, and features
	'''
	train = pd.read_csv("Output/conditional_transformed.csv")
	test = pd.read_csv("Output/mean_transformed_test.csv")
	return train, test, get_headers(train)

def get_headers(train):
	return list(train.columns.values)[2:]

def test_classifiers(train, test, features):
	'''
	Takes train and test data frames, along with list of features
	Builds and evaluates classifiers
	Writes results to output file
	'''
	with open (WRITE, 'w') as f:
		f.write("Classifiers Summary\n")
		classifiers = [LogisticRegression()]

		for clf in classifiers:
			f.write("\nTesting Classifier: {}".format(clf))
			clf.fit(train[features], train[TARGET])
			probabilities = clf.predict_proba(test[features])
			predictions = clf.predict(train[features])
			accuracy = metrics.accuracy_score(train[TARGET], predictions)
			f.write("\n      Accuracy at: {}".format(accuracy))

if __name__ == "__main__":
	train, test, features = get_train_test()
	test_classifiers(train, test, features)