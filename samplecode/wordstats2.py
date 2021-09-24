"""Count words and distinct words in a paragraph of text
(stored in a variable) and print a report"""
# MCS 260 Fall 2021 Worksheet 5

text = """The King took a heavy chamois leather bag from under his cloak and laid
it on the table.

"There are three hundred pounds in gold and seven hundred in notes," he
said.

Holmes scribbled a receipt upon a sheet of his notebook and handed it
to him.

"And Mademoiselle's address?" he asked.

"Is Briony Lodge, Serpentine Avenue, St. John's Wood."

Holmes took a note of it. "One other question," said he. "Was the
photograph a cabinet?"

"It was."

"Then, good-night, your Majesty, and I trust that we shall soon have
some good news for you. And good night, Watson," he added, as the
wheels of the royal brougham rolled down the street. "If you will be
good enough to call tomorrow afternoon at three o'clock I should like
to chat this little matter over with you.\""""

wordcount = 0
words_seen = []

punctuation = [".","?",",","\'","\"",":",";","-","(",")"]

filtered_text = text.lower() # convert to lower case
# Replace punctuation with spaces
for c in punctuation:
    filtered_text = filtered_text.replace(c," ")

for w in filtered_text.split():
    wordcount = wordcount + 1
    if w not in words_seen:
        words_seen.append(w)
        

print("Analyzing this text:")
print(text)
print()
print("Words:",wordcount)
print("Distinct words:",len(words_seen))
print("List of distinct words:",words_seen)
