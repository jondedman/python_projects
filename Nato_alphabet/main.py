student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# print(nato_dataframe)

# for (index, row) in nato_dataframe.iterrows():
#     # print(index)
#     print(row.letter)
#     print(row.code)



#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row['letter']:row['code'] for _, row in nato_dataframe.iterrows()}

print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

code_words = []

word = input("Please type word to be encoded: ").upper()
for letter in word:
    code_words.append(nato_dict[letter])

print(code_words)
