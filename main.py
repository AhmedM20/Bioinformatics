from Bio import SeqIO
from Bio.Seq import Seq
#import pandas as pd
from tempfile import TemporaryFile
from xlwt import Workbook
import csv
import numpy as np
from collections import defaultdict
from Bio.SeqUtils import GC
from Bio.SeqRecord import SeqRecord
from Bio import Align
from Bio.Align import AlignInfo
referenceSequences = SeqIO.parse("cov.fasta", "fasta")
caseSequences = SeqIO.parse("omicron.fasta", "fasta")


referenceSequencesList =  []
caseSequencesList = []


for referenceSequence in referenceSequences:
    referenceSequencesList.append(referenceSequence)
for caseSequence in caseSequences:
    caseSequencesList.append(caseSequence)


book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
sheet1.write(1,0,'Name')
sheet1.write(1,1,'Sequence')
sheet1.write(1,2,'Length')
sheet1.write(1,3,'A Content')
sheet1.write(1,4,'C Content')
sheet1.write(1,5,'G Content')
sheet1.write(1,6,'T Content')
sheet1.write(1,7,'CG Content')
sheet1.write_merge(0, 0, 0, 7, 'Reference sequences')
sheet1.write_merge(12, 12, 0, 2, 'Average percentage of the chemical constituents:')
def get_width(num_characters):
    return int((1+num_characters) * 256)
nameColWidth=0
sheet1.write(14,0,'Name')
sheet1.write(14,1,'Sequence')
sheet1.write(14,2,'Length')
sheet1.write(14,3,'A Content')
sheet1.write(14,4,'C Content')
sheet1.write(14,5,'G Content')
sheet1.write(14,6,'T Content')
sheet1.write(14,7,'CG Content')
sheet1.write_merge(13, 13, 0, 7, 'Case sequences')
sheet1.write_merge(25, 25, 0, 2, 'Average percentage of the chemical constituents:')
sumRefA=0
sumRefC=0
sumRefG=0
sumRefT=0
sumRefGC=0
sumCaseGC=0
sumCaseA=0
sumCaseC=0
sumCaseG=0
sumCaseT=0
referenceSequencesListOfObjects =  []
caseSequencesListOfObjects = []
for i in range(len(referenceSequencesList)):
    referenceSequenceLength = len(referenceSequencesList[i])
    referenceSequenceObject = defaultdict()
    referenceSequenceObject['length'] = referenceSequenceLength
    referenceSequenceObject['name'] = referenceSequencesList[i].name
    referenceSequenceObject['sequence'] = referenceSequencesList[i].seq
    referenceSequenceObject['A'] = referenceSequenceObject['sequence'].count("A") / referenceSequenceLength*100
    referenceSequenceObject['C'] = referenceSequenceObject['sequence'].count("C") / referenceSequenceLength*100
    referenceSequenceObject['G'] = referenceSequenceObject['sequence'].count("G") / referenceSequenceLength*100
    referenceSequenceObject['T'] = referenceSequenceObject['sequence'].count("T") / referenceSequenceLength*100
    referenceSequenceObject['GC'] = GC(referenceSequenceObject['sequence'])
    referenceSequencesListOfObjects.append(referenceSequenceObject)
    sheet1.write(i+2,0,referenceSequencesListOfObjects[i]['name'])
    sheet1.write(i+2,1,str(referenceSequencesListOfObjects[i]['sequence']))
    sheet1.write(i+2,2,referenceSequencesListOfObjects[i]['length'])
    sheet1.write(i+2,3,referenceSequencesListOfObjects[i]['A'])
    sheet1.write(i+2,4,referenceSequencesListOfObjects[i]['C'])
    sheet1.write(i+2,5,referenceSequencesListOfObjects[i]['G'])
    sheet1.write(i+2,6,referenceSequencesListOfObjects[i]['T'])
    sheet1.write(i+2,7,referenceSequencesListOfObjects[i]['GC'])
    nameColWidth=get_width(len(referenceSequencesListOfObjects[i]['name'])) if nameColWidth < get_width(len(referenceSequencesListOfObjects[i]['name'])) else nameColWidth
    sumRefGC=sumRefGC+referenceSequencesListOfObjects[i]['GC']
    sumRefA+=referenceSequencesListOfObjects[i]['A']
    sumRefC+=referenceSequencesListOfObjects[i]['C']
    sumRefG+=referenceSequencesListOfObjects[i]['G']
    sumRefT+=referenceSequencesListOfObjects[i]['T']

    caseSequenceObject = defaultdict()
    caseSequenceLength = len(caseSequencesList[i])
    caseSequenceObject['length'] = caseSequenceLength
    caseSequenceObject['name'] = caseSequencesList[i].name
    caseSequenceObject['sequence'] = caseSequencesList[i].seq
    caseSequenceObject['A'] = caseSequenceObject['sequence'].count("A") / caseSequenceLength*100
    caseSequenceObject['C'] = caseSequenceObject['sequence'].count("C") / caseSequenceLength*100
    caseSequenceObject['G'] = caseSequenceObject['sequence'].count("G") / caseSequenceLength*100
    caseSequenceObject['T'] = caseSequenceObject['sequence'].count("T") / caseSequenceLength*100
    caseSequenceObject['GC'] = GC(caseSequenceObject['sequence'])
    caseSequencesListOfObjects.append(caseSequenceObject)
    sheet1.write(i+15,0,caseSequencesListOfObjects[i]['name'])
    sheet1.write(i+15,1,str(caseSequencesListOfObjects[i]['sequence']))
    sheet1.write(i+15,2,caseSequencesListOfObjects[i]['length'])
    sheet1.write(i+15,3,caseSequencesListOfObjects[i]['A'])
    sheet1.write(i+15,4,caseSequencesListOfObjects[i]['C'])
    sheet1.write(i+15,5,caseSequencesListOfObjects[i]['G'])
    sheet1.write(i+15,6,caseSequencesListOfObjects[i]['T'])
    sheet1.write(i+15,7,caseSequencesListOfObjects[i]['GC'])
    nameColWidth=get_width(len(caseSequencesListOfObjects[i]['name'])) if nameColWidth < get_width(len(caseSequencesListOfObjects[i]['name'])) else nameColWidth
    sumCaseGC=sumCaseGC+caseSequencesListOfObjects[i]['GC']
    sumCaseA+=caseSequencesListOfObjects[i]['A']
    sumCaseC+=caseSequencesListOfObjects[i]['C']
    sumCaseG+=caseSequencesListOfObjects[i]['G']
    sumCaseT+=caseSequencesListOfObjects[i]['T']
