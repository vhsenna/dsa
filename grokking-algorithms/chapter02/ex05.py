# In reality, Facebook uses neither an array nor a linked list to store user information. Let's consider a hybrid data
# structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example,
# the first slot in the array points to a linked list containing all the usernames starting with A. The second slot
# points to a linked list containing all the usernames starting with B, and so on.
# Suppose Adit B signs up for Facebook, and you want to add them to the list. You go to slot 1 in the array, go to the
# linked list for slot 1, and add Adit B at the end. Now, suppose you want to search for Zakhir H. You go to slot 26,
# which points to a linked list of all the Z names. Then you search through that list to find Zakhir H. Compare this
# hybrid data structure to arrays and linked lists. Is it slower or faster than each for searching and inserting? You
# don't have to give big O run times, just whether the new data structure would be faster or slower.

# Searching—slower than arrays, faster than linked lists. Inserting—faster than arrays, same amount of time as linked
# lists. So it's slower for searching than an array, but faster or the same as linked lists for everything. We'll talk
# about another hybrid data structure called a hash table later in the book. This should give you an idea of how you
# can build up more complex data structures from simple ones. So what does Facebook really use? It probably uses a
# dozen different databases with different data structures behind them: hash tables, B-trees, and others. Arrays and
# linked lists are the building blocks for these more complex data structures.
