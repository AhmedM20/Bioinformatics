import os
from Bio import SeqIO
from Bio import pairwise2
files=[]
count=0
for file in os.listdir(os.getcwd()):
    if file.endswith(".gb") or file.endswith(".fasta"):
        files.append(os.path.join(os.getcwd(), file))
        count+=1
if count >1:
    records=[]
    for file in files:
        if file.endswith(".fasta"):
            records.append(SeqIO.read(file, "fasta"))
        elif file.endswith(".gb"):
            records.append(SeqIO.read(file, "genbank"))
    alignments =pairwise2.align.globalxx(records[0].seq, records[1].seq)
    print ('Seq1 length: ' +  str(len(records[0].seq)))
    print ('Seq2 length: ' + str(len(records[1].seq)))
    print('Seq1 format: genebank:') if file.endswith(".gb") else print('Seq1 format: fasta'  )
    print('Seq2 format: genebank'  ) if file.endswith(".gb") else print('Seq2 format: fasta')

    if not alignments:

        print("Alignment not successfull")

    else:
        print("Alignment successfull")
else:
    print(" Input files not fasta or genbank format")