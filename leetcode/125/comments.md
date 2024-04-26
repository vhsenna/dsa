# Valid Palindrome

A sentence is considered a palindrome if, after converting all characters to lowercase and removing non-alphanumeric characters, it reads the same forwards and backwards.

Alphanumeric characters include letters and numbers.

Return `true` if the sentence is a palindrome; otherwise, return `false`.

---

Firstly, preprocess the given sentence with the following steps:

- Convert the entire sentence to lowercase.
- Remove all non-alphanumeric characters.

Then, we'll create two pointers.

The first pointer (`p1`) will start at the beginning of the sentence (index 0).

The second pointer (`p2`) will start at the end of the sentence (last index).

Iterate through the sentence using a loop until reaching the middle point.

- If `p1` is equal to `p2`, increment `p1` and decrement `p2`.
- If at any point `p1` is not equal to `p2`, exit the loop and return `false`.

The loop will terminate once the pointers meet at the middle of the sentence. If the loop completes without finding any mismatches, return `true`.
