#TRADITIONAL METHOD
#READING CSV FILE 
# with open("C:\\Users\\Preksha Asati\\PY\\Day25\\weather.csv") as data :
#            list_weather= data.readlines()
# print(list_weather)

#if we just use csv import it takes too much effort to just get a column from the data
# import csv
# with open("C:\\Users\\Preksha Asati\\PY\\Day25\\weather.csv") as data :
#            data_file = csv.reader(data)
#            tempratures = []
#            for row in data_file :
#                    if row[1]!='temp':
   
#                      tempratures.append(int(row[1]))
#            print(tempratures)

#INSTALLING PANDAS 
          
#pip install pandas

import pandas as pd
data = pd.read_csv("C:\\Users\\Preksha Asati\\PY\\Day25\\weather.csv")
print(data)
# print(data["temp"])

#PANDAS HAS 2 PRIMARY DATA STRUCTURES 
# 1 ) DATA FRAME - I/E IS OUR 2 DIMENTIONAL DATA : TABLE 
# 2 ) SERIES - I/E OUR 1D DATA : LIKE A LIST IN PANDAS : EACH COLUMN IS A SERIES IN PANDAS

data_dict=data.to_dict()
print(data_dict)

#converting column to list 
temp_list = data["temp"].to_list()
#print(temp_list)
sum_temp = sum(temp_list)
len_temp=len(temp_list)
avg_temp = sum_temp/len_temp
print(avg_temp)

#OR

print(data["temp"].mean())
print(data["temp"].max())

print(data.temp)

#get ROW IN pandas
print(data[data.day=='Monday'])
print(data[data.temp==data.temp.max()])


monday = data[data.day=='Monday']
celcius = monday.temp 
farenhiet = (celcius* 9/5) + 32
print (farenhiet)
