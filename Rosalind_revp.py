#!usr/bin/python
import re
import array
import math
##this python script is solution to rosalind problem #GC_cont

myfile = open("rosalind_revp.txt", "r")
dna=myfile.read().replace('\n', '')
#dna=myfile.read()
#print (dna)

data = "TCAATGCATGCGGGTCTATATGCAT"
seqs = dna.split(">")
#seqs = seqs.split("\n")
#print (seqs)

seqs.pop(0)

#print (seqs)

#re.match('Rosalind_[0-9]{4}', seqs
#seqs.replace('Rosalind_[0-9]{4}', '')
#seqs.remove("Rosalind_[0-9]{4}")

# regex = re.compile(Rosalind_[0-9]{4})
# filtered = [i for i in seqs if not regex.match(i)]
# print(filtered)
# print(seqs)

def reverse_palindrome(data):
    palindromes = []

    for i in range(len(data) - 3):
        for j in range(4, 13):
            if i + j > len(data):
                break
            substring = data[i:i+j]
            if substring == substring[::-1]:
                palindromes.append((i+1, j))

    return palindromes
    #print (palindromes)