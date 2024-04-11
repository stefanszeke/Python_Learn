# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for(row) in data:
#         if(row[1] != "temp"):
#             temperatures.append(int(row[1]))
        
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
data['temp'] = data['temp'] *9/5 + 32

print(data)

# print(data['day'][0])

# temps = data['temp'].to_list()
# average = sum(temps)/len(temps)
# average2 = data['temp'].mean()

# max = data['temp'].max()

# print(average)
# print(average2)
# print(max)

# conditions = data['condition']
# unique_conditions = conditions.unique()
# print(unique_conditions)

# print()

mondays = data[data['temp'] == data['temp'].max()]
print(mondays)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data2 = pandas.DataFrame(data_dict)
print(data2)

data2.to_csv('students.csv')