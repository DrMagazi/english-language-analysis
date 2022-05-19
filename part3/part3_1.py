import word_set as ws
import os
path = 'C:/Users/Mikael/python_courses/1DT901/mg223tm_groupproj/part1/textfiles/holy_words.txt' 
sd = open(path, "r",encoding='utf-8') #set ur own path in life
buckets = ws.new_empty_set()
word = 0


for line in sd: 
    word += 1 # keeps track of amount of words it tries to add 
    print(f"i am on line {word}")
    line = line.replace("\n",'') # removes linebreak
    buckets = ws.add(buckets,line)
    if word > len(buckets): ## dont use 1:1 ratio unless u want empty lists
       buckets = ws.double(buckets) # double the list and rehashe 

sd.close()

wd = ws.unique_words(buckets)
print(wd)

#english amount of unique words 88811
#holy words amount of unique words 1863