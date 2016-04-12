import csv
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

NO = "0"
YES = "1"

''' if you change the read file to the set that's already transformed,
switch global variable TRANSFORM to True
this saves the data quality pie chart saved in Output '''

# READ_FILE = "Output/conditional_transformed.csv"
READ_FILE = "Data/cs-training.csv"
TRANSFORM = False

WRITE_TEXT = "Output/Summary-Statistics.txt"
MISSING = 'NA'
NUMERICAL = [1,2,3,4,5,6,7,8,9,10,11]
CLASS_ID = 1
HISTOGRAM = [1]

def graph_data_quality(counts, conditional, maps):
	'''
	Takes two counting dictionaries and the maps dictionary,
	Graphs the target classifications against missing values
	To get some perspective on how much we're relying on the data being
	Not a mistake
	'''
	fig = plt.figure()
	d = counts[maps[CLASS_ID]]
	fracs = [d[YES], d[NO]]
	labels = [YES, NO]

	for each in list(counts.keys()):
		if MISSING in counts[each]:
			fracs.append(counts[each][MISSING])
			labels.append(each)

	plt.pie(fracs, labels=labels)
	plt.title("Comparision of target counts to missing values \n Or Data Quality")
	if not TRANSFORM:
		fig.savefig("Output/Images/DataQuality.png")

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

		# count all the values, add to the dictionaries
		for row in fields:
			for idx, val in enumerate(row):

				# skip the index row
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
							i = float(val)
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

def graph_distribution():
	return

def graph_hist(header, inner_dict):
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
		f.write("Summary Statistics")
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
				write_logic(f, numerical, conditional, each)
			graph_distribution()

			if maps[each] in HISTOGRAM:
				graph_hist(each, counts[each])

		find_correlations(numerical, f)
		graph_data_quality(counts, conditional, maps)

# also want to add conditional missing values
def write_logic(f, numerical, conditional, each):
	'''
	Takes file pointer object, two dictionaries, and a key,
	Writes to file f based on the key
	'''
	f.write("\nMin: {}".format(min(numerical[each])))
	f.write("\nMax: {}".format(max(numerical[each])))
	f.write("\nMean: {}".format(np.mean(numerical[each])))
	f.write("\nMedian: {}".format(np.median(numerical[each])))
	f.write("\nStd Dev: {}".format(np.std(numerical[each])))
	f.write("\nConditional No Mean: {}".format(np.mean(conditional[each][NO])))
	f.write("\nCond. Yes Mean: {}".format(np.mean(conditional[each][YES])))
	f.write("\nCond. No Min: {}".format(min(conditional[each][NO])))
	f.write("\nCond. Yes Min: {}".format(min(conditional[each][YES])))
	f.write("\nCond. No Max :{}".format(max(conditional[each][NO])))
	f.write("\nCond. Yes Max :{}".format(max(conditional[each][YES])))

# graph correlation matrix here
# want to also get t-values here for each bivariate correlation
# then do multivariate correlations of each against all the others, plus t_values
def find_correlations(numerical, f):
	'''
	Takes dict of numerical values and pointer to write file
	Writes correlations of each variable against the other
	'''
	f.write("\n")
	f.write("\nCross-Variable Correlations")
	for each in list(numerical.keys()):
		f.write("\n")
		f.write("\n   {}".format(each))
		for k in list(numerical.keys()):
			if (k != each):
				try:
					beta = np.corrcoef(numerical[each], numerical[k])[1][0]
					f.write("\n     - {}: {}".format(k, beta))
				except:
					pass

if __name__ == "__main__":
	counts, maps, numerical, conditional = read()
	summary(counts, maps, numerical, conditional)