"""Analyze text in a file and write a report with statistics
(number of words, most common word, etc.) to another file"""
# MCS 260 Fall 2021 Lecture 14

import sys

# Check for correct number of arguments
#   argv[0] is always the script name
#   argv[1] will be used to receive the input filename
#   argv[2] will be used to receive the report filename
# Thus we expect argv to have 3 elements overall, and any fewer
# is an error
if len(sys.argv) < 3:
    print("Usage: {} INPUTFILE REPORTFILE".format(sys.argv[0]))
    exit(1)

# Save the filenames in variables with descriptive names
fn = sys.argv[1] # input filename
reportfn = sys.argv[2] # report/output filename

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

# Open the input file
infile = open(fn,"r",encoding="UTF-8")

# Examine the input file and record statistics
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

# Done reading the file, so close it.  From here on, we only need
# the statistics and histogram
infile.close()

# Open the report file and write the report to it
reportfile = open(reportfn,"w",encoding="UTF-8")
reportfile.write("filename={}\n".format(fn))
reportfile.write("words={}\n".format(wordcount))
reportfile.write("distinct_words={}\n".format(len(word_histogram)))
reportfile.write("max_words_per_line={}\n".format(max_words_per_line))

maxcount = max(word_histogram.values()) # maximum number of times any word appears (integer)
most_frequent_words = [ w for w in word_histogram 
                        if word_histogram[w] == maxcount ] # list of strings (perhaps just one)
reportfile.write("most_used_words={}\n".format(",".join(most_frequent_words)))
reportfile.write("most_used_words_freq={} ({:.2f}%)\n".format(maxcount,100.0*maxcount/wordcount))

reportfile.close()