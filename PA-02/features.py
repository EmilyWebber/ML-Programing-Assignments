'''
features.py

Used to evauate features for ML pipeline
	- scatter plots
	- comparison against target category
By Emily Webber
April 13, 2016
'''
import model
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def graph_features(train):

	for h in model.get_headers(train):
		fig = plt.figure()
		plt.title("Scatter Plot {}".format(h))
		plt.scatter(range(len(train[h])), train[h])
		fig.savefig("Output/Images/Scatter Plot {}.png".format(h))
		fig = plt.figure()
		plt.title("Compare {} With Target".format(h))
		plt.scatter(train[h], train[model.TARGET])
		fig.savefig("Output/Images/Compare {} With Target.png".format(h))

if __name__ == "__main__":
	train, test = model.get_train_test(False)
	graph_features(train)
