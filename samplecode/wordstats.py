# The following is from 7 CFR § 46.2(u)
# (Federal regulation from the Dept of Agriculture
# defining what "Fresh fruits and fresh vegetables"
# means.)
text="""
Fresh fruits and fresh vegetables include all
produce in fresh form generally considered as
perishable fruits and vegetables, whether or 
not packed in ice or held in common or cold 
storage, but does not include those perishable 
fruits and vegetables which have been
manufactured into articles of food of a different
kind or character.
"""

wordcount = 0
words_seen = []

# Convert punctuation to spaces
text_nopunc = text.replace(","," ").replace("."," ").replace("\'"," ")

for w in text_nopunc.lower().split():
    # w is one of the words from the text
    wordcount = wordcount + 1
    if w not in words_seen:
        words_seen.append(w)

print("Analyzing this text:")
print(text)
print()
print("Words:",wordcount)
print("Distinct words:",len(words_seen))
print("List of distinct words:",words_seen)
