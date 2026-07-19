# 📘 Week 6 — Day 12: Implementing Cosine Similarity from Scratch

## Objective

Today's objective was to implement Cosine Similarity from scratch using only Python built-in operations.

The implementation does not rely on external libraries such as NumPy or Scikit-learn. This reinforces the mathematical understanding of vector operations and prepares the foundation for semantic search and Retrieval-Augmented Generation (RAG).

---

# Concepts Used

The implementation combines several mathematical concepts learned during Week 5 and Week 6:

* Vectors
* Dot Product
* L2 (Euclidean) Norm
* Cosine Similarity

Rather than treating these concepts independently, the program demonstrates how they work together to compare the directional similarity between two vectors.

---

# Why Cosine Similarity Matters

Cosine Similarity compares vectors based on the angle between them instead of their magnitude.

This makes it particularly useful for comparing text embeddings because two documents may have different lengths while still conveying similar meaning.

Modern AI systems frequently rely on cosine similarity when retrieving the most relevant information from large collections of vector embeddings.

---

# Real-World Applications

Cosine Similarity is commonly used in:

* Vector Databases
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Recommendation Systems
* Information Retrieval
* Document Similarity
* Sentence Embeddings
* Large Language Models

When a user asks a question in a RAG system, both the query and stored documents are converted into embeddings. The retrieval system compares these embeddings using cosine similarity to identify the most relevant documents.

---

# Learning Outcomes

After completing today's work, I can:

* Implement cosine similarity without external libraries.
* Explain why cosine similarity uses the dot product and vector norms.
* Compare vectors based on direction rather than magnitude.
* Understand why cosine similarity is preferred for semantic similarity tasks.

---

## Progress

✅ Week 6 — Day 12 Completed
