import sys
import csv



def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
    box = []
    for line in reader:
            
        
        writer.writerow(line)

# This function allows you to test the mapper with the provided test string
def main():

    mapper()

main()