# Data Structures Implementations in Python

This repository contains implementations of various data structures in Python. The goal is to provide clear and concise implementations along with unit tests to ensure correctness.

## Data Structures

- Binary Tree

## Binary Tree

### Description

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child. This repository includes implementations for basic operations such as insertion and traversal (in-order and pre-order).

### Implementation

The `binary_tree_impl.py` file contains the implementation of the binary tree. The main classes and methods are:

- `Node`: Represents a node in the binary tree.
- `BinaryTree`: Represents the binary tree and includes methods for insertion and traversal.
  - `insert(data)`: Inserts a new node with the given data into the tree.
  - `inorder_traversal(root)`: Performs an in-order traversal of the tree.
  - `preorder_traversal(root)`: Performs a pre-order traversal of the tree.

### Unit Tests

Unit tests are provided in the `binary_tree_impl.py` file using the `unittest` framework. The tests cover the following:

- Insertion of nodes
- In-order traversal
- Pre-order traversal

To run the tests, use the following command:

```bash
python -m unittest binary_tree_impl.py
