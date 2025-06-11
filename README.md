## Assignment 3: Randomized Quicksort & Hash Table with Chaining
Description
This project implements two major components in Python:

Randomized Quicksort Algorithm
An optimized version of the Quicksort algorithm where the pivot is selected randomly to prevent poor performance on sorted or patterned input.

Hash Table with Chaining
A custom-built hash table that uses chaining to handle collisions and a universal hash function to ensure even distribution of keys.
Both components are implemented for educational purposes and performance analysis.

## How to Run the Code
Requirements
Python 3.6 or higher

## Setup Instructions
Clone the Repository
git clone https://github.com/snevoji35690/MSCS532_Assignment3.git
cd MSCS532_Assignment3

## Run the Quicksort Script
python3 quicksort.py
python3 hashtable.py

## File Structure
MSCS532_Assignment3/
│
├── hashtable.py         # Hash table implementation using chaining
├── quicksort.py         # Randomized and Deterministic Quicksort implementations
├── README.md            # This documentation

## Summary of Findings – Randomized Quicksort (Part 3)
Observations
Random pivot selection improves average performance and avoids consistently unbalanced partitions.
The algorithm handles:
Empty arrays
Arrays with duplicates
Sorted and reverse-sorted arrays
Consistent performance is observed across most input types.

## Time Complexity
Scenario	Randomized Quicksort
Best Case      𝑂(𝑛log𝑛)
Average Case	𝑂(𝑛log𝑛)
Worst Case  	𝑂(𝑛2)(rare)

## Key Findings
Randomized Quicksort outperforms Deterministic Quicksort, especially on sorted, reversed, or duplicate-heavy arrays.
Deterministic Quicksort, which uses the first element as a pivot, is highly input-sensitive and can degrade to 𝑂(𝑛2).
Randomization provides robustness and input independence in practice.

## Hash Table Summary 
Uses chaining to resolve collisions.
Employs a universal hash function for uniform key distribution.
Supports efficient:
insert(key, value)
search(key)
delete(key)

## Performance Insight
Expected operation time: 𝑂(1+𝛼), where 𝛼=𝑛/𝑚 (load factor).
Maintaining a low load factor via dynamic resizing helps retain constant-time performance.
