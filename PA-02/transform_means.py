import csv

READ_FILE = "Data/cs-test.csv"
WRITE_MEAN = "Output/mean_transformed_test.csv"
WRITE_CONDITIONAL = "Output/conditional_transformed_test.csv"

# how should we handle imputing values into a discrete variable when the mean is not discrete?
MEAN = {11:1, 6:6670}

COND_MEAN = {11: {"0": 1, "1":1}, 6: {"0": 6747, "1":5630}}

# list of possible missing values
COL_ID = [6,11]

CLASS_ID = 1
MISSING = "NA"

def process_csv_readers(a, b, c):
	'''
	Takes pointers to csvs, returns initialized writer objects
	'''
	fields = csv.reader(a)
	b_write = csv.writer(b)
	c_write = csv.writer(c)
	h = next(fields)
	b_write.writerow(h)
	c_write.writerow(h)
	return fields, b_write, c_write

def transform_means(conditional = True):
	'''
	Reads global csv file, grabs gender for missing values, writes to a new csv
	'''
	with open(READ_FILE, 'rU') as a, open(WRITE_MEAN, 'w') as b, open(WRITE_CONDITIONAL, 'w') as c:
		fields, b_write, c_write = process_csv_readers(a, b, c)

		for row in fields:

			copy = row[:]
			for i in COL_ID:
				if row[i] == MISSING:
					copy[i] = MEAN[i]
			b_write.writerow(copy)

			if conditional:

				for i in COL_ID:
					if row[i] == MISSING:
						row[i] = COND_MEAN[i][row[CLASS_ID]]
				c_write.writerow(row)

if __name__ == "__main__":
	transform_means(False)