import unittest
from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

class DataStructureTests(unittest.TestCase):
    def test_array_stack_order_and_errors(self):
        s = ArrayStack(2)
        s.push("A"); s.push("B")
        self.assertEqual(s.peek(), "B")
        with self.assertRaises(OverflowError): s.push("C")
        self.assertEqual(s.pop(), "B")
        self.assertEqual(s.pop(), "A")
        with self.assertRaises(IndexError): s.pop()

    def test_linked_stack_order_and_errors(self):
        s = LinkedStack()
        s.push(1); s.push(2)
        self.assertEqual(s.display(), [2, 1])
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        with self.assertRaises(IndexError): s.peek()

    def test_circular_queue_wraparound_and_errors(self):
        q = ArrayQueue(3)
        q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
        self.assertEqual(q.dequeue(), "A")
        q.enqueue("D")
        self.assertEqual(q.display(), ["B", "C", "D"])
        with self.assertRaises(OverflowError): q.enqueue("E")
        self.assertEqual(q.dequeue(), "B")
        self.assertEqual(q.dequeue(), "C")
        self.assertEqual(q.dequeue(), "D")
        with self.assertRaises(IndexError): q.dequeue()

    def test_linked_queue_order_and_empty_reset(self):
        q = LinkedQueue()
        q.enqueue("A"); q.enqueue("B")
        self.assertEqual(q.dequeue(), "A")
        self.assertEqual(q.dequeue(), "B")
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.rear)
        q.enqueue("C")
        self.assertEqual(q.dequeue(), "C")

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError): ArrayStack(0)
        with self.assertRaises(ValueError): ArrayQueue(-1)

if __name__ == "__main__":
    unittest.main()
