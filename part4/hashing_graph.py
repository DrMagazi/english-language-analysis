import word_set as ws, os, time
import matplotlib.pyplot as plt



time_lst = []
amount_of_words_lst = [1000,2000,3000,4000,5000]
path1k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/1k.txt'
path2k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/2k.txt'
path3k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/3k.txt'
path4k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/4k.txt'
path5k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/5k.txt'
# list of paths each containg around 1000,2000,3000,4000,5000 words

def time_calcs(path):
    buckets = ws.new_empty_set() #creating new empty set
    start = time.time() # noteing time at start
    sd = open(path, "r",encoding='utf-8')
    words = 0
    for line in sd:
        words += 1
        print(f"i am on line {words}") # my loading screen
        line = line.replace("\n",'') # no linebreaks allowed
        buckets = ws.add_with_full(buckets,line) # using add_with_full cuz small program
    end = time.time() # noteing time at start
    result = end - start # time it took
    sd.close()
    return result

def words_sec(list_of_time,amountofwords): #calcs the average words/sec
    return amountofwords/average(list_of_time)

def average(lst):
    return sum(lst)/len(lst)


saver1 =[]
saver2 =[]
saver3 =[]
saver4 =[]
saver5 =[]

for i in range(5): # doing each file 5 times and saving in savers1-5
    sd1 = time_calcs(path1k)
    saver1.append(sd1)
    sd2 = time_calcs(path2k)
    saver2.append(sd2)
    sd3 = time_calcs(path3k)
    saver3.append(sd3)
    sd4 = time_calcs(path4k)
    saver4.append(sd4)
    sd5 = time_calcs(path5k)
    saver5.append(sd5)
    
time_lst.append(average(saver1)) #saving the average time of each file in time 
time_lst.append(average(saver2))
time_lst.append(average(saver3))
time_lst.append(average(saver4))
time_lst.append(average(saver5))
word_sec_list =[]
word_sec_list.append(words_sec(saver1,1000)) #calc the average words/s for each file
word_sec_list.append(words_sec(saver2,2000))
word_sec_list.append(words_sec(saver3,3000))
word_sec_list.append(words_sec(saver4,4000))
word_sec_list.append(words_sec(saver5,5000))



print(time_lst)
print(words_sec(saver1,1000),words_sec(saver2,2000),words_sec(saver3,3000),words_sec(saver4,4000),words_sec(saver5,5000))
plt.plot(amount_of_words_lst,word_sec_list)
plt.ylabel("Words per second")
plt.xlabel("Number of words") 
plt.show()

