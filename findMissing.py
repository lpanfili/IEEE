# Given a speaker ID number, this script counts how many sentences are missing from the set of 720 and outputs their IDs
# Speaker ID format: NWF133, NWM055
# Sentence ID format: group_sentence (1-72; 1-10)

import os

speakerID = input("Speaker ID: ")
print("Missing files for", speakerID, ":")
count = 0
extracount = 0
sentIDs = []
fileIDs = []

for i in range(1, 73):
	for j in range (1, 11):
		sentID = '{0}_{1}'.format(i, j)
		sentIDs.append(sentID)	
		path = '/Users/Laura/Desktop/fall-2016/NIH/recordings-2016/{0}/{0}_seg/{0}_{1}_{2}.wav'.format(speakerID, i, j)
		if not os.path.exists(path):
			count += 1
			print(sentID)
print(count, "missing sentences")

for sent in sentIDs:
	fileID = "{0}_{1}.wav".format(speakerID, sent)
	fileIDs.append(fileID)

print("Extra files for", speakerID, ":")
for root, dirs, files in os.walk("/Users/Laura/Desktop/fall-2016/NIH/recordings-2016/{0}/{0}_seg".format(speakerID), topdown=False):
	for filename in files:
		if filename != ".DS_Store":
			filename = os.path.basename(filename)
			if filename not in fileIDs:
					extracount += 1
					print(filename)
print(extracount, "extra sentences")
