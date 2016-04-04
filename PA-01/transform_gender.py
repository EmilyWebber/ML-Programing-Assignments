import csv
import requests
import json


READ_FILE = "mock_student_data.csv"
WRITE_GENDER = "Output/gender_transformed.csv"
KEY = "key.txt"

FIRST = 1
GENDER = 4

def get_key():
	'''
	Reads in my api key from a hidden file
	'''
	with open(KEY, "r") as f:
		key = f.readline()
	return key

# better to send the whole batch as a list, much faster that way
def get_gender(name):
	'''
	Takes a single name, returns the gender of the name
	'''
	key = "/?apikey=" + get_key()
	url = "name=" + name + key
	print (url)
	req = requests.get("http://api.genderize.io?" + url)
	j = json.loads(req.text)
	print (j)
	# return (json.loads(req.text)["gender"].title())

def transform_gender():
	'''
	Reads global csv file, grabs gender for missing values, writes to a new csv
	'''
	with open(READ_FILE, 'rU') as r, open(WRITE_GENDER, 'w') as g:
		fields = csv.reader(r)
		write = csv.writer(g)
		h = next(fields)
		write.writerow(h)
		count = 0
		for row in fields:
			if len(row[GENDER]) < 1:
				print ("found another missing gender")
				count += 1
				print ("Count is {}".format(count))
				# row[GENDER] = get_gender(row[FIRST])
			write.writerow(row)

if __name__ == "__main__":
	# transform_gender()
	get_gender("Shandra")
