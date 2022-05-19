import time, table

# Create list with 20k sample keys
pathLST = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part4\\treetests\\20k_random_words.txt"
lst = []
with open(pathLST) as file:
    count = 0
    for line in file:
        tempstr = line.replace("\n", "")
        lst.append(tempstr)
        count += 1
        print(count)

# Search tree for each item in lst
root = 

start = time.time()
for word in lst:
    table.get(root, word)
stop = time.time()
totaltime = stop - start
print(totaltime)
# Results
# 100: 0.15921058654785
# 200: 0.21241216659546
# 500: 0.24620547294617
# 1000: 0.26260924339294
# 5000: 0.38879547119141
# 10000: 0.38220109939575
# 20000: 0.39892339706421
# 40000: 0.39099941253662
# 80000: 0.39619970321655