from Bio.SeqUtils import seq3
from Bio import SeqIO
print(seq3(SeqIO.read("sequence.fasta", "fasta")))
