import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
# print(data)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
# nato_dict = dict(zip(data['letter'], data['code'])) # easier method to use in place of dict comprehension
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    name = list(input('What is your name?').upper())
    try:
        output = [nato_dict[letter] for letter in name]  # list comprehension
    except KeyError:
        print('Sorry please enter a word')
        generate()
    else:
        print(output)


generate()
