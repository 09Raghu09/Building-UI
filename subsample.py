import sys,random
from Bio import SeqIO

num = int(sys.argv[2])

outArray = [record for record in SeqIO.parse(open(sys.argv[1],'r'),'fasta') if random.randint(0,1)]
while len(outArray)!= num:
    newArray = []
    for record in outArray:
        if len(newArray) == num:
            break
        if random.randint(0,1):
            newArray.append(record)
    outArray = newArray

for record in outArray:
    print (">" + record.id)
    print (record.seq)