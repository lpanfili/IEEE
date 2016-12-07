# Add a second zero in the spekeaker ID in each filename
# NWF02 --> NWF002

for file in `ls /Users/Laura/Desktop/test/*`
do
	name=$(basename "$file")
	if echo "$name" | grep 'F'; then
		mv "$file" "${file//NWF0/NWF00}"
	fi
	if echo "$name" | grep 'M'; then
		mv "$file" "${file//NWM0/NWM00}"
	fi
done
