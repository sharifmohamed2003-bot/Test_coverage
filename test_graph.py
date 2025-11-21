import unittest
from io import StringIO
import sys

from bfs_dfs import Queue, Stack, UndirectedGraph


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        q = Queue(size=5)
        q.enqueue("A")
        q.enqueue("B")
        self.assertEqual(q.dequeue(), "A")
        self.assertEqual(q.dequeue(), "B")
        self.assertTrue(q.is_empty())

    def test_queue_overflow(self):
        q = Queue(size=3)
        q.enqueue("A")
        q.enqueue("B")
        q.enqueue("C")
        self.assertEqual(q.enqueue("D"), "Queue Overflow")

    def test_queue_underflow(self):
        q = Queue()
        self.assertEqual(q.dequeue(), "Queue Underflow")


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        s = Stack()
        s.push("A")
        s.push("B")
        self.assertEqual(s.pop(), "B")
        self.assertEqual(s.pop(), "A")
        self.assertTrue(s.is_empty())

    def test_stack_underflow(self):
        s = Stack()
        self.assertEqual(s.pop(), "stack underflow")


class TestGraphConstruction(unittest.TestCase):

    def test_build_graph(self):
        nodes = ["A", "B", "C"]
        edges = [("A", "B"), ("B", "C")]
        g = UndirectedGraph(nodes, edges)
        self.assertEqual(sorted(g.graph["A"]), ["B"])
        self.assertEqual(sorted(g.graph["B"]), ["A", "C"])
        self.assertEqual(sorted(g.graph["C"]), ["B"])


class TestBFS(unittest.TestCase):

    def setUp(self):
        nodes = ["A", "B", "C", "D"]
        edges = [("A","B"), ("A","C"), ("B","D"), ("C","D")]
        self.g = UndirectedGraph(nodes, edges)

    def test_bfs(self):
        result = self.g.BFS("A")
        self.assertEqual(result, ["A", "B", "C", "D"])


class TestDFS(unittest.TestCase):

    def setUp(self):
        nodes = ["A", "B", "C", "D"]
        edges = [("A","B"), ("A","C"), ("B","D"), ("C","D")]
        self.g = UndirectedGraph(nodes, edges)

    def test_dfs(self):
        result = self.g.DFS("A")
        expected = ["A", "B", "D", "C"]
        self.assertEqual(result, expected)


class TestShortestPaths(unittest.TestCase):

    def setUp(self):
        nodes = ["A", "B", "C", "D", "E", "F"]
        edges = [
            ("A","B"), ("A","C"),
            ("B","D"), ("C","D"),
            ("D","E"), ("E","F")
        ]
        self.g = UndirectedGraph(nodes, edges)

    def test_shortest_paths(self):
        dist = self.g.shortest_paths("A")
        expected = {"A": ['A'], "B":  ['A', 'B'], "C": ['A', 'C'], "D": ['A', 'B', 'D'], "E": ['A', 'B', 'D', 'E'], "F": ['A', 'B', 'D', 'E', 'F']}
        self.assertEqual(dist, expected)

    def test_shortest_path_length(self):
        self.assertEqual(self.g.shortest_path_length("A", "F"), ['A', 'B', 'D', 'E', 'F'])
        self.assertEqual(self.g.shortest_path_length("A", "Z"), "unreachable")


if __name__ == "__main__":
    unittest.main()