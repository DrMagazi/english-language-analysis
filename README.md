# English language analysis using various data structures in Python
## Abstract
This is a project I worked on after learning programming for the first time using Python.

By the end of the 2+ month
course, we were given a couple of weeks to create Python programs that would read files containing the script for
Monty Python and the Holy Grail and also 100k sentences from English news. The data was processed to separate words
in order to gather some statistics such as which words were most common, how long words were, etc... To allow efficient
processing of the information our implementations of various data structures, mainly **binary search trees** and 
**hashing tables** were used.

I'd like to point out that this project was designed by students with no previous programming experience and therefore
may not be easily usable. I have included below the report from the project so that the findings can be read.
All the Python programs are, of course, also included and may be examined. I wish to come back and rework this later
so that it may be run by others easily and to improve the overall quality.

## Introduction  
Text analysis through the use of very efficient custom classes, supported by graphed data - our mini project. 
Here at this endpoint of our month long struggle and challenge, metaphorized symbolically in the shape of entities 
like "teamwork", we will discuss our experiences, results, and newfound wisdom we hope to carry in our brains for 
the rest of our programming carreers. Although many of what we have found may be considered "fun facts" at 
most, our process in finding them, and exploring the tools that enabled us to do so will hopefully fulfil 
you, the readers' curiosity.


## Part 1: Divide text into words
- If a word is only one letter long, only "A", "a" and "I" are accepted, and others are not included as they are likely abbreviations for names. Although it is still likely for our accepted letters to also be abbreviations, it is likelier that they are proper words, and therefore we have decided it is the best case scenario to include them. For words that are longer than 1 letter, our definition for a word is any string including a series of English letters a-z or A-Z, with the exception of apostrophes ( ' ) and dashes ( - ) provided that they are sandwiched between English letters, and not at the beginning or start of the word. However, if multiple apostrophes or dashes are present between a word (which is a gramatical mistake by the author of the text) it fixes that by simply including only the last one in the series.
```py
# Don't, Don''''t, Don''-'t and even 'Don't' will all have the same output:
"Don't"

# hi'-five and hi-'five will give different outputs respectively:
"hi-five", "hi'five"
```
- The beginning of the code in dr_words.py introduces 2 variables: ``lst`` (an empty list) and ``tempstr`` (an empty string). By iterating over every individual letter of the text, if the character being iterated over is a letter "A-Z" or "a-z", the code concatenates the letter to the end of the string, ``tempstr``. Once the iteration reaches a non-letter, the string ``tempstr`` is appended to ``lst``, which stores all individual words, and the code resets ``tempstr`` back to an empty string so it is ready for use again. Since we do ``not`` want the code to append tempstr if it is empty or if it is a 1 letter word that isn't "A", "a" or "I", once the code arrives at a non-letter in it's iteration, it appends ``tempstr`` to ``lst`` only:
```py
if len(tempstr) > 1 or tempstr == "A" or tempstr == "a" or tempstr == "I"
```
- An important exception in the code is the aforementioned inclusion of apostrophes or dashes in certain situations. if the ``len(tempstr) > 0`` and the character being iterated over is an apostrophe or dash, then the character is assigned to a variable ``pendltr`` and the variable ``Trial`` which at the beginning of the code was assigned the boolean statement ``False`` is now assigned ``True``, as the trial period for whether this character will be included in the word has begun. Now we are split into 3 cases from here. If the next character being iterated over is:
	1. a letter "A-Z" or "a-z", ``pendltr`` is concatenated to the end of ``tempstr`` and then the letter that is currently being iterated over is concatenated after that. This has made sure that there is a proper English letter both before **and** after the apostrophe or dash. ``Trial`` is assigned ``False``
	2. another apostrophe or dash, ``pendltr`` is replaced with the current apostrophe or dash and the trial period continues.
	3. any other character, then ``pendltr`` is **not** concatenated to the end of ``tempstr``. The trial ends with ``Trial`` being assigned ``False`` and ``tempstr`` is appended to ``lst`` without the apostrophe or dash added to it.
- Lastly, once the iteration has finished, if ``tempstr`` isn't an empty string, it is appended to ``lst`` one last time. 
```py
if len(tempstr) > 0:
    lst.append(tempstr)
```
- Word count for the two files 1) ``holy_grail.txt`` (Grail), 2) ``eng_news_100K-sentences.txt`` (news_100k)
```py
# English_news text has:
# 1937398 words, of which 87841 are unique

# Holy_Grail text has:
# 11008 words of which 1863 are unique
```

## Part 2: Implementing data structures

