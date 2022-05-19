import os

def read_compute(path):
    lst = []
    tempstr = ""
    trial = False
    with open(path, encoding="utf-8") as file:
        file = file.read().lower()    # Converts file into readable string and all lowercase
        for n in file:
            if 65 <= ord(n) <= 90 or 97 <= ord(n) <= 122:
                if trial:
                    tempstr += pendltr
                tempstr += str(n)
                trial = False
            elif (n == "'" or n == "-" or n == "’") and len(tempstr) > 0:        # These are only included inbetween words
                if n == "’":       # Turns weird apostrophe into a normal one
                    pendltr = "'"
                else:
                    pendltr = str(n)
                trial = True         # Puts character into trial period so we can see if there are any English letters after it before we add it
            else:
                if len(tempstr) > 1 or tempstr == "A" or tempstr == "a" or tempstr == "I":  # Only include these 1 letter words
                    lst.append(tempstr)
                tempstr = ""
                trial = False
        if len(tempstr) > 0:
            lst.append(tempstr)
    return lst




def write_file(lst, file_path): # writer works atleast 1 word 1 line
    wfile = open(file_path,"w", encoding='utf-8')
    for elem in lst:
        wfile.write(elem+"\n")
    wfile.close()
    return "done"


sd = read_compute('C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part1\\textfiles\\eng_news_100K-sentences.txt')
ss = write_file(sd, ('C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part1\\textfiles\\english_words.txt'))
write_file(sd, ss)




