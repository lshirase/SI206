# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random
from nltk import word_tokenize,sent_tokenize
from nltk.book import * 



tokens = text2[:150]
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples


tagmap = {"NN":"a noun","CC":"a conjunction","VB":"a verb","JJ":"an adjective","RB":"an adverb"} #added adverbs, and conjunctions removed plural nouns. wooo
substitution_probabilities = {"NN":.15,"CC":.10,"VB":.10,"JJ":.10, "RB":.10} ##ask about nouns vs plural nouns

def spaced(word):
	if word in ["[", "]", ",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

print("ORGINAL TEXT")
for word in tokens:
	print(spaced(word), end="")
print("\n")

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print("\n" + "Madlib'd Text Wow!")
print ("".join(final_words))


print("\n\nEND*******")
