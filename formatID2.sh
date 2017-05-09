# add a zero before any single digits in the sent ID
# Change final _ to -
# Change NW to PN

#!/bin/bash


for f in $(find /projects/pnnc_harvard_sentences/PNNC2 -name '*.wav')
    do
        # Replace NW with PN
        if echo "$f" | grep 'NW'; then
          mv "$f" "${f//NW/PN}"
        fi
        # If group ID is single digit, add 0
        if echo "$f" | grep '.*_[1-9]_.*'; then
          mv "$f" "$(echo "$f" | sed -e 's/\(.*_\)\([1-9]\)\(_.*\)/\10\2\3/g')"
        fi
        # If sent num is a single digit, add 0
        if echo "$f" | grep '.*_[1-9]\.wav'; then
          mv "$f" "$(echo "$f" | sed -e 's/\(.*_[0-9][0-9]_\)\([0-9]\)\(\.wav\)/\10\2\3/g')"
        fi
        # Replace final _ with -
        if echo "$f" | grep '\(.*[0-9][0-9]\)_\([0-9][0-9].*\)'; then
          mv "$f" "$(echo "$f" | sed -e 's/\(.*_[0-9][0-9]\)_\([0-9][0-9]\.wav\)/\1-\2/g')"
        fi
    done