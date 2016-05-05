import pandas as pd
import sys

# call this file once for training transform, once for testing transform

FILE = "/home/egwebber/ML-Programing-Assignments/PA-02/Data/cs-training.csv"
OUTPUT = "/home/egwebber/ML-Programing-Assignments/PA-03/Output/training-transformed.csv"


# fix this mean / median business

def go():
	df = pd.read_csv(FILE)
	for i in range(df.shape[1]):
		if df.iloc[i].isnull().values.any():
			m = df.iloc[i].mean()
			df.iloc[i] = df.iloc[i].fillna(m)
	df.to_csv(OUTPUT)

if __name__ == "__main__":
	go()



	# if len(sys.argv) != 3:
	# 	print ("usage: python {} <raw data filename> <result filename>".format(sys.argv[0]))
	# 	sys.exit(1)
	# go(sys.argv[1], sys.argv[2])