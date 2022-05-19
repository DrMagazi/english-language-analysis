from random import randint

pathR = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part1\\textfiles\\english_words.txt"
pathW = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part4\\treetests\\20k_random_words.txt"

with open(pathR, encoding="utf8") as file:
    lst = []
    for line in file:
        if len(lst) >= 20000:
            break
        tempstr = line.replace("\n", "")
        rnd = randint(1,10)
        if rnd == 5:
            lst.append(tempstr)

with open(pathW, "w") as file:
    for w in lst:
        file.write(w)