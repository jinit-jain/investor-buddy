
import pandas as pd

df = pd.read_csv("C://Users//Hrishikesh//Desktop//Github//InvestorBuddy//investor-buddy-frontend//data//finalBetaDB.csv")
listFile = open("C://Users//Hrishikesh//Desktop//Github//InvestorBuddy//investor-buddy-frontend//companyList.txt","w+")
companyList = []

for i in df.index:
    name = df['Symbol'][i]
    name += " - " + df['Company'][i]
    listFile.writelines("'"+name+"',\n")


