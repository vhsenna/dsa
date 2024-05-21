# People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What
# are the downsides of an array for inserts? In particular, suppose you're using binary search to search for logins.
# What happens when you add new users to an array?

# Inserting into arrays is slow. Also, if you're using binary search to search for usernames, the array needs to be
# sorted. Suppose someone named Adit B signs up for Facebook. Their name will be inserted at the end of the array. So
# you need to sort the array every time a name is inserted!
