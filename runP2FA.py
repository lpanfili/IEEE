import os
from subprocess import call

# Set directory that holds sound files
soundDir = '/home2/lpanfili/PNNC-test/NC/NCF011_seg'
# Set directory that holds transcripts
transDir = '/home2/lpanfili/PNNC-test/NC-transcripts'
# Set directory where text grids will go
textgDir = '/home2/lpanfili/PNNC-test/NC/NCF011_grids'

sounds = []

# for each sound file in the directory
for root, dirs, files in os.walk(soundDir):
	for f in files:
		# if it's a WAV (have to watch out for pesky hidden OS files)
		if os.path.splitext(f)[1] == '.wav':
			# add the full path of each .wav file to the list of sounds
			sounds.append(os.path.join(root,f))

for s in sounds:
	# the filename only without extension
	fn = os.path.splitext(os.path.split(s)[1])[0]
	# generate the corresponding textgrid and transcript paths
	tg = os.path.join(textgDir, fn+'.TextGrid')
	tr = os.path.join(transDir, fn[-5:]+'.txt') # fn[-5:] takes only the last 5 characters of the filename (the sentence number, not the speaker number)
	call(['python', '/opt/p2fa/align.py', s, tr, tg])
