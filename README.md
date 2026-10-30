# Module 5: Fundamental Data Structures — Stacks and Queues

## Description
This project implements stacks and queues using arrays and linked lists. It includes a menu-driven program, a balanced-parentheses checker, and a print-queue simulation.

## Learning Objectives
- Understand LIFO (Last In, First Out) and FIFO (First In, First Out).
- Implement push, pop, peek, enqueue, dequeue, and peek_front.
- Handle underflow and overflow errors.
- Apply stacks to balanced-parentheses checking.
- Apply queues to print-job scheduling.

## Project Files
| File | Description |
|---|---|
| `node.py` | Defines a linked-list node. |
| `array_stack.py` | Fixed-capacity array stack. |
| `linked_stack.py` | Linked-list stack. |
| `array_queue.py` | Circular array queue. |
| `linked_queue.py` | Linked-list queue. |
| `main.py` | Menu and application exercises. |
| `analysis.md` | Written analysis of the data structures. |
| `README.md` | Project documentation and run instructions. |

## Requirements
Python 3. No external libraries are required.

## How to Run
1. Keep all Python files in the same folder.
2. Open a terminal in that folder.
3. Run `python main.py` (or `python3 main.py`).

## Main Menu
1. Use a data structure.
2. Check balanced parentheses.
3. Simulate a print queue.
0. Exit.

## Error Handling
The program reports stack/queue underflow and array-based overflow. It also handles invalid capacity and invalid page-count input.

## Time Complexity
| Operation | Time |
|---|---|
| Stack push | O(1) |
| Stack pop | O(1) |
| Stack peek | O(1) |
| Queue enqueue | O(1) |
| Queue dequeue | O(1) |
| Queue peek_front | O(1) |

## Applications
- Balanced parentheses: checks matching and nesting of `()`, `[]`, and `{}`.
- Print queue: processes jobs in FIFO order.

## Author
Jayfh Mori L. Yruma

## Subject
Data Structures and Algorithms
