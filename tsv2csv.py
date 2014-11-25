import sys
import csv
 
with open("combinedscl.txt.tsv", 'rb') as tsv:
	spamreader = csv.reader(tsv, dialect=csv.excel_tab)
	for r in spamreader:
		print ', '.join(r)
 

