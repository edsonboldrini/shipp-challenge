import sys

line=""
lines=[]
words=[]
wordsTable={}

fileTest = open(sys.argv[1], "r")
line = fileTest.readline()
while line!="":
	lines.append(line.split())
	line = fileTest.readline()

#print(lines)

for line in lines:
	for word in line:
		word=word.lower()
		if word[-1].isalpha():
			if word in wordsTable:
				wordsTable[word]+=1
			else:
				wordsTable[word]=1
		else:
			if word[:-1] in wordsTable:
				wordsTable[word[:-1]]+=1
			else:
				wordsTable[word[:-1]]=1
		
print(wordsTable)