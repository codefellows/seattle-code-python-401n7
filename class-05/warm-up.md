Exercise 1:

Write a function that calculates the sum of all numbers from 1 to n, where n is a positive integer. What is the time complexity of this function?

```python
def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
```

Exercise 2:

Write a function that finds the maximum element in a given list. What is the time complexity of this function?

```python
def find_max(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element
    
```

Exercise 3:

Write a function that takes two lists as input and returns a list containing their intersection (common elements). What are the time and space complexity of this function?

```python
def list_intersection(lst1, lst2):
    common_elements = []
    for element in lst1:
        if element in lst2:
            common_elements.append(element)
    return common_elements
    
```    
    
Exercise 4:

Write a function that takes a list of integers and returns the number of pairs that add up to a given target. What are the time and space complexity of this function?

```python
def count_pairs_with_sum(lst, target):
    pairs = 0
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs += 1
        seen.add(num)
    return pairs
    
```    
    
Exercise 5:

Write a function that checks if a given word is a palindrome. What is the time complexity of this function?

```python
def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
    
```    
