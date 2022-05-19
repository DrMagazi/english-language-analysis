import matplotlib.pyplot as plt

# Graph data
words_amount_lst = [100,200,500,1000,5000,10000,20000,40000,80000]
time_lst = [159.21, 212.41, 246.21, 262.61, 388.8, 382.20, 398.92, 390, 396.20]
depth_lst= [21,33,52,55,63,67,71,74,80]


# Make graph
fig, (time, depth) = plt.subplots(1, 2)
time.plot(words_amount_lst, time_lst)
time.set_xlabel("Tree Size (number of nodes)")
time.set_ylabel("Time (milliseconds)")
time.set_title("Time it takes to get 20k words from BST") # dr fix this
depth.plot(words_amount_lst, depth_lst)
depth.set_xlabel("Tree Size (number of nodes)")
depth.set_ylabel("Depth (from root node to deepest leaf)")
depth.set_title("Relation between tree size and maximum depth")

plt.show()