import word_set as ws, os, time
import matplotlib.pyplot as plt

max_bucket_list = []
amount_of_words_lst = [1000,2000,3000,4000,5000]
path1k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/1k.txt'
path2k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/2k.txt'
path3k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/3k.txt'
path4k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/4k.txt'
path5k ='C:/Users\Mikael/python_courses/1DT901/mg223tm_groupproj/part4/words_for_graph/5k.txt'

def max_calc(path): # takes path returns max_bucket_size 
    buckets = ws.new_empty_set() #creating new empty set
    sd = open(path, "r",encoding='utf-8') 
    words = 0
    for line in sd:
        words += 1
        print(f"i am on line {words}")
        line = line.replace("\n",'') # removes linebreaks
        buckets = ws.add_with_full(buckets,line) # using add_with_full cuz small program
    sd.close()
    return ws.max_bucket_size(buckets)

max_bucket_list.append(max_calc(path1k)) # putting results in list for graph
max_bucket_list.append(max_calc(path2k))
max_bucket_list.append(max_calc(path3k))
max_bucket_list.append(max_calc(path4k))
max_bucket_list.append(max_calc(path5k))


plt.plot(amount_of_words_lst,max_bucket_list) # graph
plt.ylabel("Max bucket size") # naming axis
plt.xlabel("Number of words added to set")  # naming axis
plt.title("Max bucket size compared to number of words added")
plt.show()

print(max_bucket_list) # for accurate measurment
print(amount_of_words_lst)