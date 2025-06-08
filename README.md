# MSCS532 - Assignment 3: Quicksort

## Description

This project implements the **Quicksort** algorithm in Python. The algorithm is an enhancement of the standard Quicksort, where the pivot is chosen randomly to avoid the worst-case performance that occurs when the pivot is poorly chosen (e.g., in already sorted arrays).

The code handles:
- Arrays with unique and repeated elements
- Empty arrays
- Already sorted arrays
- Reverse sorted arrays

## How to Run the Code

### Requirements
- Python 3.6 or higher

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/snevoji35690/MSCS532_Assignment3.git
   cd MSCS532_Assignment3

### Run  the python script
python quicksort.py

### File Structure
MSCS532_Assignment3/
│
├── quicksort.py         # Main implementation
├── test_randomized_quicksort.py    # Optional test cases
├── README.md                       # This file


### Summary of Findings
Random pivot selection significantly improves average performance by reducing the chance of encountering the worst-case time complexity 
𝑂(n^2)
The algorithm consistently performs well on random and partially sorted inputs.
Performance degrades only slightly with repeated elements, but not significantly.
Time complexity observed:
Average: O(n log n)
Worst-case: O(n²) (rare due to random pivot)
Randomized Quicksort outperforms deterministic Quicksort when input patterns are unpredictable.


