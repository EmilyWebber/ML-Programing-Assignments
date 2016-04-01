import csv

READ_FILE = "mock_student_data.csv"
WRITE_MEAN = "Output/mean_transformed.csv"
WRITE_CONDITIONAL = "Output/conditional_transformed.csv"

MEAN = {5:17, 6:3, 7:18}
COND_MEAN = {5: {"Yes": 0, "No":0}, 6: {"Yes": 0, "No":0}, 7: {"Yes": 0, "No":0}}

COL_ID = [5,6,7]
CLASS_ID = 8

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

def transform_means():
	'''
	Reads global csv file, grabs gender for missing values, writes to a new csv
	'''
	with open(READ_FILE, 'rU') as a, open(WRITE_MEAN, 'w') as b, open(WRITE_CONDITIONAL, 'w') as c:
		fields, b_write, c_write = process_csv_readers(a, b, c)

		for row in fields:

			copy = row[:]
			for i in COL_ID:
				if len(row[i]) < 1:
					copy[i] = MEAN[i]
			b_write.writerow(copy)

			for i in COL_ID:
				if len(row[i]) < 1:
					# class = row[CLASS_ID]
					row[i] = COND_MEAN[i][row[CLASS_ID]]
			c_write.writerow(row)

if __name__ == "__main__":
	transform_means()