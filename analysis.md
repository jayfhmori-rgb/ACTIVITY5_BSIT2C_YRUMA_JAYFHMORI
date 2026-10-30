# Analysis: Stacks and Queues

A linked-list stack pushes and pops at the head because these operations take O(1) time. If the stack removes elements from the tail of a singly linked list, it must traverse the list to find the previous node, which takes O(n) time. An array queue must be circular so that empty spaces at the beginning of the array can be reused after dequeue operations. The modulo operator allows the front and rear positions to wrap around to the beginning of the array. This makes enqueue and dequeue operations efficient, taking O(1) time.
