# A binary search based dictionary implementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child
KEY, VALUE, LEFT, RIGHT = 0, 1, 2, 3    # Because root[KEY] looks better than root[0]

# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None, None, None, None]

# Add a new key-value pair to table if the key doesn't already exist.
# Update value if already key exists in the table.
def add(root,key,value):
    if root[KEY] == None:    # If node has no key, then add our key and value pair to it (mainly used on a fresh BST with nothing inside it)
        root[KEY] = key
        root[VALUE] = value
        return root
    elif root[KEY] == key:   # If node is our key, then change value
        root[VALUE] = value
        return root
    elif key < root[KEY]:    # If key is smaller than the node's key, then go left
        node = root[LEFT]
        if node == None:
            node = new_empty_root()
            node[KEY] = key
            node[VALUE] = value
            root[LEFT] = node
            return root
        else:
            return add(node, key, value)
    elif key > root[KEY]:      # If key is smaller than the node's key, then go right
        node = root[RIGHT]
        if node == None:   
            node = new_empty_root()
            node[KEY] = key
            node[VALUE] = value
            root[RIGHT] = node
            return root
        else:
            return add(node, key, value)
    
# Returns a string representation of the table content.
# That is, all key-value pairs
def to_string(node):
    global TO_STRING_FIRST   

    first = False     # We want to add curly brackets only on the very first function
    try:
        if TO_STRING_FIRST == False:
            pass
    except NameError:
        first = True
        TO_STRING_FIRST = False
    
    treestring = f" ({node[KEY]},{node[VALUE]})"

    leftnode, rightnode = node[LEFT], node[RIGHT]     # Keep running same function if path continues
    if node[LEFT] != None:
        treestring += to_string(leftnode)
    if node[RIGHT] != None:
        treestring += to_string(rightnode)

    if first:
        treestring = "{" + treestring + " }"
        del TO_STRING_FIRST

    return treestring


# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    # Where final returns happen
    if node == None:
        return None
    elif node[KEY] == key:
        return node[VALUE]
    elif node[KEY] == None:
        return None 

    # Where the recursion happens
    leftnode, rightnode = node[LEFT], node[RIGHT]
    if key < node[KEY]:
        getleft = get(leftnode, key)
        if getleft != None:
            return getleft   
    else:
        getright = get(rightnode, key)
        if getright != None:
            return getright
        


# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):
    count = 0

    leftnode, rightnode = node[LEFT], node[RIGHT]

    # Node has 3 conditions: 2 children, 1 child or no children.
    if node[LEFT] != None and node[RIGHT] != None:
        count += 1
        depthleft, depthright = max_depth(leftnode), max_depth(rightnode)  # To make sure we don't run the same function more than once we store result in variable
        if depthleft > depthright:
            count += depthleft
        else:
            count += depthright
    elif node[LEFT] == None and node[RIGHT] == None:
        return 1
    else:
        if node[LEFT] != None:
            count += 1
            count += max_depth(leftnode)
        else:
            count += 1
            count += max_depth(rightnode)

    return count


# Returns the number of key-value pairs currently stored in the table
def count(node):
    num = 1

    # Pretty simple, if it branches left, go left, if it branches right, also go right, return 1 for every travel
    leftnode, rightnode = node[LEFT], node[RIGHT]
    if node[LEFT] != None:
        num += count(leftnode)
    if node[RIGHT] != None:
        num += count(rightnode)

    return num

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
def get_all_pairs(root):
    global ALL_PAIRS_FIRST   # Same trick as to_string()

    first = False
    try:
        if ALL_PAIRS_FIRST == False:
            pass
    except NameError:
        first = True
        ALL_PAIRS_FIRST = False

    lst = [(root[KEY], root[VALUE])]

    # Uses same code as count()
    leftnode, rightnode = root[LEFT], root[RIGHT]
    if root[LEFT] != None:
        lst += get_all_pairs(leftnode)
    if root[RIGHT] != None:
        lst += get_all_pairs(rightnode)

    # At the very end, sorts by alphabetical order of key
    if first:
        lst.sort(key = lambda x: x[0])
        del ALL_PAIRS_FIRST

    return lst