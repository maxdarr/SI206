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

import nltk
from nltk.book import *
import random
#makes SnStext equal to the first 150 tokens of text 2 from the nltk corpus which is Sense and Sensibility
SnStext = text2[:150]
#PRINT ORIGINAL STRING CODE

original_str = ""
# iterates over the tokens in SnStext and adds it to a string and then prints it
for elem in SnStext:
	original_str += elem + " "
print("Original Text")
print(original_str)

#print(nltk.pos_tag(SnStext))

# makes a dictionary that maps the tags of a word to what the tag is in words for when the user is prompted
# sets a probability for each of the tags in the tagmap
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","RB":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"RB":.1}
new_string = []

# defines a way for appending to the new_string that adds a space to the word if it is not punctuation
def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

#iterates through the words and their tags in SnStext and if the tag is not in the tagmap dictionary or 
# the random.random funtion generates a number over the substituion probabilit for that tag then it just 
#appends the word to the new string. However if the random.random function generates a number that is 
#within the probability then it prompts the user for the specific tag to enter in a new word
# Finally, it joins together the new string and prints it out		
for (word, tag) in nltk.pos_tag(SnStext):
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		new_string.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		new_string.append(spaced(new_word))
print("New Text")
print ("".join(new_string))


print("\n\nEND*******")
