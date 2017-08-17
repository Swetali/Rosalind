#!usr/bin/python
import re
import array
##this python script is solution to rosalind problem #GC

#open and read file in a variable
with open('rosalind_gc_3.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    #print (data)
   
    #split to each seq 
    seqs = data.split(">")
    #print (seqs[2])
    
    percent_gc = []
    id = []
    #remove first empty element 
    seqs.pop(0)
    
    #for loop to go through each sequence 
    for seq in seqs:
            #Couting GC content
            a = seq.count('A')
            t = seq.count('T')
            g = seq.count('G')
            c = seq.count('C')
            
            #calculate for the % of GC
            length = (a + t + g + c)
            gc_add = (g + c)
            frac_gc = gc_add/length
            percent_gc.append(frac_gc*100)
            #print (percent_gc)
            
            #in the array find the highest GC %
            high =  max(percent_gc)
            
            #find the index of the highest GC %
            pos = percent_gc.index(high)
            #print (pos)
            #gc = []
            #gc.append(percent_gc)
            #print (gc)
            
            #regex to grab id
            #id = array()
            id.append(re.match('Rosalind_[0-9]{4}', seq))
            #if id:
#print id with corresponsing highest gc count
print (id[pos].group(0))
print (high)
    
    