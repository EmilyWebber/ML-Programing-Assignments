import csv

READ_FILE = "mock_student_data.csv"
WRITE_TEXT = "student_summaries.txt"
WRITE_CSV = "transformed_student_data.csv"
MISSING = ''

def read():
	'''
	Takes a csv filename and returns a list of lists of rows in the csv,
	Along with dictionary of each header as a key and an inner dictionary
	As a value
	'''
	counts = {}
	maps = {}
	with open(READ_FILE, 'rU') as f:
		fields = csv.reader(f)
		headers = next(fields)
		for idx, field in enumerate(headers):
			if idx > 0:
				counts[field] = {}
				maps[idx] = field

		for row in fields:
			for idx, val in enumerate(row):
				if idx == 0:
					pass
				else:
					header = maps[idx]
					if val not in counts[header]:
						counts[header][val] = 1
					else:
						counts[header][val] += 1
	return counts

def missing(each, counts, f):
	if MISSING in counts[each]:
		f.write("Missing Values : {}".format(counts[each][MISSING]))
	else:
		f.write("Missing Values : 0")


def summary(counts):
	with open(WRITE_TEXT, "w") as f:
		f.write("Summary Statistics For Mock Student Data")
		for each in list(counts.keys()):
			f.write("\n")
			f.write("\n")
			f.write(each)
			f.write("\n")
			missing(each, counts, f)
			for val in list(counts[each].keys()):
				print (counts[each][val])

# mean
# median
# mode
# standard deviation
# number of missing values



if __name__ == "__main__":
	summary(read())