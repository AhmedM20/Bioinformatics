from Bio import AlignIO
from tempfile import TemporaryFile
from xlwt import Workbook
filename = "test.aln"
format = "clustal"
alignment = AlignIO.read(filename, format)
stars = alignment.column_annotations['clustal_consensus']
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def mergeAdjNum(l):
    r = [[l[0]]]
    for e in l[1:]:
        if r[-1][-1] == e - 1:
            r[-1].append(e)
        else:
            r.append([e])
    return r
def startEndOnly(l):
    tmp = []
    for x in l:
        if len(x) >=2:
            tmp.append([x[0],x[-1]])
        else:
            tmp.append(x)
    return tmp
conservedRegions = find(stars,'*')
unConservedRegions = find(stars,' ')
#for i in range(len(unConservedRegions)):
#    print(alignment.Seq[unConservedRegions[i]])
conservedRegions = startEndOnly(mergeAdjNum(conservedRegions))
unConservedRegions = startEndOnly(mergeAdjNum(unConservedRegions))
# print(len(stars))
#print(conservedRegions)
#print(unConservedRegions)

#create excel file to results of dissimilar regions
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
#write column names
sheet1.write(0,0,'similar regions:')
# caculate length of column
def get_width(num_characters):
    return int((1+num_characters) * 256)
row=1
ColWidth=0
#Get the dissimilar regions and write them to the excel file
for i in conservedRegions:
    if len(i) > 1:
        # print(i)
        sheet1.write(row,0,str(alignment[0].seq[i[0]:i[1]]))
        row+=1
        ColWidth=get_width(len(alignment[0].seq[i[0]:i[1]])) if ColWidth < get_width(len(alignment[0].seq[i[0]:i[1]])) else ColWidth
    else:
        sheet1.write(row,0,str(alignment[0].seq[i[0]]))
        ColWidth=get_width(len(alignment[0].seq[i[0]])) if ColWidth < get_width(len(alignment[0].seq[i[0]])) else ColWidth
        row+=1
#sheet1.col(0).width = ColWidth
#save excel file
#book.save('similar regions.xls')
#book.save(TemporaryFile())
print( conservedRegions)