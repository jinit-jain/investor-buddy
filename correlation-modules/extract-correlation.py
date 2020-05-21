import csv
import correlation as corr
import plot_map as plm
# csv file name 
# dit_path = 
DIR = 'csv/'
filename = "finalBetaDB.csv"
# filename = "correlation-matrix.csv"

# initializing the titles, symbols and rows list 
fields = [] 
rows = [] 
symbols = []

# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)

for row in rows:
    # if row[0][0] == 'B':
    #     break
    symbols.append(row[0] + '.NS')

df, xPoints = corr.correlation(symbols)
print(df)
plm.plot_map(xPoints)
df.to_csv('{}correlation-matrix.csv'.format(DIR))
