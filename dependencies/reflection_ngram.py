#!/usr/bin/python
# -*- coding: utf-8 -*-

# Class to handle processing of reflection ngrams
# Written by Fasermaler
from ngram import ngram

# Define the word filter lists for n-grams
f = open("filter_words.txt", "r")
filter_words = f.read().splitlines()
f.close()


# Get the list of filter words
gram1_filter_list = [None]

for word in filter_words:
	if word == "":
		pass
	else:
		gram1_filter_list += [word]
gram2_filter_list = [('we', 'can')]

gram3_filter_list = []

class reflection_post:
	def __init__(self, prompts, texts):
		self.prompts = prompts
		self.texts = texts

		# create ngram objects for both prompt and text
		self.prompt_gram = ngram(gram1_filter_list,
	                             gram2_filter_list,
	                             gram3_filter_list)

		self.texts_gram = ngram(gram1_filter_list,
	                            gram2_filter_list,
	                            gram3_filter_list)

		# Initialize summary dictionary and human readable summary
		self.summary_dict = {}
		self.summary_HR = ""

	def process_prompts(self):
		for prompt in self.prompts:
			self.prompt_gram.process_text(prompt)

	def process_texts(self):
		for text in self.texts:
			self.texts_gram.process_text(text)

	def process_post(self):
		self.process_prompts()
		self.process_texts()

	def sort_popular(self, l1, l2, l3, k=0):
		main_dict = {}
		for d in (l1, l2, l3):
			for item in d:
				if main_dict.has_key(item[0]):
					main_dict[item[0]] += item[1]
				else:
					main_dict[item[0]] = item[1]

		main_dict_list = sorted(main_dict.items(), key=lambda (word, count): -count)

		if k == 0:
			return main_dict_list
		if k > len(main_dict_list):
			return main_dict_list
		else:
			return main_dict_list[:k]

	# Compares the texts to the prompts to generate a list of
	# ngrams that appeared in the prompts and a list that did not
	def compare_to_prompt(self, prompt_list, text_list):
		current_ngrams = {}
		new_ngrams = {}


		for item in text_list:
			# Flag for checking whether the ngram is already added to prompts
			in_prompt = False
			for ngram in prompt_list:

				if item[0] == ngram[0]:
					if current_ngrams.has_key(item[0]):
						pass
					else:
						current_ngrams[item[0]] = item[1]

					in_prompt = True
			if in_prompt == False:
				if new_ngrams.has_key(item[0]):
					pass
				else:
					new_ngrams[item[0]] = item[1]

		current_ngrams_list = sorted(current_ngrams.items(), key=lambda (word, count): -count)
		new_ngrams_list = sorted(new_ngrams.items(), key=lambda (word, count): -count)

		return current_ngrams_list, new_ngrams_list


	# Generate the summary, takes the k-th most popular ngrams from prompts
	# and v-th most popular ngrams from the texts
	# from each category for consideration
	def generate_summary(self, k=0, v=0):
		# resets the summary
		self.summary_dict = {}
		self.summary_HR = ""

		# generate the main ngram list for prompts

		prompt_gram1, prompt_gram2, prompt_gram3 = self.prompt_gram.get_ngrams()
		#print(prompt_gram1)
		self.main_prompt_gram = self.sort_popular(prompt_gram1,
												  prompt_gram2,
												  prompt_gram3)

		self.summary_dict["prompt_ngrams"] = self.main_prompt_gram[:k]

		# generate the main ngram list for texts

		text_gram1, text_gram2, text_gram3 = self.texts_gram.get_ngrams()

		self.main_texts_gram = self.sort_popular(text_gram1,
												 text_gram2,
												 text_gram3)

		self.summary_dict["text_ngrams"] = self.main_texts_gram[:k]

		# Get the list of ngrams that are common with the prompt as well as new ngrams
		self.current_ngrams, self.new_ngrams = self.compare_to_prompt(self.main_prompt_gram, self.main_texts_gram)

		self.summary_dict["ngrams_related_to_prompt"] = self.current_ngrams[:k]
		self.summary_dict["new_ngrams"] = self.new_ngrams[:k]
		self.summary_dict["precision"] = k

		self.generate_HR()
		print(self.summary_HR)


		#print(self.summary_dict)

	# Generate Human Readable text
	def generate_HR(self):
		self.summary_HR = "\n[SUMMARY]\n"
		self.summary_HR += "Showing " + str(self.summary_dict["precision"]) + " most popular entries per category\n\n"

		self.summary_HR += "[N-grams from the reflection prompt]\n"
		for item in self.summary_dict["prompt_ngrams"]:
			if type(item[0]) is tuple:
				for i in item[0]:
					self.summary_HR += str(i) + " "
				self.summary_HR += str(item[1]) + "\n"
			else:
				self.summary_HR += str(item[0]) + " " + str(item[1]) + "\n"

		self.summary_HR += "\n[N-grams from the reflection submissions]\n"
		for item in self.summary_dict["text_ngrams"]:
			if type(item[0]) is tuple:
				for i in item[0]:
					self.summary_HR += str(i) + " "
				self.summary_HR += str(item[1]) + "\n"
			else:
				self.summary_HR += str(item[0]) + " " + str(item[1]) + "\n"

		self.summary_HR += "\n[N-grams from prompt that appeared in submissions]\n"
		for item in self.summary_dict["ngrams_related_to_prompt"]:
			if type(item[0]) is tuple:
				for i in item[0]:
					self.summary_HR += str(i) + " "
				self.summary_HR += str(item[1]) + "\n"
			else:
				self.summary_HR += str(item[0]) + " " + str(item[1]) + "\n"

		self.summary_HR += "\n[N-grams that were not from prompt]\n"
		for item in self.summary_dict["new_ngrams"]:
			if type(item[0]) is tuple:
				for i in item[0]:
					self.summary_HR += str(i) + " "
				self.summary_HR += str(item[1]) + "\n"
			else:
				self.summary_HR += str(item[0]) + " " + str(item[1]) + "\n"

	def write_HR(self, filename):
		lines = self.summary_HR.splitlines()
		#print(lines)
		f = open(str(filename), "w+")
		for line in lines[1:]:
			f.write(line)
			f.write("\n")
		f.close()




