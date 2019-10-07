'''
find_and_replace('story.txt', 'Alice', 'Colt')
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file, rep_word, new_word):
    with open(file, 'r+') as text:
        n_file = text.read()
        new_file = n_file.replace(rep_word, new_word)
        text.seek(0)
        text.write(new_file)
        text.truncate()