# Programming excercises level intermediate

This collection of exercises is designed to provide an intermediate approach to programming, addressing basic concepts of data structures and algorithms. Whether you're advancing from basic programming concepts or looking to consolidate your understanding in these key topics.

# Section under construction

![construction](./image.jpg)

## Table of contents of excercises

- [Data-Structures](#data-structures).
  - [Stacks](#stacks).
  - [Queues](#queues).
  - [Sets](#sets).
  - [Linked-Lists](#linked-lists).
  - [Graphs](#graphs).
- [HTTP-REST-endpoints](#http-rest-endpoints).

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


## HTTP-REST-endpoints

In this section, we will harden HTTP REST endpoints. You will find
exercises on sending HTTP requests, verbs, pagination, resource filtering, and more here. You don't need to connect a database, you can create arrays of items in your service to simulate a database. Each exercise is independent of the rest, it is best to evaluate case by case.

1. **Get all users:**
   - Description: Retrieve all users stored in the database.
   - Method: GET
   - URL: `/users`
   - Example Output:
     ```json
     [
       {"id": 1, "name": "User1", "age": 25, "active": true},
       {"id": 2, "name": "User2", "age": 30, "active": true},
       {"id": 3, "name": "User3", "age": 22, "active": true}
     ]
     ```
   - HTTP Status: 200 OK

2. **Get a user by ID:**
   - Description: Retrieve a specific user by their ID.
   - Method: GET
   - URL: `/users/{id}` (e.g., `/users/1`)
   - Example Output:
     ```json
     {"id": 1, "name": "User1", "age": 25, "active": true}
     ```
   - HTTP Status: 200 OK

3. **Filter users by criteria:**
   - Description: Retrieve users that meet certain filtering criteria.
   - Method: GET
   - URL: `/users?age=25`
   - Example Output:
     ```json
     [
       {"id": 1, "name": "User1", "age": 25, "active": true}
     ]
     ```
   - HTTP Status: 200 OK

4. **Create a new user:**
   - Description: Create a new user with the provided information.
   - Method: POST
   - URL: `/users`
   - Body: New user data
     ```json
     {"name": "NewUser", "age": 28, "active": true}
     ```
   - Example Output:
     ```json
     {"id": 4, "name": "NewUser", "age": 28, "active": true}
     ```
   - HTTP Status: 201 Created

5. **Update user information:**
   - Description: Update the information of a specific user.
   - Method: PUT
   - URL: `/users/{id}` (e.g., `/users/2`)
   - Body: New user data
     ```json
     {"name": "ModifiedUser", "age": 32, "active": true}
     ```
   - Example Output:
     ```json
     {"id": 2, "name": "ModifiedUser", "age": 32, "active": true}
     ```
   - HTTP Status: 200 OK

6. **Delete a user by ID:**
   - Description: Delete a specific user by their ID.
   - Method: DELETE
   - URL: `/users/{id}` (e.g., `/users/4`)
   - Example Output:
     ```json
     {"message": "User deleted successfully"}
     ```
   - HTTP Status: 204 No Content

7. **User pagination:**
   - Description: Retrieve a specific page of users for pagination.
   - Method: GET
   - URL: `/users?offset=2&limit=1`
   - Example Output:
     ```json
     [
       {"id": 3, "name": "User3", "age": 22, "active": true}
     ]
     ```
   - HTTP Status: 200 OK

8. **Search users by name:**
   - Description: Search for users matching a provided name.
   - Method: GET
   - URL: `/users?name=User1`
   - Example Output:
     ```json
     [
      {"id": 1, "name": "User1", "age": 25, "active": true}
     ]
     ```
   - HTTP Status: 200 OK

9. **Sort users by a specific field:**
   - Description: Retrieve users sorted by a specific field (e.g., age).
   - Method: GET
   - URL: `/users?order=age`
   - Example Output:
     ```json
     [
       {"id": 3, "name": "User3", "age": 22, "active": true},
       {"id": 1, "name": "User1", "age": 25, "active": true},
       {"id": 2, "name": "User2", "age": 30, "active": true},
     ]
     ```
   - HTTP Status: 200 OK

10. **Filter active users:**
    - Description: Retrieve users that are active in the system.
    - Method: GET
    - URL: `/users?active=true`
    - Example Output:
      ```json
      [
       {"id": 1, "name": "User1", "age": 25, "active": true},
       {"id": 2, "name": "User2", "age": 30, "active": true},
       {"id": 3, "name": "User3", "age": 22, "active": true}
      ]
      ```
    - HTTP Status: 200 OK

11. **Get all products:**
   - Description: Retrieve all products available in the inventory.
   - Method: GET
   - URL: `/products`
   - Example Output:
     ```json
     [
       {"id": 101, "name": "ProductA", "price": 19.99, "category": "Electronics", "stock": true},
       {"id": 102, "name": "ProductB", "price": 29.99, "category": "Clothing", "stock": true},
       {"id": 103, "name": "ProductC", "price": 14.99, "category": "Home", "stock": false}
     ]
     ```
   - HTTP Status: 200 OK

12. **Get a product by ID:**
   - Description: Retrieve a specific product by its ID.
   - Method: GET
   - URL: `/products/{id}` (e.g., `/products/101`)
   - Example Output:
     ```json
     {"id": 101, "name": "ProductA", "price": 19.99, "category": "Electronics", "stock": true}
     ```
   - HTTP Status: 200 OK

13. **Filter products by category:**
   - Description: Retrieve products belonging to a specific category.
   - Method: GET
   - URL: `/products?category=electronics`
   - Example Output:
     ```json
     [
        {"id": 101, "name": "ProductA", "price": 19.99, "category": "Electronics", "stock": true},
     ]
     ```
   - HTTP Status: 200 OK

14. **Create a new product:**
   - Description: Add a new product to the inventory.
   - Method: POST
   - URL: `/products`
   - Body: New product data
     ```json
     {"name": "NewProduct", "price": 39.99, "category": "Home", "stock": true}
     ```
   - Example Output:
     ```json
     {"id": 104, "name": "NewProduct", "price": 39.99, "category": "Home", "stock": true}
     ```
   - HTTP Status: 201 Created

15. **Update product information:**
   - Description: Update details of a specific product.
   - Method: PUT
   - URL: `/products/{id}` (e.g., `/products/102`)
   - Body: Updated product data
     ```json
     {"name": "UpdatedProductB", "price": 34.99, "category": "Clothing", "stock": false}
     ```
   - Example Output:
     ```json
     {"id": 102, "name": "UpdatedProductB", "price": 34.99, "category": "Clothing", "stock": false}
     ```
   - HTTP Status: 200 OK

16. **Delete a product by ID:**
   - Description: Remove a specific product from the inventory.
   - Method: DELETE
   - URL: `/products/{id}` (e.g., `/products/103`)
   - Example Output:
     ```json
     {"message": "Product deleted successfully"}
     ```
   - HTTP Status: 204 No Content

17. **Product pagination:**
   - Description: Retrieve a specific page of products for pagination.
   - Method: GET
   - URL: `/products?offset=2&limit=1`
   - Example Output:
     ```json
     [
      {"id": 103, "name": "ProductC", "price": 14.99, "category": "Home", "stock": false}
     ]
     ```
   - HTTP Status: 200 OK

18. **Search products by name:**
   - Description: Search for products matching a provided name.
   - Method: GET
   - URL: `/products?name=ProductA`
   - Example Output:
     ```json
     [
        {"id": 101, "name": "ProductA", "price": 19.99, "category": "Electronics", "stock": true},
     ]
     ```
   - HTTP Status: 200 OK

19. **Sort products by price:**
   - Description: Retrieve products sorted by price in ascending order.
   - Method: GET
   - URL: `/products?order=price`
   - Example Output:
     ```json
     [
       {"id": 103, "name": "ProductC", "price": 14.99, "category": "Home", "stock": false},
       {"id": 101, "name": "ProductA", "price": 19.99, "category": "Electronics", "stock": true},
       {"id": 102, "name": "ProductB", "price": 29.99, "category": "Clothing", "stock": true},
     ]
     ```
   - HTTP Status: 200 OK

20. **Filter in-stock products:**
    - Description: Retrieve products that are currently in stock.
    - Method: GET
    - URL: `/products?stock=true`
    - Example Output:
      ```json
      [
        {"id": 101, "name": "ProductA", "price": 19.99, "category": "Electronics", "stock": true},
        {"id": 102, "name": "ProductB", "price": 29.99, "category": "Clothing", "stock": true},
      ]
      ```
    - HTTP Status: 200 OK
