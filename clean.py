import xlrd
import csv
import re

def write_csv():
	# Convert xls to a CSV
	wb = xlrd.open_workbook('data/safeway/report.xlsx')
	sh = wb.sheet_by_name('Denver')
	newcsv = open('data/safeway/report.csv', 'wb')
	wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)

	for rownum in xrange(sh.nrows):
	    wr.writerow(sh.row_values(rownum))
	newcsv.close()

def remove_top():
	# Get rid of the top blank lines
	with open('data/safeway/report.csv', 'r') as fin:
		data = fin.read().splitlines(True)
	with open('data/safeway/report.csv', 'w') as fout:
		fout.writelines(data[4:])
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


if __name__ == "__main__":
	write_csv()
	remove_top()
	remove_extras()
