# Programming excercises level intermediate

This collection of exercises is designed to provide an intermediate approach to programming, addressing basic concepts of data structures and algorithms. Whether you're advancing from basic programming concepts or looking to consolidate your understanding in these key topics.

## Table of contents of excercises

- [Data-Structures](#data-structures).
  - [Stacks](#stacks).
  - [Queues](#queues).
  - [Sets](#sets).
  - [Linked-Lists](#linked-lists).
  - [Graphs](#graphs).

## Data-Structures

In this section, you will face challenges related to data types and data structures. These exercises are designed to consolidate your basic understanding of these structures.

### Stacks

1. **Stack Implementation**:
    - Description: Implement a stack from scratch with basic `push` and `pop` operations. Make sure to include functions for checking if the stack is empty `(isEmpty())` and getting the size of the stack `(size())`.

### Queues

1. **Queue Implementation**:
    - Description: Implement a basic queue with `enqueue` and `dequeue` operations. Perform a sequence of enqueue and dequeue operations and display the resulting queue.

### Sets

1. **Unique Elements in a List:**
   - *Description:* Write a function to return a set containing unique elements from a given list.
   - *Example Input:* `[1, 2, 2, 3, 4, 4, 5]`
   - *Example Output:* `{1, 2, 3, 4, 5}`

2. **Set Intersection:**
   - *Description:* Create a function to find the common elements between two sets.
   - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {2, 3, 4}`
   - *Example Output:* `{2, 3}`

3. **Symmetric Difference:**
   - *Description:* Write a function to find the symmetric difference between two sets.
   - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {3, 4, 5}`
   - *Example Output:* `{1, 2, 4, 5}`

4. **Subset Check:**
   - *Description:* Implement a function to check if one set is a subset of another.
   - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {1, 2, 3, 4, 5}`
   - *Example Output:* `True`

5. **Remove Duplicates from a List:**
   - *Description:* Write a function to remove duplicate elements from a list using a set.
   - *Example Input:* `[1, 2, 2, 3, 4, 4, 5]`
   - *Example Output:* `[1, 2, 3, 4, 5]`

6. **Union of Sets:**
   - *Description:* Create a function to find the union of two sets.
   - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {3, 4, 5}`
   - *Example Output:* `{1, 2, 3, 4, 5}`

7. **Set Comprehension:**
   - *Description:* Use a set comprehension to create a set of squares from a given list of numbers.
   - *Example Input:* `[1, 2, 3, 4, 5]`
   - *Example Output:* `{1, 4, 9, 16, 25}`

8. **Difference of Sets:**
   - *Description:* Write a function to find the difference between two sets.
   - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {3, 4, 5}`
   - *Example Output:* `{1, 2}`

9. **Set Disjointness:**
   - *Description:* Implement a function to check if two sets are disjoint (have no common elements).
   - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {4, 5, 6}`
   - *Example Output:* `True`
10. **Common Elements with Another Set:**
    - *Description:* Write a function to find the common elements between two sets.
    - *Example Input:* `set1 = {1, 2, 3}`, `set2 = {3, 4, 5}`
    - *Example Output:* `{3}`

### Linked-lists

1. **Linked List Implementation:**
    - Description: Implement a basic singly linked list with methods for insertion and display.
    - Example: Insert elements into the linked list and display its content.
2. **Search in Linked List:**
   - *Description:* Implement a function to search for the first node with a specific value in a linked list.
   - *Example List:* `1 -> 3 -> 7 -> 9`
   - *Value to Search:* `7`
   - *Example Output:* The first node with value `7` was found: `7`
3. **Delete Node from Linked List**:
    - Description: Write a function to delete a specific node from a linked list.
    - Example Input: Linked list: `1 -> 2 -> 3 -> 4`, Node to delete: `3`
    - Example Output: Linked list after deletion: `1 -> 2 -> 4`

### Graphs

1. **Create a Cyclic Graph:**
   - *Description:* Implement code to create a simple cyclic directed graph.
   - *Graph Structure:*  `A -> B -> C -> A` (Forming a cycle).
