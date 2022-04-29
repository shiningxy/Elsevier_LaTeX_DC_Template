# !/usr/bin/python
# -*- coding:UTF-8 -*-
import os
import shutil
import re
# from PyPDF2 import  PdfFileReader, PdfFileWriter

# move fig and thumbnails to the parent directory
# remove doc figs thumbnails folder
try:
	for i in os.listdir("figs"):
		shutil.move(os.path.join("figs",i), i)
	for i in os.listdir("thumbnails"):
		shutil.move(os.path.join("thumbnails",i), i)
	shutil.rmtree("doc")
	shutil.rmtree("figs")
	shutil.rmtree("thumbnails")
except FileNotFoundError as e:
	pass
# remove github repositories files
try:
	os.system("rd /s/q .git")
	os.remove(".gitignore")
	os.remove("LICENSE")
	os.remove("manifest.txt")
	os.remove("README")
	os.remove("README.md")
except:
	pass

# find double columns .tex file
texName = [x for x in os.listdir(os.getcwd()) if x.split(".")[1] == "tex"][0]
# read old tex file
texFile = open(texName, 'r+')
texFileLines = texFile.readlines()
# create new tex file
texFileOutputPath = os.path.join("Manuscript-LaTeX-Source-File.tex")
outputtexFile = open(texFileOutputPath, "w+")
newtexFileContent = ""
# find figs' path which include figs/ and delete it to fix new relative path
for i in texFileLines:
	newLine = str(i)
	if "figs/" in i:
		newLine = str(i.replace("figs/", ""))
	newtexFileContent += newLine
# write result to new tex file
outputtexFile.write(newtexFileContent)

# find .sty file to delete thumbnails/ path in it
styName = [x for x in os.listdir(os.getcwd()) if x.split(".")[1] == "sty"][-1]
# read old sty file
styFile = open(styName, 'r+')
styFileLines = styFile.readlines()
# create new sty file
styFileOutputPath = os.path.join(styName.split(".")[0] + "-new.sty")
outputstyFile = open(styFileOutputPath, "w+")
newstyFileContent = ""
# find thumbnails' path which include thumbnails/ and delete it to fix new relative path
for i in styFileLines:
	newLine = str(i)
	if "thumbnails/" in i:
		newLine = str(i.replace("thumbnails/", ""))
	newstyFileContent += newLine
# write result to new sty file
outputstyFile.write(newstyFileContent)
