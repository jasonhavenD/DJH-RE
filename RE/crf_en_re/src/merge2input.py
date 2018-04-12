#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:convert2input
   Author:jason
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""
import codecs

delimiter = '\t'
if __name__ == '__main__':
	inputs = ["../data/tokens/tokens1.txt.utf-8", "../data/tagged/tokens1_tagged.txt.utf-8",
	          "../data/nered/nered1.txt.utf-8", "../data/dependency/dependency1.txt.utf-8",
	          "../data/raw/raw1_tagged.txt.utf-8"]

	output = "../data/input/input1.txt.utf-8"

	tokenses = codecs.open(inputs[0], 'r', encoding='utf-8').readlines()
	taggedes = codecs.open(inputs[1], 'r', encoding='utf-8').readlines()
	neredes = codecs.open(inputs[2], 'r', encoding='utf-8').readlines()
	dependencies = codecs.open(inputs[3], 'r', encoding='utf-8').readlines()
	targets = codecs.open(inputs[4], 'r', encoding='utf-8').readlines()

	# print(len(tokenses),len(taggedes),len(neredes),len(dependencies),len(targets))

	content = []

	for tokens, tags, ners, deps, tars in zip(tokenses, taggedes, neredes, dependencies, targets):
		line = []
		for token, tag, ner, dep, tar in zip(tokens.strip().split(), tags.strip().split(delimiter),
		                                     ners.strip().split(delimiter), deps.strip().split(delimiter),
		                                     tars.strip().split(delimiter)):
			line.append(delimiter.join(
				(token, tag.split('/')[1], ner.split('/')[1], dep.split('/')[1], dep.split('/')[2], tar.split('/')[1])))
		content.append(line)

	# print(len(content))
	# for c in content:
	# 	print(c)

	with open(output, 'w', encoding='utf-8') as f:
		for line in content:
			for item in line:
				f.write(item)
				f.write('\n')
			f.write('\n')
