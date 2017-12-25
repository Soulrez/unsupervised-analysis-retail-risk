import xlrd
import csv
import re

def write_csv():
	# Convert xls to a CSV
	wb = xlrd.open_workbook('data/safeway/report.xlsx')
	newcsv = open('data/safeway/report.csv', 'wb')

	# Names of the sheets to process in workbook
	sheets = ['Denver','Eastern','Houston','Intermountain','Norcal','Portland','Seattle','SoCal','Southern','Southwest']
	for sheet in sheets:	
		sh = wb.sheet_by_name(sheet)
		wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)
		for rownum in xrange(sh.nrows):
			wr.writerow(sh.row_values(rownum,start_colx=3))
	newcsv.close()

def remove_top():
	# Get rid of the top blank lines
	with open('data/safeway/report.csv', 'r') as fin:
		data = fin.read().splitlines(True)
	with open('data/safeway/report.csv', 'w') as fout:
		# Multiple sheets all have top blank lines/headings
		fout.writelines(data[4:104]) #6168
		fout.writelines(data[108:207]) #7984
		fout.writelines(data[212:311]) #6216
		fout.writelines(data[316:415]) #8853
		fout.writelines(data[420:519]) #6748
		fout.writelines(data[524:623]) 
		fout.writelines(data[628:727]) 
		fout.writelines(data[732:831])
		fout.writelines(data[836:935])
		fout.writelines(data[940:1039])   
	fin.close()
	fout.close()

def remove_extras():
	# Get rid of blanks in the middle from poor formatting
	with open('data/safeway/report.csv', 'r') as fin:
		data = fin.read()
		# Remove blank columns
		data = re.sub(r',"",', ',',data)
		# Remove "" so it can be formatted as float
		data = re.sub('"','',data)

	with open('data/safeway/report.csv', 'w') as fout:
		fout.write(data)

'''
Obsolete
'''
def remove_ids():
	# Removes Store ID, Clerk ID, and Risk Factor
	data = ''
	with open('data/safeway/report.csv', 'r') as fin:
		for line in fin:
			line = line.split(',')
			for i in range(3, len(line)):
				data += str(line[i])
				if not i == (len(line)-1):
					data += ','
			#data += '\r\n'
	with open('data/safeway/report.csv', 'w') as fout:
		fout.write(data)

if __name__ == "__main__":
	write_csv()
	remove_top()
	remove_extras()
