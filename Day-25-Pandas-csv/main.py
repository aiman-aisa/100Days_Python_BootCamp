# with open("Day-25-Pandas-csv\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day-25-Pandas-csv\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
            
#     print(temperatures)

# import pandas as pd

# data = pd.read_csv("Day-25-Pandas-csv\weather_data.csv")
# print(data)

# data_dict = data.to_dict()

# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # average = sum(temp_list) / len(temp_list)
# # print(average)

# print(data['temp'].mean())

# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday_temp = data[data.day == "Monday"].temp[0]
# print(monday_temp)
# monday_tempF  = monday_temp *9/5 + 32
# print(monday_tempF)

# # create a df from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv(r"Day-25-Pandas-csv\new_data.csv")

import pandas as pd

squirrel_data = pd.read_csv(r"Day-25-Pandas-csv\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data = squirrel_data["Primary Fur Color"].value_counts()

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [data[0], data[1], data[2]]  
}

df = pd.DataFrame(data_dict)
df.to_csv(r"Day-25-Pandas-csv\squirr_count.csv")
