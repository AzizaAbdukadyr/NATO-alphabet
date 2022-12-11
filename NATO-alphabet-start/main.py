import pandas

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for index, row in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generic_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [data_dict[letter] for letter in word]
    except KeyError:
        print("Please write only letters")
        generic_phonetic()
    else:
        print(result)

generic_phonetic()

# Try Except
# --------------------------------------------------------------------------------
# Example 1
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)
#
# # Example 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
#
# print(total_likes)