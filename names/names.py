import time
import re

from binary_search import BinarySearchTree

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
search_tree = BinarySearchTree()

for name in names_1:
    search_tree.insert(name)

for name in names_2:
    found = search_tree.lookup(name)
    if found:
        duplicates.append(found)

end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
