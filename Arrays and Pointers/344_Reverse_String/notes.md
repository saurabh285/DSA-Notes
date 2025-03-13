# LeetCode Problem #344: Reverse String

## Problem Description

Given an array of characters, reverse the array in-place without using extra memory. The goal is to modify the original array directly.

## Approach & Logic

I used the **two-pointer method** to efficiently reverse the array.

### Steps Taken:

1. **Initialize two pointers:**
   - `l` (left) pointing to the beginning of the array (`0`).
   - `r` (right) pointing to the end of the array (`len(s) - 1`).

2. **Swap elements:**
   - Swap characters at indices `l` and `r`.

3. **Move pointers:**
   - Increment `l` (move rightwards) and decrement `r` (move leftwards).

4. **Repeat until pointers meet or cross:**
   - Continue swapping until `l` is no longer less than `r`.

### Example Walkthrough:

```python
Input: s = ['h', 'e', 'l', 'l', 'o']

Initial pointers:
l = 0, r = 4
Swap 'h' and 'o': ['o', 'e', 'l', 'l', 'h']

Move pointers:
l = 1, r = 3
Swap 'e' and 'l': ['o', 'l', 'l', 'e', 'h']

Move pointers:
l = 2, r = 2
Pointers meet, stop.
```

## Final Implementation (Python)

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

## Complexity

- **Time Complexity:** `O(n)` (each character is visited exactly once)
- **Space Complexity:** `O(1)` (no extra space, in-place modification)

---

This document serves as a quick revision guide summarizing my approach to solving the LeetCode Reverse String problem (#344).

