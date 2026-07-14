# 📘 Day 09 — Vector Norms: Applications and Comparison

## Week 6 — Linear Algebra

### Objective

Today's goal was to complete the study of vector norms by understanding how different norms measure vector magnitude and where they are used in Artificial Intelligence.

---

# What is a Norm?

A norm is a mathematical function used to measure the size or magnitude of a vector.

Different norms measure "size" in different ways depending on the problem being solved.

---

# L1 Norm (Manhattan Norm)

## Intuition

The L1 norm measures the total distance traveled along each axis.

Instead of taking the shortest path, it moves horizontally and vertically, similar to navigating city streets arranged in a grid.

## Characteristics

* Sum of absolute values
* Produces sparse solutions
* Less sensitive to outliers

## Common Applications

* Lasso Regression
* Feature Selection
* Sparse Machine Learning Models

---

# L2 Norm (Euclidean Norm)

## Intuition

The L2 norm measures the straight-line distance between the origin and a vector.

It represents the actual geometric length of a vector.

## Characteristics

* Most common norm in Machine Learning
* Penalizes large values more strongly
* Smooth and differentiable

## Common Applications

* Neural Networks
* Gradient Descent
* Euclidean Distance
* Weight Decay
* Embedding Magnitude

---

# L∞ Norm (Maximum Norm)

## Intuition

The L∞ norm only considers the largest absolute component of a vector.

It measures the maximum possible deviation.

## Characteristics

* Focuses on the worst-case value
* Useful for optimization problems

## Common Applications

* Constraint Optimization
* Error Bounds
* Numerical Analysis

---

# Comparison of Norms

| Norm | Measures                | Typical Use                      |
| ---- | ----------------------- | -------------------------------- |
| L1   | Total absolute distance | Sparse models, feature selection |
| L2   | Straight-line distance  | Machine learning, deep learning  |
| L∞   | Largest component       | Optimization and error analysis  |

---

# Why Norms Matter in AI

Norms appear throughout Artificial Intelligence.

They help measure:

* Vector magnitude
* Prediction error
* Model complexity
* Distance between vectors
* Embedding normalization

Without norms, many optimization algorithms and learning methods would not function correctly.

---

# Real-World AI Connection

Examples of where norms are used:

* Training neural networks
* Weight regularization
* Gradient optimization
* Vector embeddings
* Recommendation systems
* Similarity search
* Retrieval-Augmented Generation (RAG)

Norms provide the mathematical foundation for comparing and controlling numerical representations inside AI systems.

---

# Key Learning Outcomes

After completing today's study:

* Understand the intuition behind L1, L2 and L∞ norms.
* Know the strengths and weaknesses of each norm.
* Understand where each norm is commonly applied.
* Recognize the importance of norms in modern AI systems.

---

## Progress

✅ Week 6 — Day 09 Completed
