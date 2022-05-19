import table as tbl

pathR = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part4\\treetests\\mushroom2.0.txt"
pathW = "C:\\Users\\Atakan.ATAKAN\\Desktop\\School\\pyth0n_c0urs3s\\1DV501\\mini_project\\team-2\\part4\\treetests\\tree"   # Enter size number and .txt after choosing size e.g. tree1000.txt

lstsize = [200]      # Enter wanted BST size(s)
with open(pathR) as file:

    for size in lstsize:
        root = tbl.new_empty_root()
        count = 0
        for line in file:
            if count == size:    # Stops once desired size is reached
                break
            tempstr = line.replace("\n", "")
            tbl.add(root, tempstr, 1)
            count += 1
        path = pathW + str(size) + ".txt"
        with open(path, "w", encoding="utf-8") as txtpath:
            txtpath.write( str(root) )
    
        
        
