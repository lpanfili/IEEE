# Add a zero before any single digits in the sent ID
# Change final _ to -
# Change NW to PN

#!/bin/bash

path=/Users/Laura/Desktop/recordings-2016

# Rename each speaker's main dir
for dir in `ls /Users/Laura/Desktop/recordings-2016`
	do
		#echo "$dir"
		if echo "$dir" | grep 'NW'; then
			fp="$path"/"$dir"
			#echo "$fp"
			#echo "${fp//NW/PN}"
			mv "$fp" "${fp//NW/PN}"
		fi
	done


# Rename each speaker's _seg dir
for dir in `ls /Users/Laura/Desktop/recordings-2016/`
	do
		for subdir in `ls /Users/Laura/Desktop/recordings-2016/$dir`
			do
				if echo "$subdir" | grep 'NW'; then
					fp="$path"/"$dir"/"$subdir"
					mv "$fp" "${fp//NW/PN}"
				fi
			done
	done

for f in $(find /Users/Laura/Desktop/recordings-2016 -name '*.wav')
	do
		# Replace NW with PN
		if echo "$f" | grep 'NW'; then
			mv "$f" "${f//NW/PN}"
		fi
		# If group ID is single digit, add 0
		mv "$f" $(echo "$f" | sed -E 's/(.*_)([0-9])(_.*)/\10\2\3/g')
		# If sent num is a single digit, add 0
		mv "$f" $(echo "$f" | sed -E 's/(.*_[0-9][0-9]_)([0-9])(\.wav)/\10\2\3/g')
		# Replace final _ with -
		mv "$f" $(echo "$f" | sed -E 's/(.*_[0-9][0-9])_([0-9][0-9]\.wav)/\1-\2/g')
	done







