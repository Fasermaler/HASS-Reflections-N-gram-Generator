#!/usr/bin/python
# -*- coding: utf-8 -*- 


# Simple demo script to process reflections manually
# Written by Fasermaler

from reflection_ngram import reflection_post as reflection

try:
	f = open("prompts.txt", "r")
	prompts = f.read().splitlines()
	f.close()
	
	f = open("texts.txt", "r")
	texts = f.read().splitlines()
	f.close()

except:
	print("Unable to find one or more files")


reflect = reflection(prompts, texts)
reflect.process_post()
reflect.generate_summary(30)
reflect.write_HR("output.txt")