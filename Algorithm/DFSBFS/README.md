# DFS/BFS (Depth-First/Breadth-First Search) Algorithms

This repository was created to learn the concepts of Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms and to document the process of solving related problems.

## Overview

DFS and BFS are the two most fundamental methods for graph traversal. They are used to visit every vertex of a graph once and form the basis for solving a wide variety of problems.

- **Graph:** A set of vertices and the edges that connect them.
- **Search (Traversal):** The process of visiting all the vertices in a graph.

---

## Depth-First Search (DFS)

DFS is a method that starts at a root node (or an arbitrary node) and explores as far as possible along each branch before backtracking. In other words, it goes as deep as possible and then backtracks to explore other paths.

### Key Features

- **Data Structure:** Implemented using a stack or recursion.
- **How it works:**
  1. Push the starting node onto the stack and mark it as visited.
  2. If the node at the top of the stack has an unvisited adjacent node, push that node onto the stack and mark it as visited.
  3. If there are no unvisited adjacent nodes, pop the node from the top of the stack.
  4. Repeat steps 2-3 until the stack is empty.
- **Advantages:** Requires relatively less memory as it only needs to store the nodes on the current path.
- **Disadvantages:** Can get stuck in deep paths that have no solution, potentially leading to long search times.

---

## Breadth-First Search (BFS)

BFS is a method that starts at a root node and explores all the neighboring nodes at the present depth prior to moving on to the nodes at the next depth level. In other words, it explores nodes in order of their distance from the starting point.

### Key Features

- **Data Structure:** Implemented using a queue.
- **How it works:**
  1. Enqueue the starting node and mark it as visited.
  2. Dequeue a node and for all its adjacent nodes that have not been visited, enqueue them and mark them as visited.
  3. Repeat step 2 until the queue is empty.
- **Advantages:** Effective for finding the shortest path in unweighted graphs because it explores nodes level by level.
- **Disadvantages:** Can consume a large amount of memory if the path is very long, as it needs to store many nodes in the queue.

---

## Problem List

This repository covers the following DFS/BFS related problems.

*The list of problems will be continuously updated.*