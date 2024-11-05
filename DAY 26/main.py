import pandas
import logo

print(logo.logo)


data=pandas.read_csv('nato_phonetic_alphabet.csv')
new_data={code.letter:code.code for (letter,code) in data.iterrows()}





def extract_function():
    text_input = input("Write a word:").upper()
    extracted_text_input = [letter for letter in text_input]
    try:
        extracted_list = [new_data[letter] for letter in extracted_text_input]
    except KeyError:
        print("Input contains numbers please type only letters")
        extract_function()
    else:
        print(extracted_text_input)
        print(extracted_list)


extract_function()