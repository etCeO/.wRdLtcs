
# Ethan E. Lopez
# 002425516
# etlopez@chapman.edu
# CPSC 230 - Section 2
# Program Assignment 5

import operator
# imports operator module from Python

def read_file(file):
# creates a function read_file that takes in the name of a file
    f = open(file, 'r')
    # f variable opens the argument file in read mode
    a = ''
    # a variable creates an empty string
    for line in f:
    # creates a for loop that goes through each line in file f
        a += str(line)
        # line in string form in file f is added to variable a
    f.close()
    # file f is closed
    return a # returns a, the whole file in string form     

def build_dictionary(string):
# creates a function build_dictionary that takes in string argument a
    string = string.lower()
    # all words in string a are converted to lowercase form
    string = string.split()
    # each word in string a is split into individual formats as a list of words
    word_count = {}
    # creates an empty dictionary called word_count
    for word in string:
    # creates a for loop for every individual word in string a
        if word.isalpha():
        # identifies if the word has all letters
            word_count[word] = word_count.get(word, 0) + 1
            # adds the count of the word to the dictionary
        else:
        # identifies if the word does not have all letters
            for i in word:
            # creates a for loop for the individual characters in the word
                if i.isalpha() == False:
                # creates the condition if a character is not a letter
                    word = word.replace(i, '')
                    # removes the character from the word by replacing the non-alpha component with an empty placeholder
            word_count[word] = word_count.get(word, 0) + 1
            # adds the count of the word to the dictionary
    return word_count # returns dictionary word_count with all individual words counted 

def write_file(dictionary, outputfile):
# creates a function write_file that takes in a dictionary as the argument word_count
    g = open(outputfile, 'w')
    # writes / opens a new file g with the name BeeMovieDict
    dictionary = sorted(dictionary.items(), key=operator.itemgetter(1))
    # sorts word_count dictionary into ascending order
    dictionary = dictionary[::-1]
    # reverses the order of word_count dictionary into descending order
    g.write(str(dictionary))
    # writes the result of word_count as a string to file g
    g.close() # file g is closed

read_file('BeeMovieScript.txt')
# calls the function of read_file with argument BeeMovieScript.txt as the file being read
# 'BeeMovieScript.txt' is transformed into a string

a = read_file('BeeMovieScript.txt')
# assigns variable a with the result of read_file('BeeMovieScript.txt')

build_dictionary(a)
# calls the function build_dictionary to build a dictionary of all words from string a

word_count = build_dictionary(a)
# assigns variable word_count as the result of build_dictionary(a)
# a as stated before was the file string
# build_dictionary transforms 'a' into a dictionary with separate counts for each individual word

write_file(word_count, 'counts.txt')
# a call is given to the function write_file to write a file that takes in dictionary word_count
# the final output from all previous functions is given in the file counts.txt






