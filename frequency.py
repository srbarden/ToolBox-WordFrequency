""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """

    f = open(file_name, 'r')

    # read the lines to look for start
    lines = f.readlines()
    for line in lines:
        start = line.find('START OF THIS PROJECT GUTENBERG')
        end = line.find('END OF THIS PROJECT GUTENBERG')
    # cut out the beginning, start after 'START OF ...'
    lines = lines[start+1:end]

    words = []
    for line in lines:
        w = line.split()
        words.extend(w)

    for word in range(len(words)):
        w = words[word]
        w = w.lower()
        w = w.strip(string.punctuation)
        w = w.strip(string.whitespace)
        words[word] = w

    return words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed all are lower case with no punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    words_ordered = sorted(word_freq, key=word_freq.get, reverse=True)
    return words_ordered[0:n]


if __name__ == "__main__":
    words = get_word_list('federalist_papers.txt')
    top_100 = get_top_n_words(words, 100)
    print(top_100)

    f = open('top100words.txt', 'w+')
    for word in top_100:
        f.write(word)
        f.write('\n')
    f.close
