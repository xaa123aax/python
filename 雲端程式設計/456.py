01 # -*- coding: utf-8 -*-
02 import csv
03 with open('csv.txt', 'r', encoding='utf-8') as fin:
04     with open('csv_out.txt', 'w', encoding='utf-8') as fout:
05         csvreader = csv.reader(fin, delimiter=',')
06         csvwriter = csv.writer(fout, delimiter=' ')
07         header = next(csvreader)
08         csvwriter.writerow(header)
09         for row in csvreader:
10             row[0] = row[0].replace('/', '-')
11             row[-1] += '%'
12             print(','.join(row))
13             csvwriter.writerow(row)
14 
