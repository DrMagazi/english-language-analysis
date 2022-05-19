import table as tbl

path = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part1\\textfiles\\english_words.txt"

root = tbl.new_empty_root()
with open(path) as file:
    count = 0
    for line in file:
        count += 1
        print(count)
        word = line.replace("\n", "")
        tbl.add(root, word, 1)
    print( tbl.max_depth(root) )

# Holy_Grail: 25 depth
# English_News: 44 depth
