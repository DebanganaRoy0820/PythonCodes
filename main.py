import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
# print(data)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
# nato_dict = dict(zip(data['letter'], data['code'])) # easier method to use in place of dict comprehension
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = list(input('What is your name?').upper())
output = [nato_dict[letter] for letter in name]  # list comprehension
print(output)
