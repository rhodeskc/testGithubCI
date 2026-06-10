import unittest
from hello_world import HelloClass

class TestHello(unittest.TestCase):
    def testEmpty(self):
        obj=HelloClass()
        result=obj.hello_world_msg("")
        self.assertEqual(result,"Hello world!",f"EvA: {result} vs 'world!'")

    def testString(self):
        obj=HelloClass()
        result=obj.hello_world_msg("Dingo")
        self.assertEqual(result,"Hello Dingo",f"EvA: {result} vs 'Dingo'")

if __name__ == "__main__":
    unittest.main()
