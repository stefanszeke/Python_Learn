import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240129.csv')

colors = data['Primary Fur Color'].unique()
colors_dict = {}

for color in colors:
    if(str(color) != 'nan'):
        colors_dict[color] = len(data[data['Primary Fur Color'] == color])

new_data = pd.DataFrame(colors_dict.items(), columns=['Fur Color', 'Count'])

print(new_data)

new_data.to_csv('squirrel_count.csv')