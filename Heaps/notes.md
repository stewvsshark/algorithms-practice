# Heaps

Heaps are a subset of binary trees that are complete and
maintain the property that each node must be not greater than
or not less than the value(s) of its children. 

A Priority queue is an abstract data type; 
a heap is a data structure. A priority queue could
be implemented as a list or array which would guarantee
O(1) insertion or deletion, but other operations would have
O(N) time complexity

Stores elements, and can find the smallest (min-heap) or largest (max-heap) element stored in O(1)O(1).
Can add elements and remove the smallest (min-heap) or largest (max-heap) element in O(\log(n))O(log(n)).
Can perform insertions and removals while always maintaining the first property.


## Methods required 
### Insertion
- Determine type of heap: examine root and children
- Insert element in first available leaf node (bottom left most unoccupied)
- Heapify: 
  - if new node is less than parent; swap
  - repeat until heap condition satisfied

### Deletion

- Remove the first (root) element of the tree
- Remove the bottom right (last) element of the tree and place it at root
- Heapify
  - exchange node with child that satisfies heap condition, starting with left most

### Heapify 
- Heapify will be required for insertion and deletion operations to maintain
the desired heap properties
