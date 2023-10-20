# # import csv

# # with open("/Users/jondedman/code/jondedman/python_projects/pandas_csvs/day-25-start/weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     clean_data = []
# #     for line in data:
# #         clean_data.append(line.strip())

# #     print(clean_data)

# # /Users/jondedman/code/jondedman/python_projects/pandas_csvs/day-25-start/weather_data.csv

# # with open("/Users/jondedman/code/jondedman/python_projects/pandas_csvs/day-25-start/weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         # print(row)
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))

# #     print(temperatures)

# import pandas as pd

# data = pd.read_csv("/Users/jondedman/code/jondedman/python_projects/pandas_csvs/day-25-start/weather_data.csv")

# data_dict = data.to_dict()


# temp_list = data["temp"].to_list()

# # print(temp_list)

# # av_temp = sum(temp_list) / len(temp_list)

# # print(av_temp)

# # print(data["temp"].max())

# # print(data[data.temp == data.temp.max()])

# monday_temp_in_f = (data[data.day == "Monday"].temp * 9 / 5) + 32

# print(monday_temp_in_f)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data)

# gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
# black_fur = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(gray_fur)
# print(black_fur)
# print(cinnamon_fur)

output_csv_file = "fur_color.csv"
df = pd.DataFrame(data)
fur_counts = df["Primary Fur Color"].value_counts().reset_index()
fur_counts.columns = ["Fur Color", "Count"]
# Replace "Cinnamon" with "Red" in the "Fur Color" column
fur_counts["Fur Color"] = fur_counts["Fur Color"].replace("Cinnamon", "Red")


fur_counts.to_csv(output_csv_file)

print(fur_counts)



# # Example DataFrame
# data = {'Animal': ['Squirrel', 'Rabbit', 'Fox', 'Squirrel', 'Squirrel'],
#         'Primary Fur Color': ['Gray', 'Brown', 'Red', 'Gray', 'Gray'],
#         'Size': ['Small', 'Medium', 'Medium', 'Small', 'Small']}
# df = pd.DataFrame(data)

# # Group the data by "Primary Fur Color" and count the instances
# fur_counts = df['Primary Fur Color'].value_counts().reset_index()
# fur_counts.columns = ['Fur Color', 'Count']

# # Define the path and filename for the new CSV file
# output_csv_file = "fur_color_counts.csv"

# # Save the counts to a new CSV file
# fur_counts.to_csv(output_csv_file, index=False)