For part 2, our focus was required sustainably to fuel with optimized code the 2 most important programs in this project: `table.py` and `word_set.py`. After learning the concepts of hashing and binary search trees, our mission in these 2 ruthless programmes were to provide them with code that would allow any user to, humbly said, create fire and bend water to their desire. To summarize, both files contain codes for basic funtions such as adding, removing, retrieving and displaying data in multiple forms.

## <span style="color:blue">**wordset.py**</span>
The ``add`` function is simply put, looking for a word in a specific list and if that word does not exist it adds it to that list. To know what list the function should look in we use ``key_calc``. ``key_calc`` needs the word and the whole ``word_set`` to calculate the correct list, it takes the sum of the ASC11 value of the word mod the length of the wordset and that's the list the word belongs to. The reason why the add function lacks any way to check if the ``word_set`` is close to full and has no way to increase the set size is because i have another function that includes those but it made the program to slow to work on large files like
``eng_news_100K-sentences.txt``. ``add_with_full`` has ways to check if the word set is getting full and if it is full the ``double`` function makes a new larger wordset and rehashes the words to the correct place. The problem we had with this approach was that every time the program adds a word it has to check every list to see if its getting close to full, slowing the program down. That's why for bigger files we needed a variable that keeps track of the amount of words added and when that variable gets close to the size of the set we simply call the ``double`` function and rehase.

For ``word_set_main.py`` we needed to make some changes we needed to use the ``add_with_full`` function to make use of doubling the set and rehashing, I also needed to set ``word_set = ws.add_with_full(word_set,s)`` for the simple reason that the program returns the whole set.
I think the biggest diffrence when it comes to result is that our max bucket size is three while it supposed to be two. We havent figured out why and at first we thought something was wrong with the rehashing system but according to the ``key_calc`` all names are in their right place. 
306 max_bucket_size for ``eng_news_100K-sentences.txt`` 
17 max_bucket_size for ``holy_grail.txt``

## <span style="color:blue">**table.py**</span>
Due to its use of recursion, the add() function starts off by checking the current node it is at. If the node has no key, it adds the input key and value to the node. This is because this means it has travelled all the way down, and has not found the duplicate key. If the node's key is the same as the input key, then the value is updated to the input value. In the beginning of the file, the numbers 0-3 have been assigned to their corresponding node attribute, which is why the code has writing like `root[KEY]` instead of `root[0]`
```py
if root[KEY] == None: 
	root[KEY] = key
	root[VALUE] = value
	return root
elif root[KEY] == key:
	root[VALUE] = value
	return root
```
If neither condition has been met, meaning we have not found a duplicate, or gotten to the end of the BST, then it is time to continue, thus the recursion starts. If the input key is smaller than the node's key (meaning it comes before it alphabetically), then the code shifts its focus to the left node
```py
elif key < root[KEY]:    # If key is smaller than the node's key, then go left
    node = root[LEFT]
```
If the node is None, then it creates a new empty node there with the input key and value, otherwise, it runs the add() function again on that node. Same code applies for if the key was bigger than the current node.

For max_depth(node), the code begins with assigning the variable _count_ to 0. From there we have 3 if conditions. 
1. If the current node has no children at all, then it returns 1, so that it can be added to the count.
2. If the current node only has 1 child, then 1 is added to the count, and max_depth() for whichever node exists is run and also added to the count
3. If the current node has 2 children, then 1 is added to the count and max_depth() is executed for both nodes. Whichever returns a higher value is then also added to the count.

There were no differences between the table_main.py expected output and my output other than the to_string() function's order of key, value pairs. This is fine because it isn't meant to have any specific order anyway, and in get_all_pairs() where order does matter, the results are the same.

Tree depths:
```py
# Holy_Grail: 25 depth
# English_News: 44 depth
```

## Part 3: Word related exercises

## 3.1
For finding the amount of unique words in a textfile. We checked everything the word_set contains, since it shouldnt contain any duplicates. We just had a for loop looping over all lists in the set and another for loop checking all list within the set.  
```py
def unique_words(word_set): # Saad unique words
    count = 0
    for i in range(len(word_set)):
        for j in word_set[i]:
            count += 1
    return count
```
English_news text: 87841 unique words
Holy_Grail text: 1863 unique words
 

## 3.2
For this part of the project, we simply iterated over the words again in the textfiles that had our preprocessed words, to determine how long they are, count how many of each length has occured and make a histogram for them. Since we had textfiles that already had one word per line seperated all we had to do was assign the word to the line we are currently on in the iteration (with line breaks `("\n")` removed) but also iterate over each letter of the word to make sure we don't count apostrophes or dashes as a letter for the length. once the length of the word was counted, it was added to a binary search tree with its length as its key, and frequency of occurence as its value. For each word, the code had to run the get() function first to see if the key is already there, so if it returned none, it added the key with a value of 1, and if the key already existed, it added 1 to it's value. 
### Holy Grail
<img src="https://imgur.com/62ZmQQl" width="400"/>

