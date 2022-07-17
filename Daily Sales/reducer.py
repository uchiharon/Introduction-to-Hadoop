import csv
import sys


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    old_day = None
    
    sale = 1
    count = 1
    
    for line in reader:
        day = line[0]
        
        if day != old_day:
            avg_sale = sale/count
            writer.writerow([old_day, avg_sale])
            
            
            key = day

            sale = float(line[1])
            count = 1
            
            old_day = day
        else:
            sale += float(line[1])
            count += 1
    avg_sale = sale/count
    writer.writerow([old_day, avg_sale])



        
reducer()