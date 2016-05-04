# Next Iteration

- Edits
	- Use histograms instead of scatter plots
 	- Use more plots: more histograms over predictors, and more histograms over pairs of predictors
 	- Change get_header() function
 	- Change read file to parameter, not global variables
 	- Set all global variables in one place if they're coming directly from the data set
 	- Have test_classifier() return a dictionary instead of writing to a file
 	- Imput values in held out set from training stats

- Add to Implementation
	- Split to train and test set
		- just worry about one k in k-folds cross validation for now
	- Bag of Classifiers
		- Include a parameter for how many classifiers you want to run
		- Logistic Regression, K-Nearest Neighbor, Decision Trees, Linear SVC, Random Forests, Boosting, Bagging
			- alternate parameters for each
	- Evaluation Metrics
		- Accuracy, Precision, Recall, F1, Area Under the Curve, Precision-Recall Curves
	- Produce a comparison table of each classifiers against the others

- Deliverable
	- full-fledged and modular modeling file
	- two page report describing the performance of the classifiers
		- try to answer the credit problem