### English News
<img src="https://imgur.com/n9KIOah" width="400"/>


## 3.3
Here in the project, we were supposed to find the 10 most frequently occuring words (with atleast 5 letters) in each text file. We used similar code to part 3.2, but instead of the word's length, we added the word itself as the key to the trees and only if it's length was > 4. Once that was complete, we used a modified version of get_all_pairs() function to create a list of the tree and sort by descending value rather than ascending key. From there we had a function iterate over the first 10 key-value pairs of the list, and print them to present to us which words occured the most. 

<img src="https://imgur.com/PSUzzm9" width="400"/>
<img src="https://imgur.com/Pe3AeKY" width="400"/>

## Part 4: Measuring time

## 4.1
We first had a python programme iterate (line by line) through our text file `english_words.txt` which contains all words (one per line). For every word it was on, the code randomized a number between 1-9, and if the number was 5, it would grab that word and add it to a list. For every iteration, the code would check if the length of the list is bigger than or equal to 20k, in which case it would break the loop.
```py
lst = []
for line in file:
	if len(lst) >= 20000:
		break
	tempstr = line.replace("\n", "")
	rnd = randint(1,10)
	if rnd == 5:
		lst.append(tempstr)
```
After that, the code printed every word in the list onto another textfile `20k_random_words.txt`, one word per line. Once that was done, we had another python file, `createBSTs.py` generate a BST with any size (number of nodes), depending on input, using the words from the processed english news textfile `english_words.txt`. The code used functions from table.py to iterate over each word and add it to a binary search tree and stopped once the desired size was reached. Using this code we make trees of sizes: 100, 200, 500, 1000, 5000, 10000, 20000, 40000, 80000. Initially we did not have trees of sizes 200 and 500, but after realizing that the biggest differences for our experiments happened in the lower sized trees, we decided to create those too and use them for the experiment. After that we had two last python files: `4.1_time.py` and `4.1_depth.py`. The latter simply measured the maximum depth of each tree and gave us the results. The `4.1_time.py` file, however, used the `get()` function from `table.py` to search the preselected 20k words for any given tree, and timed its result using the time module.

<img src="https://imgur.com/Dq5R6ct" width="400"/>

The results were exactly as expected. The speed at which the depth of the tree grew as the size got bigger, rapidly decreased, which is the reason binary search trees are so efficient at storing huge amounts of data. The graph for the time to retrieve 20k words had the exact same signature of rapidly declining as the size grew. This is because the time to search is directly correlated with the maximum depth, as maximum depth also means how far the code will have to travel in the worst case scenario to grab data from it.

## 4.2
For measuring time in the hashing system we used five files containing 1000, 2000, 3000, 4000 and 5000 words. We measured the time it took for the program to hase everything out and then we took the average of 5 tries. With the average time we could calculate the average amount of words per second for each file. We put that in a graph and there is a clear curve, showing that the programs words/sec slows down alot for larger files, as is expected. For max buckets size it was a slow increase, it is the most likely outcome but it there could be situations where the bucket size decreases with bigger files.  

<img src="https://imgur.com/KBYSlJQ" width="400"/>
<img src="https://imgur.com/iFW9lRO" width="400"/>

# Project conclusions and lessons learned
## Technical issues 

### Learning git and mathplotlib with anaconda. 

One of the first hurdles we faced was learning git, how to push and pull files. 
We did not fully understand it for a while and it caused some issues with file management. 
We also had some problems with using mathplotlib library. It required some uninstalling and 
reinstalling of programs and eventually we realized there was something wrong with the virtual 
environment that VSC was using (Anaconda). 

### Hashing improvements

Our hashing right now has problems with speed and it creates too many empty lists when it comes 
to larger files. We think the speed could be improved and the problems with empty lists could 
be fixed by only keeping track when a unique word enters the set instead of when any word enters 
the set. You could also consider using linear probing. Our first instinct told us that the program 
would become slower since with such a large file and many words clustered around the same lists, 
the program would have to search thousands of lists for an open address. 

### Teaching each other

Since we had our own specialties in our project, we didn't realise how difficult it would be to 
teach eachother our own code. We realised not too soon after running into this problem that the 
best solution was to describe the basics of the concepts behind our code (rather than going into 
a lot of detail), and to let eachother go over our codes in our own time, to which we could answer 
questions later, if we had any.

### Other improvements

Although the pressure got pretty intense to finish the project as we were reaching the end, we were able to finish it mostly how we wanted to. We don't think we needed any more time to finish the project, but rather if we were more organized, we could have been much more time efficient and clear with our process.
