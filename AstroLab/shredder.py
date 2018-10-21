import csv
reader = csv.reader(open("initial_results.txt", 'w+'), delimiter="\t")
filename = "initial_results.txt"

f = open(filename, 'r+')
try:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
finally:
    f.close()