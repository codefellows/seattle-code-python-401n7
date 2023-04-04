# Guide for Big O Time Complexity Analysis

1. Identify the input size: Determine the variable(s) that represent the input size. In most cases, this is the length of a list, the number of elements, or the size of an integer.

1. Analyze loops: Analyze the loops in the code and their relationship with the input size. If there is a single loop iterating over the input, the time complexity is likely O(n). For nested loops, multiply the complexity of the outer loop with the complexity of the inner loop.

1. Consider the worst case: When analyzing time complexity, consider the worst-case scenario. This is the situation where the algorithm performs the maximum number of operations.

1. Focus on the dominant term: As input sizes grow, the term with the highest degree of growth dominates the complexity. For example, if you have a function with a time complexity of O(n^2 + n), the dominant term is n^2, so the complexity is considered O(n^2).

1. Constant factors don't matter: In Big O notation, constant factors are not considered. This means that O(2n) and O(n) are equivalent, as they both represent linear growth.

1. Analyze operations within loops: Consider the operations within loops or recursive calls. If the operations take constant time, they won't affect the overall complexity. However, if the operations have their complexity, you need to consider their impact on the overall time complexity.

## Common "gotchas" for time complexity

- Misidentifying the input size.
- Incorrectly estimating the complexity of nested loops or recursive calls.
- Not considering the worst-case scenario.

## Guide for Big O Space Complexity Analysis

1. Identify the input size: Determine the variable(s) that represent the input size, similar to the time complexity analysis.

1. Analyze data structures: Examine the data structures used in the algorithm and their relationship with the input size. The space complexity is determined by the amount of additional memory the algorithm requires as the input size grows.

1. Consider the worst case: When analyzing space complexity, consider the worst-case scenario, similar to the time complexity analysis. This is the situation where the algorithm uses the maximum amount of memory.

1. Focus on the dominant term: As input sizes grow, the term with the highest degree of growth dominates the complexity, similar to the time complexity analysis.

1. Constant factors don't matter: In Big O notation, constant factors are not considered for space complexity, just like in time complexity analysis.

1. Analyze space within loops or recursive calls: Consider the memory used within loops or recursive calls. If the memory usage is constant or has its complexity, consider its impact on the overall space complexity.

## Common "gotchas" for space complexity

- Overlooking the memory usage of data structures.
- Not considering the worst-case scenario.
- Misidentifying the input size.

## Similarities between time and space complexity analysis

- Both analyses involve identifying the input size and considering the worst-case scenario.
- In both cases, the focus is on the dominant term, and constant factors are not considered.

## Differences between time and space complexity analysis

- Time complexity analysis focuses on the number of operations performed, while space complexity analysis focuses on the amount of memory used.
- Time complexity analysis often involves analyzing loops and operations within loops, while space complexity analysis focuses on the memory used by data structures and within loops or recursive calls.
