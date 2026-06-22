import unittest
from hello_world import HelloClass

class TestHello(unittest.TestCase):
    def test_empty(self):
        obj=HelloClass()
        result=obj.hello_world_msg("")
        self.assertEqual(result,"Hello world!",f"EvA: {result} vs 'world!'")

    def test_string(self):
        obj=HelloClass()
        result=obj.hello_world_msg("Dingo")
        self.assertEqual(result,"Hello Dingo",f"EvA: {result} vs 'Dingo'")

    def test_list_empty(self):
        obj = HelloClass()
        self.assertEqual(obj.hello_world_msg([]), "Hello world!")
        self.assertEqual(obj.hello_world_msg(["", "   "]), "Hello world!")

    def test_list_single(self):
        obj = HelloClass()
        self.assertEqual(obj.hello_world_msg(["Alice"]), "Hello Alice")

    def test_list_two(self):
        obj = HelloClass()
        self.assertEqual(obj.hello_world_msg(["Alice", "Bob"]), "Hello Alice and Bob")

    def test_list_multiple(self):
        obj = HelloClass()
        self.assertEqual(obj.hello_world_msg(["Alice", "Bob", "Charlie"]), "Hello Alice, Bob, and Charlie")
        self.assertEqual(obj.hello_world_msg(["Alice", "Bob", "Charlie", "David"]), "Hello Alice, Bob, Charlie, and David")

    def test_invalid_type(self):
        obj = HelloClass()
        with self.assertRaises(TypeError):
            obj.hello_world_msg(123)  # type: ignore

if __name__ == "__main__":
    unittest.main()

