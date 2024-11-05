import pandas

data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
black_squirrel_data=len(data["Primary Fur Color"][data["Primary Fur Color"]=="Black"])
grey_squirrel_data=len(data["Primary Fur Color"][data["Primary Fur Color"]=="Gray"])
cinnamon_squirrel_data=len(data["Primary Fur Color"][data["Primary Fur Color"]=="Cinnamon"])

data_dict={
    'name':['Black','Gray','Red'],
    'count':[black_squirrel_data,grey_squirrel_data,cinnamon_squirrel_data]
}

DF=pandas.DataFrame(data_dict)
DF.to_csv('Report.csv')