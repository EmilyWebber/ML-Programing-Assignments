import csv
import numpy as np
import matplotlib.pyplot as plt

READ_FILE = "mock_student_data.csv"
WRITE_TEXT = "Output/student_summaries.txt"
MISSING = ''
NUMERICAL = [7,6,5]
HISTOGRAM = [4,5,6,7,8]
CLASS_ID = 8

def get_initial_dicts(row):
	'''
	Takes a csv row, returns a two-way dictionary of headers
	And initialized counts dict with each header : {}
	'''
	maps = {}
	counts = {}
	for idx, field in enumerate(row):
		if idx > 0:
			counts[field] = {}
			maps[idx] = field
			maps[field] = idx
	return maps, counts

def read():
	'''
	Reads in the global csv file
	Returns four dictionaries:
		counts: {column : {instance: count, instance: count},
				column : {instance: cout, instance: count}}
		maps: {column: index, index: column}
		numerical: {Age: list, GPA: list, Days Missed: list}
		conditional: {Age: {"Yes": list, "No": list}, GPA: {"Yes": list, "No":list}
	'''
	numerical = {}
	conditional = {}

	with open(READ_FILE, 'rU') as f:
		fields = csv.reader(f)
		maps, counts = get_initial_dicts(next(fields))

		# count all the values, add to the dictionary
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

					if idx in NUMERICAL:
						try:
							i = int(val)
							if header not in numerical:
								numerical[header] = []
							numerical[header].append(i)

							if header not in conditional:
								conditional[header] = {}
							if row[CLASS_ID] not in conditional[header]:
								conditional[header][row[CLASS_ID]] = [i]
							else:
								conditional[header][row[CLASS_ID]].append(i)

						except:
							pass

	return counts, maps, numerical, conditional

def missing(each, counts, f):
	'''
	Takes a key, a dictionary, and a csv pointer object
	Writes the number of missing values to the csv
	'''
	if MISSING in counts[each]:
		f.write("\nMissing Values: {}".format(counts[each][MISSING]))
	else:
		f.write("\nMissing Values: 0")

def graph(header, inner_dict):
	'''
	Takes column header and inner dict of types and counts,
	Creates a histogram
	'''
	labels = []
	values = []
	for x, y in inner_dict.items():
		if x == MISSING:
			labels.append("Missing")
		else:
			labels.append(x)
		values.append(y)
	xs = np.arange(len(labels))
	x_ticks = xs + 0.4
	fig = plt.figure()
	plt.title("Histogram for {}".format(header))
	plt.xlabel("Possible Values")
	plt.ylabel("Number of each value")
	plt.xticks(x_ticks, labels)
	plt.bar(xs, values)
	fig.savefig("Output/Images/Histogram-{}.png".format(header))

def summary(counts, maps, numerical, conditional):
	with open(WRITE_TEXT, "w") as f:
		f.write("Summary Statistics For Mock Student Data")
		for each in list(counts.keys()):
			mode = 0
			mode_str = ""
			f.write("\n")
			f.write("\n{}".format(each))
			missing(each, counts, f)

			for val in counts[each]:
				if val == MISSING:
					pass
				else:
					c = counts[each][val]
					if c > mode:
						mode = c
						mode_str = val

			f.write("\nMode: {}, Count: {}".format(mode_str, mode))

			if maps[each] in NUMERICAL:
				f.write("\nMean: {}".format(np.mean(numerical[each])))
				f.write("\nMedian: {}".format(np.median(numerical[each])))
				f.write("\nStd Dev: {}".format(np.std(numerical[each])))
				f.write("\nConditional Graduated Mean: {}".format(np.mean(conditional[each]["Yes"])))
				f.write("\nConditional Did Not Graduate Mean: {}".format(np.mean(conditional[each]["No"])))

			if maps[each] in HISTOGRAM:
				graph(each, counts[each])

if __name__ == "__main__":
	counts, maps, numerical, conditional = read()
	summary(counts, maps, numerical, conditional)