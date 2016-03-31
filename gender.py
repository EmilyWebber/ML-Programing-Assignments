# do this yourself, don't use his

# Based on the file written by Brian Smith
# https://github.com/block8437/gender.py/blob/master/gender.py

# Have to use with a list of names

import requests, json

def getGenders(names):
	url = ""
	cnt = 0
	for name in names:
		if url == "":
			url = "name[0]=" + name
		else:
			cnt += 1
			url = url + "&name[" + str(cnt) + "]=" + name

	req = requests.get("http://api.genderize.io?" + url)
	results = json.loads(req.text)

	retrn = []
	for result in results:
		if result["gender"] is not None:
			retrn.append(result["gender"])
			# retrn.append((result["gender"], result["probability"], result["count"]))
		else:
			retrn.append((u'None',u'0.0',0.0))
	return retrn

if __name__ == '__main__':
	print getGenders(["Betty", "Emily"])