import unittest
from hello_world.hello import say_hello

class TestHelloWorld(unittest.TestCase):
  def test_say_hello(self):
    result = say_hello("world")
    self.assertEqual(result, "Hello, World!")

if __name__ == "__main__":
  unittest.main()
