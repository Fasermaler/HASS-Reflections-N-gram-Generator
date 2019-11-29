#!/usr/bin/python
# -*- coding: utf-8 -*- 

# Basic Ngram filter and manipulation class
# Written by Fasermaler

import re
import sets


class ngram:
	def __init__(self, gram1_filter_list, gram2_filter_list, gram3_filter_list):
		self.gram1_filter_list = gram1_filter_list
		self.gram2_filter_list = gram2_filter_list
		self.gram3_filter_list = gram3_filter_list

		self.words = None
		self.word2 = None
		self.word3 = None

		self.gram1_freq = {}
		self.gram2_freq = {}
		self.gram3_freq = {}

		self.count = 0

	def filter_gram1(self, word):
		if word in self.gram1_filter_list:
			return False
		elif len(word) <= 1:
			return False
		else:
			return True

	def filter_gram2(self, word):
		if word in self.gram2_filter_list:
			return False
		elif len(word) <=1:
			return False
		else:
			return True

	def filter_gram3(self, word):
		if word in self.gram3_filter_list:
			return False
		elif len(word) <= 1:
			return False
		else:
			return True

	def process_text(self, text):
		# Reset the word sets
		self.words = None
		self.word2 = None
		self.word3 = None

		# Increment the counter on number of texts processed
		self.count += 1

		# Split the text into words and remove punctuation
		self.words = re.split('[^A-Za-z]+', text.lower())
		self.words = filter(self.filter_gram1, self.words)

		#print("There are {} words".format(len(self.words)))

		for word in self.words:
			if self.gram1_freq.has_key(word):
				self.gram1_freq[word] += 1
			else:
				self.gram1_freq[word] = 1

		# This implements is 2 element sliding window and assigns the results to gram2
		self.word2 = [(self.words[i], self.words[i+1]) for i in xrange(len(self.words)-1)]


		self.gram2_filter_list = [('we', 'can')]


		# Word filter
		self.word2 = filter(self.filter_gram2, self.word2)

		for word in self.word2:
			if self.gram2_freq.has_key(word):
				self.gram2_freq[word] += 1
			else:
				self.gram2_freq[word] = 1


		# 3-grams
		self.word3 = [(self.words[i], self.words[i+1], self.words[i+2]) for i in xrange(len(self.words)-2)]

		self.word3 = filter(self.filter_gram3, self.word3)

		for word in self.word3:
			if self.gram3_freq.has_key(word):
				self.gram3_freq[word] += 1
			else:
				self.gram3_freq[word] = 1

	# Methods for retriveing the ngram dicts
	# k is a parameter to limit the entries to the k-th most popular ngrams
	def get_gram1(self, k=0):
		g_grem1 = sorted(self.gram1_freq.items(), key=lambda (word, count): -count)
		if k == 0:
			return g_grem1
		if k > len(g_grem1):
			return g_grem1
		else:
			return g_grem1[:k]


	def get_gram2(self, k=0):
		g_grem2 = sorted(self.gram2_freq.items(), key=lambda (word, count): -count)
		if k == 0:
			return g_grem2
		if k > len(g_grem2):
			return g_grem2
		else:
			return g_grem2[:k]

	def get_gram3(self, k=0):
		g_grem3 = sorted(self.gram3_freq.items(), key=lambda (word, count): -count)
		if k == 0:
			return g_grem3
		if k > len(g_grem3):
			return g_grem3
		else:
			return g_grem3[:k]

	def get_ngrams(self, k=0):
		return (self.get_gram1(k), self.get_gram2(k), self.get_gram3(k))

# OLD IMPLEMENTATION =======================================
# # Define list of words to filter
# # Partly taken from: https://www.englisch-hilfen.de/en/grammar/conjunctions.htm
# filter_list = [None, "no", "it", "is", "the", "and", "if", "are", "so", "but", "either", "yet",
#                "nor", "for", "although", "as", "because", "but", "even", "though", "how", "however",
#                "since", "unless", "what", "when", "whether", "of", "in", "to", "was", "were"]


# # Define the filter function to be used by the filter call
# # Also filter words of length 1
# def filter_words(word):
# 	if word in filter_list:
# 		return False
# 	elif len(word) == 1:
# 		return False
# 	else:
# 		return True

# # Split the text into words and remove punctuation
# words = re.split('[^A-Za-z]+', text.lower())
# # Remove empty words
# words = filter(filter_words, words)

# print("There are {} words".format(len(words)))

# # Debug to print the words
# #print(words)


# # 1-grams ===================================================
# gram1 = set(words)

# # Debug to print the 1-grams
# #print(gram1)

# # Convert to dictionary and populate with the word frequencies
# gram1 = dict()
# for word in words:
# 	if gram1.has_key(word):
# 		gram1[word] += 1
# 	else:
# 		gram1[word] = 1


# gram1 = sorted(gram1.items(), key=lambda (word, count): -count)

# # Debug print gram1
# #print(gram1)

# # 2-grams ======================================================

# # This implements is 2 element sliding window and assigns the results to gram2
# word2 = [(words[i], words[i+1]) for i in xrange(len(words)-1)]


# word2_filter_list = [('we', 'can')]

# def filter_word2(word):
# 	if word in word2_filter_list:
# 		return False
# 	else:
# 		return True

# # Remove empty words
# word2 = filter(filter_word2, word2)

# gram2 = set(word2)

# gram2 = dict()
# for word in word2:
# 	if gram2.has_key(word):
# 		gram2[word] += 1
# 	else:
# 		gram2[word] = 1


# gram2 = sorted(gram2.items(), key=lambda (word, count): -count)

# print(gram2)


# # Debug to print the 2-grams
# # print(gram2)


# # 3-grams

# # This implements is 2 element sliding window and assigns the results to gram2
# word3 = [(words[i], words[i+1], words[i+2]) for i in xrange(len(words)-2)]
# gram3 = set(word3)

# # Secondary filter for 3 grams to check for unneccessary common conjunctions
# word3_filter_list = []

# def filter_word3(word):
# 	if word in word3_filter_list:
# 		return False
# 	else:
# 		return True

# # Remove empty words
# word3 = filter(filter_words, word3)


# # Debug to print the 3-grams
# # print(gram3)



