# 📘 Week 6 – Weekly Recap: Advanced Linear Algebra for AI

## Week Objective

The primary objective of Week 6 was to strengthen my understanding of advanced linear algebra concepts that are widely used in Artificial Intelligence, Machine Learning, Retrieval-Augmented Generation (RAG), recommendation systems, vector databases, and dimensionality reduction techniques.

Instead of focusing only on mathematical formulas, I concentrated on building intuition, understanding the purpose of each concept, and learning how these ideas are applied in real AI systems.

---

# Topics Covered

## 1. Vector Norms

### L1 Norm (Manhattan Norm)

* Sum of the absolute values of all vector components.
* Measures the total distance travelled along each dimension.
* Commonly used in sparse machine learning models and LASSO Regularization.

### L2 Norm (Euclidean Norm)

* Straight-line distance from the origin to a vector.
* Represents the magnitude (length) of a vector.
* Widely used in optimization, gradient calculations, and cosine similarity.

### L-Infinity Norm

* The maximum absolute value among all vector components.
* Measures the largest deviation in any dimension.
* Used when the maximum error is more important than the overall error.

---

# Why Norms Matter

Norms allow us to measure the magnitude of vectors.

They are used in:

* Machine Learning
* Gradient Descent
* Regularization
* Error Measurement
* Similarity Calculations
* Optimization Algorithms

---

# 2. Cosine Similarity

Cosine Similarity measures how similar two vectors are based on the angle between them rather than their magnitude.

Unlike Euclidean distance, cosine similarity focuses on direction, making it highly effective for comparing text embeddings and semantic meaning.

---

## Mathematical Formula

Cosine Similarity is calculated using:

* Dot Product
* L2 Norm of Vector A
* L2 Norm of Vector B

The resulting value ranges from **-1 to 1**.

---

## Interpretation

* **1** → Vectors point in the same direction.
* **0** → Vectors are perpendicular (no directional similarity).
* **-1** → Vectors point in opposite directions.

---

# Why Cosine Similarity Matters

Cosine Similarity is one of the most important concepts in modern AI because it powers:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Sentence Embeddings
* Recommendation Systems
* Information Retrieval
* Document Similarity
* Large Language Models

Whenever an embedding is compared with another embedding, cosine similarity is one of the most commonly used similarity metrics.

---

# 3. Relationship Between Concepts

This week demonstrated how multiple mathematical concepts work together.

Vectors represent data.

↓

Dot Product measures directional relationship.

↓

Norms measure vector magnitude.

↓

Cosine Similarity combines both to compare semantic similarity.

Instead of treating these as isolated topics, I learned how they form a connected mathematical pipeline used throughout AI.

---

# 4. Linear Combination Revision

I revised the concept of linear combinations and strengthened my understanding that:

* A linear combination creates a new vector by multiplying existing vectors by scalar weights and adding them together.
* Neural networks perform weighted linear combinations of input features before applying activation functions.
* Machine learning models learn these weights during training.

This concept forms the mathematical foundation of neural networks and many machine learning algorithms.

---

# Practical Work

Throughout the week I:

* Practiced manual calculations of vector norms.
* Reviewed vector magnitude and dot product.
* Implemented cosine similarity using pure Python.
* Strengthened my understanding of vectors and linear combinations.
* Connected mathematical concepts to their applications in AI.
* Revised previous linear algebra concepts to build a stronger foundation.

---

# Real-World AI Applications

The concepts studied this week are directly used in:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search Engines
* Recommendation Systems
* Information Retrieval
* Document Search
* Embedding Models
* Large Language Models
* Neural Networks
* Machine Learning Pipelines

---

# Key Learning Outcomes

After completing Week 6, I can:

* Explain the difference between L1, L2, and L-Infinity norms.
* Describe what vector magnitude represents.
* Explain why cosine similarity measures angle instead of distance.
* Interpret cosine similarity values.
* Explain why cosine similarity is preferred for text embeddings.
* Understand how vectors, dot products, and norms work together.
* Explain the purpose of linear combinations in machine learning.
* Relate these mathematical concepts to real-world AI applications.

---

# Summary

Week 6 strengthened my mathematical foundation for Artificial Intelligence by connecting vectors, norms, dot products, linear combinations, and cosine similarity into a unified understanding.

Rather than memorizing formulas, I focused on understanding the intuition behind each concept, implementing them in Python, and recognizing how they are used inside modern AI systems such as Retrieval-Augmented Generation (RAG), vector databases, semantic search, recommendation systems, and Large Language Models.

---

## Week Status

✅ Week 6 Completed
