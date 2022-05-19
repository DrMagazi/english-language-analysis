import table
import matplotlib.pyplot as plt

path = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part1\\textfiles\\english_words.txt"

root = table.new_empty_root()
with open(path, encoding="utf-8") as file:
    for line in file:
        tempstr = line.replace("\n", "")
        length = 0
        for letter in tempstr:
            if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:   # We don't want to count apostrophes as letters
                length += 1

        nodevalue = table.get(root, length)
        if nodevalue != None:
            table.add(root, length, (nodevalue + 1))
        else:
            table.add(root, length, 1)

        length = 0

data = table.get_all_pairs(root)

len_lst = []
freq_lst = []
for e in data:
    strlen, lenfreq = e
    if strlen <= 17:
        len_lst.append(strlen)
        freq_lst.append(lenfreq)

plt.bar(len_lst, freq_lst)
plt.xticks(range(1,18), len_lst)
plt.title("Frequency of words with length 1 to 17")
plt.xlabel("Length of word")
plt.ylabel("Frequency of occurrence")
plt.show()