# prompt = ["This comes a little late. Before this week is over, make one observation about the viability of Asimov's Three Laws of Robotics either in 'The Evitable Conflict' (short story) or 'Three Robots' (from Love, Death +Robots) by engaging with one science fiction 'icon' and what it represents -- robots, mad scientist, damsel in distress, computers, the city, habitats, etc. Is the use of the icon typical? If not, what changed from the usual understanding of that icon?"]

# text1 = "In the Three Robots, it is not immediately clear and hard to infer if the robots are actually following Asimov's 3 laws of Robotics as there are no humans for the audience to see the laws in action. However, after some thinking, maybe they do. Asimov's 3 Laws of Robotics lay the general foundation that the robots would never harm humans in any way at all. And given that it was mentioned that humans brought harm upon themselves (although not specifically how) we can conclude that robots played no direct cause in the extinction of humans. In addition, looking at the type of robots of the main characters, we can infer that they were created at a time when mankind was generally okay with the mass production of robots as a service product, which means they must have gained society's trust in their safeness (which i believe most definitely involves passing the very popular 3 laws)"
# text2 = "Isaac Asimov’s the evitable conflict’ we can see the story about the people have no reason to follow them, but humans of the time already know that it is the best choice for humans to follow the supercomputer's suggestions. In the story we can think that it is possible to make a robot like super computer but in real life our technique is still have to be more advanced to satisfy human thinking about robot adviser.Isaac asimov’s many short story only in the eviatble conflict we can see basic laws of robotics that talk about humanity. Basic laws definition is that robot have to do something that not affect humanity and if there is something that affect humanity robot have to do something. I think that in this line what is humanity that we can define correctly. So, robot can know that what is the range that did not affect humanity.So I think this question can be discussed in many thinkings and When reading this material I can get a chance to think what is humanity and if supercomputer and robot rules human what will happen and how human have to behave."
# text3 = "I feel that Isaac Asimov’s Three Laws of Robotics would not viable upon watching ‘Three Robots’(from Love, Death + Robots).This is due to the fact that cats are depicted as being genetically engineered by humans to have opposing thumbs and hence, were the cause of the human extinction. This can be highlighted by the cat(that was following the 3 robots) mentioning that, “When we could open our own tuna cans, that was pretty much that for the human race.” This shows that the cats, being “machines” since they were modified, violated Asimov’s first law of Robotic by harming/killing humans. The icon of ‘robot’ could be said to be typical in this case, typical in the sense that these genetically engineered cats, who were now considered to be robots, were the cause of human extinction, killing the ones that created them. This resonates with many sci-fi films, such as “I-Robot”, where the robots begin to harm the human species that created them. Hence the robot icon, given its portrayal in ‘Three Robots’ by cats as well as its portrayal in many sci-fi films, suggests that Asimov’s Three Laws of Robotics will never be viable."


# texts = [text1, text2, text3]

# reflect = reflection_post(prompt, texts)
# reflect.process_post()
# reflect.generate_summary(10)

# reflect1 = ngram(gram1_filter_list,
# 	             gram2_filter_list,
# 	             gram3_filter_list)

# reflect1.process_text(text1)
# reflect1.process_text(text2)
# reflect1.process_text(text3)

# print("=========== 1-GRAM ===========")
# print(reflect1.get_gram1())
# print("=========== 2-GRAM ===========")
# print(reflect1.get_gram2())
# print("=========== 3-GRAM ===========")
# print(reflect1.get_gram3())
