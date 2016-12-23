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

print("EXTRA")
# Find any extra sentences
for root, dirs, files in os.walk("/Users/Laura/Desktop/fall-2016/NIH/recordings-2016/{0}/{0}_seg".format(speakerID), topdown=False):
	for filename in files:
		if filename != ".DS_Store":
			filename = filename.split("_")
			group = filename[1]
			sent = filename[2]
			sent = sent.split(".")
			sent = sent[0]
			sentID = group + "_" + sent
			if not sentID in sentIDs:
				extracount += 1
				print(sentID)
print(extracount, "extra sentences")