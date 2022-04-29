# pip install pypdf2
# pip install pdfplumber
import os
import shutil
import re
from PyPDF2 import  PdfFileReader, PdfFileWriter

# try:
# 	for i in os.listdir("figs"):
# 		shutil.move(os.path.join("figs",i), i)
# 	for i in os.listdir("thumbnails"):
# 		shutil.move(os.path.join("thumbnails",i), i)
# 	shutil.rmtree("doc")
# 	shutil.rmtree("figs")
# 	shutil.rmtree("thumbnails")
# except FileNotFoundError as e:
# 	pass
# try:
# 	os.system("rd /s/q .git")
# 	os.remove(".gitignore")
# 	os.remove("LICENSE")
# 	os.remove("manifest.txt")
# 	os.remove("README")
# 	os.remove("README.md")
# except:
# 	pass

# print(os.listdir(os.getcwd()))
texName = [x for x in os.listdir(os.getcwd()) if x.split(".")[1] == "tex"]
print(texName)
texFile = open(texName, 'r+')
for i in texFile.readlines():
	if "{figs/" in i:
		print(i)