Exercise 1

- The time complexity of the function sum_numbers(n) is O(n). This is because there is a single loop iterating over n elements, and the total number of operations scales linearly with the input size n.

Exercise 2

- The time complexity of the function find_max(lst) is O(n), where n is the length of the list. The function iterates through the list once, with the number of operations scaling linearly with the input size n.

Exercise 3

- The time complexity of the function list_intersection(lst1, lst2) is O(n*m), where n is the length of lst1 and m is the length of lst2. This is because, for each element in lst1, the function checks if it is in lst2, which takes O(m) time. The space complexity is O(min(n, m)) in the worst case, as the resulting list could contain all elements of the smaller input list.

Exercise 4

- The time complexity of the function count_pairs_with_sum(lst, target) is O(n), where n is the length of the list. The function iterates through the list once, and the operations inside the loop take constant time. The space complexity is O(n), as the set seen could store all elements of the list.

Exercise 5

- The time complexity of the function is_palindrome(word) is O(n), where n is the length of the word. The function iterates through half of the word's characters, comparing them in pairs, so the number of operations scales linearly with the input size n.
