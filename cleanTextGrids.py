# Converts TextGrid annotations from the format [NCF03_43-02] to 43_2 (Northwestern to UW convention)
# Outputs a new TextGrid
# IF THIS DOESN'T WORK ON A SPCIFIC FILE:
# Check the encoding of the file. Change it to UTF-8.
# Praat can be cranky. http://www.fon.hum.uva.nl/praat/manual/Unicode.html

import re
import os

for root, dirs, files in os.walk("/Users/Laura/Desktop/nw-grids/", topdown=False):
	for name in files:
		if name != '.DS_Store':
			filename = name[:-9]
			fn = open('/Users/Laura/Desktop/nw-grids_clean/{0}_rough.TextGrid'.format(filename),'w+', encoding = 'latin1')
			with open('/Users/Laura/Desktop/nw-grids/{0}'.format(name), 'r', encoding = 'latin1') as f:
				text = f.readlines()
				for line in text:
					line = re.sub(r'\[NC[MF]\d\d_(\d+)-0?(\d+)\]', r'\1_\2', line)
					fn.write(line)