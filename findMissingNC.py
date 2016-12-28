# Given a speaker ID number, this script counts how many sentences are missing from the set of 620 that Northwestern used and prints out their IDs
# Finds any extra sentences and prints their IDs
# Speaker ID format: NWF133, NWM055
# Sentence ID format: group_sentence (1-72; 1-10)
# Sentence IDs determined from a csv with the IDs

import os

speakerID = input("Speaker ID: ")
print("Missing files for", speakerID, ":")
count = 0
extracount = 0
sentIDs = []
fileIDs = []

sentences = open("/Users/Laura/Desktop/fall-2016/NIH/Stimuli/evanston/evanston1.csv", "r")
print("MISSING")
for line in sentences:
	line = line.split(',')
	sentID = line[0] + '_' + line[1]
	sentIDs.append(sentID)

for i in sentIDs:
	path = '/Users/Laura/Desktop/fall-2016/NIH/recordings-2016/{0}/{0}_seg/{0}_{1}.wav'.format(speakerID, i)
	if not os.path.exists(path):
		count += 1
		print(i)
print(count, "missing sentences")

# Make all the sentence IDs into filenames and put in a list
for sent in sentIDs:
	fileID = "{0}_{1}.wav".format(speakerID, sent)
	fileIDs.append(fileID)

# Walk through directory and find any filenames that aren't in the list of expected filenames
print("Extra files for", speakerID, ":")
for root, dirs, files in os.walk("/Users/Laura/Desktop/fall-2016/NIH/recordings-2016/{0}/{0}_seg".format(speakerID), topdown=False):
	for filename in files:
		if filename != ".DS_Store": # This file is always created and should be ignored
			filename = os.path.basename(filename)
			if filename not in fileIDs:
					extracount += 1
					print(filename)
print(extracount, "extra sentences")