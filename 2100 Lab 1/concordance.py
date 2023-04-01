"""
SYSC 2100 Winter 2023
Lab 1, Part 3, Exercise 4, Extra-Practice Exercise 5
"""

__author__ = 'Ahmed Babar'
__student_number__ = '101154651'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the documentation
# (available @ python.org).


def build_concordance(filename: str) -> dict[str, list[int]]:
    """Return a concordance of words in the text file
    with the specified filename.

    The concordance is stored in a dictionary. The keys are the words in the
    text file. The value associated with each key is a list containing the line
    numbers of all the lines in the file in which the word occurs.)

    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    infile = open(filename, "r")
    hist = {}

    currentline = 0  # Counter for current line
    for line in infile:  # For every line in file
        word_list = line.split()  # Split line into words
        currentline += 1
        for word in word_list:
            # removes punctuation
            word = word.strip(string.punctuation).lower()
            if word != '':
                count = hist.get(word, [])
                duplicates = False
                for value in count:
                    if currentline == value:
                        duplicates = True
                if(duplicates == False):
                    count.append(currentline)
                    hist[word] = count
    print(hist)
    return hist

# Extra-Practice: Exercise 5 Solution


if __name__ == '__main__':
    pass
    # Write your solution to Extra-practice Exercise 5 here

    # Test cases Exercise 4
    # build_concordance('two_cities.txt')
    # build_concordance('sons_of_martha.txt')
