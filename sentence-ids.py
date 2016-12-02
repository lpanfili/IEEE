# Makes a dictionary of sentences (keys) and IDs (values)
# Given a text file, finds the ID of each sentence
# Outputs a new CSV with the sentences and IDs in the order of the original text file

import csv

ids = {}
cleaned = open("evanston5.csv", "w")

# This is the file that already contains sentence IDs
master = open("/Users/laurapanfili/Desktop/fall-2016/NIH/Stimuli/csv/order1.csv", "r")
for line in master:
	line = line.split(',')
	# Super hacky to get around sentences that have commas in them
	if len(line) > 4:
		line = [line[0], line[1], ','.join(line[2:-1]), line[-1]]
	sentID = line[0] + ',' + line[1]
	sent = line[2].strip("\"")
	ids[sent] = sentID

# This is the file that's missing sentence IDs
fix = open("/Users/laurapanfili/Desktop/fall-2016/NIH/Stimuli/northwestern/Evanston_order5.txt", "r")
for line in fix:
	line = line.strip()
	if line != "" and line != "PAUSE":
		newid = ids[line]
		newLine = newid + "," + line
		cleaned.write(newLine)
		cleaned.write("\n")
