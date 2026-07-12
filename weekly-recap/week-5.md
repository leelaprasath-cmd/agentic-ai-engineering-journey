# 📘 Week 05 Recap — Linear Algebra Foundations for AI

## Overview

Week 5 focused on building the mathematical foundation required for Artificial Intelligence and Machine Learning.

The objective of this week was to understand how real-world information is represented mathematically using vectors and matrices, and how these concepts form the foundation of neural networks, embeddings, and transformer architectures.

---

# Day 1 — Introduction to Vectors

## Concepts Covered

### What is a Vector?

A vector is an ordered collection of numbers that represents an object or data point in mathematical space.

Example:

```
Student = [19, 6, 90]
```

Representation:

```
19 → Age
6  → Study Hours
90 → Attendance
```

The complete student information is represented as one vector.

---

## Vector Components

Each value inside a vector is called a component.

Example:

```
[5, 10, 15]

Component 1 → 5
Component 2 → 10
Component 3 → 15
```

---

## Vector Dimension

The dimension of a vector represents the number of components.

Examples:

```
[1,2]

Dimension = 2
```

```
[1,2,3,4]

Dimension = 4
```

In AI:

```
Embedding Vector

[0.25, -0.43, 0.89, ...]

can contain hundreds or thousands of dimensions.
```

---

## Real-World AI Usage

Different types of data are converted into vectors:

```
Text → Word/Sentence Embeddings

Images → Pixel Vectors

Audio → Numerical Features

User Information → Feature Vectors
```

AI models cannot directly process raw human data. They operate on numerical representations.

---

# Day 2 — Linear Combinations, Span and Basis

## Linear Combination

A linear combination is the process of creating a new vector by combining existing vectors using scalar values.

General idea:

```
New Vector = a × Vector A + b × Vector B
```

Example:

```
A = [1,2]

B = [3,4]


2A + 3B
```

produces a new vector.

---

## Importance in AI

Machine learning models create new representations by combining existing features.

Neural networks continuously perform operations that combine information from previous layers to create better representations.

---

## Span

The span of vectors is the complete set of possible vectors that can be created using linear combinations of those vectors.

Example:

Two independent vectors:

```
[1,0]

[0,1]
```

can create every point in a 2D space.

Their span covers the complete 2D plane.

---

## Basis

A basis is the smallest set of independent vectors required to represent a vector space.

A good basis:

* Has independent vectors
* Can represent every vector in that space

Example:

For 2D space:

```
[1,0]

[0,1]
```

forms a basis.

---

# Day 3 — Matrix Multiplication: Geometric Understanding

## What is a Matrix?

A matrix is a rectangular arrangement of numbers.

Example:

```
[
 [1,2,3],
 [4,5,6]
]
```

Dimensions:

```
2 × 3

2 rows
3 columns
```

---

## Relationship Between Vectors and Matrices

Multiple vectors combined together form a matrix.

Example:

Three student vectors:

```
[
 [19,6,90],
 [20,5,85],
 [18,8,95]
]
```

This creates a matrix.

---

## Matrix Multiplication Concept

Matrix multiplication represents a transformation.

General idea:

```
Input Vector

×

Transformation Matrix

↓

New Vector
```

The matrix changes the position or representation of the vector.

---

## AI Connection

Neural networks are built using repeated matrix transformations.

Example:

```
Input Data

↓

Weight Matrix

↓

Output Representation
```

This is the mathematical foundation behind neural network layers.

---

# Day 4 — Matrix Multiplication Practice

## Matrix Multiplication Rules

For multiplication:

```
(A × B)
```

the number of columns in A must equal the number of rows in B.

Example:

```
(3 × 4)

×

(4 × 2)

=

(3 × 2)
```

---

## Row × Column Calculation

Each output value is calculated by multiplying:

```
Row of first matrix

×

Column of second matrix
```

Example:

```
[1,2,3]

×

[4,5,6]
```

The values are multiplied and added together.

---

## Important Understanding

Matrix multiplication is not simple element-by-element multiplication.

The order matters.

```
A × B

is not always equal to

B × A
```

Matrix multiplication is not commutative.

---

# Day 5 — Transpose, Identity and Inverse Matrix

## Matrix Transpose

Transpose changes rows into columns.

Example:

Before:

```
[
[1,2,3],
[4,5,6]
]
```

After:

```
[
[1,4],
[2,5],
[3,6]
]
```

---

## Identity Matrix

An identity matrix behaves like the number 1 in multiplication.

Example:

```
I × A = A
```

It keeps the original matrix unchanged.

---

## Inverse Matrix

The inverse matrix reverses the effect of another matrix.

Example:

```
A × A⁻¹ = I
```

Not every matrix has an inverse.

A matrix without an inverse is called a singular matrix.

---

## AI Connection

Matrix inverses and transformations are important in:

* Solving mathematical systems
* Understanding transformations
* Optimization algorithms

---

# Day 6 — Matrix Class Project Implementation

## Project: Matrix Class in Pure Python

Implemented a Matrix class without using NumPy.

---

## Features Implemented

### Matrix Creation

Represented matrices using nested Python lists.

Example:

```python
[
 [1,2,3],
 [4,5,6]
]
```

---

### Matrix Display

Created functionality to display matrices in readable format.

---

### Matrix Addition

Added corresponding elements of matrices.

Example:

```
A + B
```

---

### Matrix Subtraction

Subtracted corresponding elements.

Example:

```
A - B
```

---

### Matrix Multiplication

Implemented matrix multiplication manually using loops.

Concept applied:

```
Row × Column calculation
```

---

# Day 7 — Matrix Class Project Completion

## Completed Project

Finalized the Matrix Class project with:

✅ Matrix creation
✅ Matrix display
✅ Matrix addition
✅ Matrix subtraction
✅ Matrix multiplication
✅ Matrix transpose

---

## Technical Skills Applied

* Object-Oriented Programming
* Classes and Objects
* Nested Lists
* Loops
* Indexing
* Mathematical Logic Implementation

---

# Week 5 AI Connections

## Neural Networks

Neural networks use matrix multiplication between:

```
Input Vectors

×

Weight Matrices

=

Output Vectors
```

---

## Word Embeddings

Words and sentences are converted into high-dimensional vectors.

Example:

```
"AI"

↓

[0.21, -0.45, 0.87, ...]
```

---

## Transformers

Attention mechanisms rely heavily on matrix operations.

Example:

```
Q × Kᵀ
```

Matrix multiplication is one of the core operations behind modern LLMs.

---

# Week 5 Projects Completed

## Matrix Class Project

Implemented:

* Matrix operations
* Matrix multiplication
* Transpose operation

Technology:

```
Pure Python
(No NumPy)
```

---

# Final Learning Outcomes

After completing Week 5:

✅ Understand how AI data is represented as vectors.

✅ Understand vector dimensions and components.

✅ Understand linear combinations, span, and basis.

✅ Understand how matrices represent collections of vectors.

✅ Understand matrix transformations.

✅ Understand matrix multiplication conceptually and practically.

✅ Implemented matrix operations from scratch using Python.

---

# Week 05 Completion Status

```
Vectors                         ✅

Linear Combinations             ✅

Span                            ✅

Basis                           ✅

Matrix Multiplication           ✅

Transpose                       ✅

Identity Matrix                 ✅

Inverse Matrix                  ✅

Matrix Class Project            ✅
```

---

# Next Step

Continue deeper into Linear Algebra concepts required for Machine Learning and AI Engineering.
