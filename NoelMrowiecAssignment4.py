# INF360 - Programming in Python
# Noel Mrowiec
# Assignment 4
# Open story, replaces 'Sherlock Holmes' with my name, outputs the count of 
# replaces and 'the', then outputs new story to text file

import re

#Read text file
file = open('story.txt', 'r')

story = file.read();
file.close()

#find find and replace 'Sherlock Holmes'
origName = 'Sherlock Holmes'
regex = f"(?:{origName})"
replacementName = 'Noel Mrowiec'
result, foundCount = re.subn(regex, replacementName, story)
print(f'Original name: {origName}, replacement name: {replacementName}, count of replacement= {foundCount}')

#find find and replace 'Sherlock Holmes'
regex = r"(?:the)"
theList = re.findall(regex, story)
theCount = len(theList)
print(f'Total number of occurances of "the"= {theCount}')

# write the replaced file for new file
newFile = open("new_story.txt", 'w')
newFile.write(result)

#close file
newFile.close()


