import table

KEY, VALUE, LEFT, RIGHT = 0, 1, 2, 3

path = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part1\\textfiles\\holy_words.txt"

# Add all words to binary search tree
root = table.new_empty_root()
with open(path, encoding="utf-8") as file:
    loadbar = 0
    for line in file:
        line = line.replace("\n", "")   # Gets rid of line breaks
        tempstr = line
        if len(tempstr) > 4:    # Better to have this if statement early so we don't run functions unnecessarily
            frequency = table.get(root, tempstr)
            if frequency != None:
                table.add(root, tempstr, (frequency + 1))  # Counts frequency
            else:
                table.add(root, tempstr, 1)
            
        # Loading bar
        loadbar += 1
        print("I am on line", loadbar)

def get_all_pairs(root):    # Modified version of the table.py function, this one sorts values instead of keys and descending instead of ascending.
    global ALL_PAIRS_FIRST

    first = False
    try:
        if ALL_PAIRS_FIRST == False:
            pass
    except NameError:
        first = True
        ALL_PAIRS_FIRST = False

    lst = [(root[KEY], root[VALUE])]


    leftnode, rightnode = root[LEFT], root[RIGHT]
    if root[LEFT] != None:
        lst += get_all_pairs(leftnode)
    if root[RIGHT] != None:
        lst += get_all_pairs(rightnode)

    if first:
        lst.sort(key = lambda x: x[1], reverse = True)
        del ALL_PAIRS_FIRST

    return lst

# Convert BST to normal python list
data = get_all_pairs(root)

# Calculate top 10 most frequent words
top10 = []
count = 0
for t in data:
    if count < 10:
        temptpl = (t[0], t[1])
        top10.append(temptpl)
        count += 1
    else:
        break

# Output
print("The top 10 most frequently used words with length > 4:\n")
number = 1
for t in top10:
    word, freq = t
    print(number, ". ", word, ": ", freq, sep="")
    number += 1

# holy_words
# The top 10 most frequent words with length > 4:

#  1. arthur: 261
#  2. launcelot: 102
#  3. knight: 84
#  4. galahad: 81
#  5. father: 76
#  6. bedevere: 68
#  7. knights: 65
#  8. guard: 58
#  9. robin: 58
#  10. right: 57

# eng_news_words
# The top 10 most frequently used words with length > 4:

#  1. their: 6146
#  2. about: 4612
#  3. there: 3945
#  4. would: 3878
#  5. people: 3810
#  6. which: 3580
#  7. after: 3018
#  8. first: 2891
#  9. years: 2823
#  10. other: 2749