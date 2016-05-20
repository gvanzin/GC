'''this script extracts sample name, data result, date, time, and sample notes
notes (in our case, sample pressure) from the Agilent GC6890 used by the GEM lab
for permanent gas analysis.  Input is a directory containing *.D folders.  Each
directory should have a report.txt file, and a report00.csv containing 
sample pressure in the sample info field.  If sample pressure is not in the 
sample info field this script won't run.  This python file should be placed in the directory
containing the *.D folders. '''

import pandas as pd
import os
sample_result_date_time_pressure=[]
pat=[]
for root, dir, files in os.walk('.'):
    pat.append(root)

pat.pop(0)
for i in pat:
	os.chdir(i)
	date_line=[]
	result_line=[]
	sample_line=[]
	pressure_line=[]
	with open('Report.TXT','r') as inF:
		for line in inF:
			if 'BP' in line:
				result_line.append(line)
			if 'BB' in line:
				result_line.append(line)
			if 'PP' in line:
				result_line.append('999 999 999 999 999')
			if 'No peaks found' in line:
				result_line.append('999 999 999 999 999')
			if 'Calibrated compound(s) not found' in line:
				result_line.append('999 999 999 999 999')
			if 'Data File' in line:
				sample_line.append(line)
			if 'GC6890' in line:
				date_line.append(line)
	
	result_line_split=[i.split() for i in result_line]
	if result_line_split[0][2]=='S':
		del(result_line_split[0][2])
	result=result_line_split[0][4]

	date_line_split=[i.split() for i in date_line]
	date=date_line_split[0][1]
	time=date_line_split[0][2]

	sample_line_split=[i.split() for i in sample_line]
	sample=sample_line_split[0][5]

	with open('REPORT00.CSV','r') as inF:
		for line in inF:
			if 'Sample Info' in line:
				pressure_line.append(line)
			elif 'Calibration Table' in line:
				pressure_line.append('999,999,999')
	psl=[i.strip('\r\n') for i in pressure_line]
	pressure_line_split=[i.split(',') for i in psl]
	pressure=pressure_line_split[0][1][1:]

	sample_result_date_time_pressure.append([sample,result,date,time,pressure])
	os.chdir("..")


df=pd.DataFrame(sample_result_date_time_pressure)
df.columns=['sample','% CH4','Date','Time','Pressure']
df.to_csv('final_merged.csv',index=False)