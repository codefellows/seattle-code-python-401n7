# Warm Up Class 38

For today's warm-up, we will be practicing the "Forward Backward Method" for developing algorithms. You can find the guide [here](https://codefellows.github.io/common_curriculum/challenges/code/forward_backward). Below are some excerpts from Solow's book, "How to Read and Do Proof's" which provides a mathematically rigorous explanation of the Forward Backward Method.

## Summary of Forward Backward Method - Solow

To use the forward-backward method for proving that “A implies B,” begin
with the statement B that you are trying to conclude is true. Through the
backward process of asking and answering the key question, derive a new
statement, B1, with the property that, if B1 is true, then so is B. All efforts
are now directed toward establishing that B1 is true. To that end, apply the
backward process to B1, obtaining a new statement, B2, with the property
that, if B2 is true, then so is B1 (and hence B). The backward process
is motivated by the fact that A is assumed to be true. Continue working
backward until either you obtain the statement A (in which case the proof is
finished) or you can no longer pose and/or answer the key question fruitfully.
In the latter case, it is time to start the forward process, in which you derive a
sequence of statements from A that are necessarily true as a result of assuming
that A is true. Remember that the goal of the forward process is to obtain
precisely the last statement you have in the backward process, at which time
the proof is complete.

These two processes are easily remembered by thinking of the statement B
as a needle in a haystack. When you work forward from the assumption that
A is true, you start somewhere on the outside of the haystack and try to find
the needle. In the backward process, you start at the needle and try to work
your way out of the haystack toward the statement A.

## The Backward Process - Solow

In the backward process you begin by asking, “How can I conclude that the statement B is true? The question obtained from statement B in such problems is referred to here as the key question. Once you have posed the key question, the next step in the backward process is to provide an answer.

The process of asking the key question, providing an abstract answer, and then applying that answer to the specific problem constitutes one step of the backward process.

## The Forward Process - Solow

The forward process involves deriving from the statement A, which you assume is true, some other statement, A1, that you know is true as a result of A being true. Statements are directed toward linking up with the last statement obtained in the backward process.

## Instructions

Open a new doc. Follow the guide and fill in the intermediate steps for the following problems. The number of steps in the middle are up to you:

**Problem 1: Calculate the sum of all elements in a list**

**Forward/Backward Process:**
- **A:** A list of numbers [1, 2, 3, 4, 5]
-
-
-
- **B:** The sum of all numbers in the list is 15

**Problem 2: Determine if a word is a palindrome**

**Forward/Backward Process:**
- **A:** A string "radar"
-
-
-
- **B:** The string "radar" is a palindrome (True)

**Problem 3: Find the maximum number in a list**

**Forward/Backward Process:**
- **A:** A list of numbers [1, 2, 3, 4, 5]
-
-
-
- **B:** The maximum number in the list is 5
