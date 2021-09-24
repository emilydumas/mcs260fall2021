"""Count words and distinct words in a file and print a report"""
# MCS 260 Fall 2021 Lecture 14

import sys

# Check for correct number of arguments
if len(sys.argv) < 2:
    print("Usage: {} INPUTFILE".format(sys.argv[0]))
    exit(1)

fn = sys.argv[1] # input filename
infile = open(fn,"r",encoding="UTF-8")

# Characters that are always taken to mark a word boundary
# (hence equivalent to spaces for the purpose of splitting
# into words)
always_word_bdry = [ "“", "”", "-", ";",
                     "_", "\ufeff", "(", "?", ".",
                     "\"", "!", "‘", "%", "#", ")",
                     "*", "$", "/", "&", ",", "]",
                     "—", ":", "[" ]

# A string containing all the characters that are allowed in
# the middle of a word, but which should be trimmed from the
# start or end of a word.
remove_from_word_edges = "’'"

def split_words(s):
    """Take a line of text and extract words, attempting to ignore punctuation and numbers"""
    s = s.strip().lower()
    # Convert punctuation that is never part of a word to spaces
    for c in always_word_bdry:
        s = s.replace(c," ")
    L = []
    # split along spaces and examine each piece
    for w in s.split():
        # strip any characters that are allowed inside but not
        # at the ends of words
        w = w.strip(remove_from_word_edges)
        # Are there any alphabet letters left?
        for c in w:
            if c.isalpha():
                # Found an alphabet letter; keep this word
                L.append(w)
                break
    # Return the list of words found in s
    return L

wordcount = 0 # total number of words seen
word_histogram = dict() # keys are distinct words, values are counts
max_words_per_line = 0

for line in infile: # handle one line at a time
    line_words = split_words(line) # split this line into words
    # Is this the longest so far (in word count?)
    if len(line_words) > max_words_per_line: 
        max_words_per_line = len(line_words)
    # Iterate over the words in this line
    for w in line_words:
        wordcount = wordcount + 1 # always increase count
        if w in word_histogram:
            # Word previously seen; increase the count
            word_histogram[w] = word_histogram[w] + 1
        else:
            # Word not previously seen; record it with a count of 1
            word_histogram[w] = 1

# Print the report
print("filename={}".format(fn))
print("words={}".format(wordcount))
print("distinct_words={}".format(len(word_histogram)))
print("max_words_per_line={}".format(max_words_per_line))

maxcount = max(word_histogram.values())
most_frequent_words = [ w for w in word_histogram 
                        if word_histogram[w] == maxcount ]
print("most_used_words={}".format(",".join(most_frequent_words)))
print("most_used_words_freq={} ({:.2f}%)".format(maxcount,100.0*maxcount/wordcount))


# Uncomment to print all the words
# print("distinct words:")
# for w in word_histogram:
#     print(w)