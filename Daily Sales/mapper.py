import csv
import sys
from datetime import datetime



def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    for line in reader:
        
        
        date,time,name,item,amount,payment = line
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        
        writer.writerow([weekday,amount])
        
            


mapper()