# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size         
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets

def key_calc(word,word_set): # hash calc
    saver = 0 
    for i in word:
        saver += ord(i)
    return saver % len(word_set) # hash value depends on len(word_set)


# Adds word to word set if not already added 
def add(word_set, word): # had to add return word_set and we all good i think
    calcvalue = key_calc(word,word_set)
    if word not in word_set[calcvalue]:
        word_set[calcvalue].append(word)
    return word_set

# Returns current number of elements in set
def count(word_set):
    savs = 0
    for i in range(len(word_set)): # loops everything
        savs += len(word_set[i]) #returns number of elements in set
    return savs


# Returns current size of bucket list 
def bucket_list_size(word_set):
    sd = len(word_set)
    return sd
    

# Returns a string representation of the set content 
def to_string(word_set):
    for i in range(len(word_set)):
        print(i, end=" ") # use file verison for bigger files
        for j in word_set[i]: # prints all elemns the word_set[i]
                print("-->", end = " ") # adding arrrows cuz cool
                print(j, end = " ")
        print()
   

# Returns True if word in set, otherwise False    
def contains(word_set, word):
    if word in word_set[key_calc(word,word_set)]:
        return True 
    return False
    

# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word):
    calcvalue = key_calc(word,word_set)
    if word in word_set[calcvalue]: # removes the word if there
        word_set[calcvalue].remove(word) # only checks the list its supposed to be in 
    
  
# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    savr = 0
    for i in range(len(word_set)):
        if len(word_set[i]) > savr:
            savr = len(word_set[i]) 
    return savr 


def is_full(word_set): # checks if its full  # dont use for big programs takes too long
    save = 0    
    for i in range(len(word_set)): 
        save += len(word_set[i]) #compares the amount of elems in the set with set size ( len(word_set))
    if save > len(word_set):
        return True
    return False


def double(word_set): # should be used if set gets close to full or if is_full returns true
    temp_stor = []
    ins = int(len(word_set)*2 / 10)
    for i in range(ins):  # creates a new list with double the len the prev one   
         temp_stor.extend(new_empty_set())
    
    for i in range(len(word_set)): # should move all chars to correct place cuz diffrent len of list
        for j in word_set[i]: 
           temp_stor = add(temp_stor, j) # use add function for new list aka rehashing the list
    return temp_stor
    

def to_file(word_set,write_path): # writing to file for viusals

    ss = open(write_path, "w",encoding='utf-8')
    for i in range(len(word_set)): # basicly same as string
        ss.write(str(i))
        for j in word_set[i]:
                ss.write("-->  ") 
                ss.write(j) 
        ss.write("\n")
    ss.close


def unique_words(word_set): # Saad unique words
    count = 0
    for i in range(len(word_set)):
        for j in word_set[i]:
            count += 1
    return count


def add_with_full(word_set, word): # this add funciton works easier to use with smaller files up to 500k words
    calcvalue = key_calc(word,word_set)
    if word not in word_set[calcvalue]:
        word_set[calcvalue].append(word)
    if is_full(word_set) == True:
        word_set = double(word_set)
    return word_set


def to_file_unique(word_set,write_path): # writing to file for viusals

    ss = open(write_path, "w",encoding='utf-8')
    for i in range(len(word_set)): # basicly same as string
        for j in word_set[i]:
                ss.write(j) 
                ss.write("\n")
    ss.close
