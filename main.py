from itertools import groupby
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict
from gui import *
import gui as gui

root.mainloop()
path = gui.select_file
path2 = path.decode("utf8")

with open(path2, "r") as file:
    text = file.read()
    words = word_tokenize(text)

    # activating stopwords
    stop_words = set(stopwords.words("english"))
    no_stopwords_sentence = [w for w in words if not w in stop_words]

    # remove all punctuation
    without_punctuation = [w for w in no_stopwords_sentence if w.isalpha()]

    # filtered by alphabet
    alphabet_sorted = sorted(without_punctuation)

    # word counter
    def count_word(word):
        if word in total_count:
            total_count[word] += 1
        else:
            total_count[word] = 1

    total_count = dict()
    list(map(lambda x: count_word(''.join(filter(str.isalpha, x.lower()))), alphabet_sorted))
    print(total_count)

    print('CHLENIS DOLBAEB')



    # text = text.lower()
    # words = word_tokenize(text)
    #
    # # activating stopwords
    # stop_words = set(stopwords.words("english"))
    # no_stopwords_sentence = [w for w in words if not w in stop_words]
    #
    # # remove all punctuation
    # without_punctuation = [w for w in no_stopwords_sentence if w.isalpha()]
    #
    # # filtered by alphabet
    # alphabet_sorted = sorted(without_punctuation)
    #
    # # counter
    # list = []
    # word_count_dict = defaultdict(int)
    # for word in alphabet_sorted:
    #     temp1 = [word]
    #     word_count_dict[word] += 1
    #     temp1.append(word_count_dict[word])
    #     print(temp1)



    # for i in temp1:
    #     if (i < len(temp1) - 1):
    #         temp1.remove(i)
    #
    # for i in temp2:
    #     if(i< len(temp2)-1):
    #         temp2.remove(i)

    # drop duplicates
    #     drop_duplicates = [el for el, _ in groupby(word)]
    # print(drop_duplicates)

    # show words as list
    # for i in alphabet_sorted:
    #     print(i)








    # for i in word_tokenize(text):
    #     print(i)
    # stop_words = set(stopwords.words("english"))
    # filtered_text = []
    # for w in words:
    #     if w not in stop_words:
    #         filtered_text.append(w)