sheet1.write(12,7,sumRefGC/10)
sheet1.write(12,6,sumRefT/10)
sheet1.write(12,5,sumRefG/10)
sheet1.write(12,4,sumRefC/10)
sheet1.write(12,3,sumRefA/10)
sheet1.write(25,7,sumCaseGC/10)
sheet1.write(25,6,sumCaseT/10)
sheet1.write(25,5,sumCaseG/10)
sheet1.write(25,4,sumCaseC/10)
sheet1.write(25,3,sumCaseA/10)
sheet1.col(0).width = nameColWidth
book.save('Chemical constituents.xls')
book.save(TemporaryFile())

longestCaseSequenceLength = 0
for caseSequence in caseSequencesListOfObjects:
    longestCaseSequenceLength = max(caseSequence['length'],longestCaseSequenceLength)

longestReferenceSequenceLength = 0
for referenceSequence in referenceSequencesListOfObjects:
    longestReferenceSequenceLength = max(referenceSequence['length'],longestReferenceSequenceLength)

## MSA Preparation
## Right padding with Gaps for MSA.
referenceListMultipleSequenceAlignment = []
caseListMultipleSequenceAlignment = []


i = 0
while i <= 9:
    referenceListMultipleSequenceAlignment.append(SeqRecord(Seq(str(referenceSequencesListOfObjects[i]['sequence']).ljust(longestReferenceSequenceLength, '-')),annotations={"molecule_type": "DNA"}))
    caseListMultipleSequenceAlignment.append(SeqRecord(Seq(str(caseSequencesListOfObjects[i]['sequence']).ljust(longestCaseSequenceLength, '-')),annotations={"molecule_type": "DNA"}))
    i+=1
###########################################
#print(longestReferenceSequenceLength)
alignment = Align.MultipleSeqAlignment(referenceListMultipleSequenceAlignment)
summary_align = AlignInfo.SummaryInfo(alignment)
consensus_seq=summary_align.dumb_consensus(0.7)

#print(consensus_seq)
#print(len(caseListMultipleSequenceAlignment[0].seq))
#print(len(consensus_seq))
#print("////////////////////////////////////////////////")
dissimillar_indices=[]
dissimillar_elements_case=[]
dissimillar_elements_consensus=[]

#for i in caseListMultipleSequenceAlignment:
 #print( len(i.seq))


for i in range (0,len(caseListMultipleSequenceAlignment)):
  CaseSeqMultipleAlignment= caseListMultipleSequenceAlignment[i].seq
  
  maprange=[]
  start=[]
  for j in range(len( CaseSeqMultipleAlignment)):
    
      if not consensus_seq[j]:
          dissimillar_indices.append(j)
          dissimillar_elements_case.append(CaseSeqMultipleAlignment[i])
          dissimillar_elements_consensus.append("-")

      elif not CaseSeqMultipleAlignment[j]:
          dissimillar_indices.append(j)
          dissimillar_elements_case.append("-")
          dissimillar_elements_consensus.append(consensus_seq[j])
       

      elif CaseSeqMultipleAlignment[j] != consensus_seq[j]:
          dissimillar_indices.append(j)
          dissimillar_elements_case.append(CaseSeqMultipleAlignment[j])
          dissimillar_elements_consensus.append(consensus_seq[j])
          
          
      

          
          

          #dissimillar_indices.append(j)
          #dissimillar_elements_case.append(CaseSeqMultipleAlignment[j])
          #dissimillar_elements_consensus.append(consensus_seq[j])

#print(dissimillar_indices)




