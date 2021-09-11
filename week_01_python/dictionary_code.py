# For dictionaries you can write a program that reads a file and uses a dictionary to count the number of times each word appears.

dict = {}

file = open("text.txt")

text = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters. My dear Mr. Bennet, said his lady to him one day, have you heard that Netherfield Park is let at last? Mr. Bennet replied that he had not. But it is, returned she; for Mrs. Long has just been here, and she told me all about it. Mr. Bennet made no answer."

# Cleaning text and lower casing all words
for char in '-.,\n':
    text = text.replace(char,' ')
text = text.lower()

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = text.split()

# count number of times each word comes up in list of words (in dictionary)
for word in word_list:
    dict[word] = dict.get(word, 0) + 1


print(dict)


# # also reading a file:
# f = open("text.txt")
#
# for k in dict.keys():
#     dict.setdefault(k, 0)
#     dict[k] += 1
#     #print(k,dict[k])
#
# print(dict)
#
# for line in f.readlines():
#     line = line.strip()
#     print(line)
