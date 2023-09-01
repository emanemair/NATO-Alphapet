import pandas as pd

dataset = pd.read_csv("nato_phonetic_alphabet.csv")


user_name = input("enter your name").upper()

letter_in_user_name= [letter for letter in user_name]

NATO_code = {row.letter : row.code for (index, row) \
in dataset.iterrows() if row.letter in letter_in_user_name}

print(f"NATO_code for {user_name.lower()} :  {NATO_code} ")
