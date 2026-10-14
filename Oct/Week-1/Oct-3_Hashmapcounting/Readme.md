# Array Problems

## 1. Majority Element

Find the element that appears more than half the times of the given array.

### Approach
* Use a hashmap to store the frequency of the elements.
* Traverse the array and update the counts dynamically.
* If an element's frequency exceeds `n / 2` (where `n` is the length of the array), return it immediately.

### Complexity
* **Time Complexity:** O(n) 
* **Space Complexity:** O(n)