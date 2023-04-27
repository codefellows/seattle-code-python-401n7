# Warm-up Exercise: Big O Analysis

In this exercise, you will analyze the time and space complexity of the following functions and methods using Big O notation. The problems start relatively easy and then increase in difficulty.

1. Function: sum_of_elements

```python
def sum_of_elements(arr):
    """
    Calculate the sum of elements in the given list.

    :param arr: List of integers
    :return: The sum of all elements in the list
    """
    total = 0
    for num in arr:
        total += num
    return total
```

2. Function: nested_sum

```python
def nested_sum(nested_arr):
    """
    Calculate the sum of all elements in a nested list of integers.

    :param nested_arr: Nested list of integers
    :return: Sum of all elements in the nested list
    """
    total = 0
    for inner_arr in nested_arr:
        for num in inner_arr:
            total += num
    return total
```

3. Function: cartesian_product

```python
def cartesian_product(arr1, arr2):
    """
    Calculate the Cartesian product of two lists.

    :param arr1: First list of integers
    :param arr2: Second list of integers
    :return: List of tuples representing the Cartesian product of the two input lists
    """
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            result.append((arr1[i], arr2[j]))
    return result
```

4. Function: has_pair_with_sum

```python
def has_pair_with_sum(arr, target):
    """
    Check if the given list has a pair of elements that sum up to the target.

    :param arr: List of integers
    :param target: Target integer
    :return: True if a pair of elements with the target sum exists, False otherwise
    """
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False
```

5. Class & Method: WordCounter (analyze the count_words method)

```python
class WordCounter:
    def __init__(self):
        """
        Initialize an instance of the WordCounter class.
        """
        self.word_freq = {}

    def count_words(self, words):
        """
        Count the frequency of each word in the given list of strings.

        :param words: List of strings
        """
        for word in words:
            word = word.lower()
            if word in self.word_freq:
                self.word_freq[word] += 1
            else:
                self.word_freq[word] = 1

    def get_word_freq(self):
        """
        Get the word frequencies.

        :return: Dictionary with the frequency of each word
        """
        return self.word_freq
```

For each function or method, analyze both the time and space complexity using Big O notation.
