import csv
import time


if __name__ == '__main__':
    with open('infile.csv') as csv_infile:
        with open('outfile.csv', 'a') as csv_outfile:
            reader = csv.reader(csv_infile)
            writer = csv.writer(csv_outfile, lineterminator='\n')
            for row in reader:
                if ("AM" in row[0]) or ("PM" in row[0]):
                    row[0] = time.strftime("%d/%m/%Y %H:%M:%S", time.strptime(row[0], "%m/%d/%Y %I:%M:%S %p"))
                else:
                    try:
                        row[0] = time.strftime("%d/%m/%Y %H:%M:%S", time.strptime(row[0], "%m/%d/%Y %H:%M"))
                    except:
                        print("not a date")
                writer.writerow(row)


