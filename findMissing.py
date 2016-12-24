# Given a speaker ID number
# Counts how many sentences are missing from the set of 720 and outputs their IDs
# Counts how many sentences are extra (unexpected) from the set of 720 and outputs their IDs
# Speaker ID format: NWF133, NWM055
# Sentence ID format: group_sentence (1-72; 1-10)

import os

# User enters speaker ID
speakerID = input("Speaker ID: ")
print("Missing files for", speakerID, ":")

count = 0 # number of missing sentences
extracount = 0 # number of extra sentences
sentIDs = [] # list of sentence IDs
fileIDs = [] # list of file IDs (same as sentIDs but with speaker ID and .wav)

# Make all of the combinations of 1-72 and 1-10 and find if that exists as a file
for i in range(1, 73):
	for j in range (1, 11):
		sentID = '{0}_{1}'.format(i, j)
		sentIDs.append(sentID)	
		path = '/Users/Laura/Desktop/fall-2016/NIH/recordings-2016/{0}/{0}_seg/{0}_{1}_{2}.wav'.format(speakerID, i, j)
		if not os.path.exists(path):
			count += 1
			print(sentID)
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
