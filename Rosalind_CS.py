#!usr/bin/python
import re
import array
import math

myfile = open("rosalind_lcsm.txt", "r")
seqs=myfile.read().replace('\n', '')

seqs = seqs.split(">")
seqs.pop(0)
#print (seqs[1])
#print (type(seqs))
for seq in seqs: 
	seq = re.sub("^Rosalind_", "", seq)
	seq = re.sub("^[0-9]{4}", "", seq)
	#print(seq)
#print (seqs)

def longest_common_substring(seqs):
    # Find the length of the shortest sequence
    min_len = min(len(s) for s in seqs)

    # Initialize the result to be an empty string
    result = ""

    # Iterate over all possible substrings of the shortest sequence
    for i in range(min_len):
        for j in range(i + 1, min_len + 1):
            # Check if all sequences contain the current substring
            substring = seqs[0][i:j]
            if all(substring in seq for seq in seqs):
                # Update the result if the current substring is longer than the previous result
                if len(substring) > len(result):
                    result = substring
    return result

print(longest_common_substring(seqs))




