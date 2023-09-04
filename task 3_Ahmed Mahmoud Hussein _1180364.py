from Bio import SeqIO
from Bio.SeqUtils import GC
SeqIO.convert("sequence.gb", "genbank", "sequence.fasta", "fasta")
GCPercentage=GC(SeqIO.read("sequence.fasta", "fasta").seq)
ATPercentage=100-GCPercentage
print('GC% ' + str(GCPercentage))
print('AT% ' + str(ATPercentage))
print('Stable') if GCPercentage>40 and GCPercentage<80 else print('Unstable')