# GC
workup GC data

this script extracts sample name, data result, date, time, and sample notes
notes (in our case, sample pressure) from the Agilent GC6890 used by the GEM lab
for permanent gas analysis.  Input is a directory containing *.D folders.  Each
directory should have a report.txt file, and if necessary, a report00.csv containing 
sample pressure in the sample info field.  This python file should be placed in the directory
containing the *.D folders
