import model
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def evaluate(train):

	for h in model.get_headers(train):
		fig = plt.figure()
		plt.title("Scatter Plot {}".format(h))
		plt.scatter(range(len(train[h])), train[h])
		fig.savefig("Output/Images/Scatter Plot {}.png".format(h))
		fig = plt.figure()
		plt.title("Compare {} With Target".format(h))
		plt.scatter(train[h], train[model.TARGET])
		fig.savefig("Output/Images/Compare {} With Target.png".format(h))

def pull_final_version():
	'''
	Returns the final version of features, train, and test sets
	'''
	return

if __name__ == "__main__":
	train, test = model.get_train_test(False)
	evaluate(train)