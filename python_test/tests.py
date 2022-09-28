from Animals import Animal, Tiger
import unittest
import io
import sys

class TestAnimal(unittest.TestCase):

    def test_animal_energy_points_update(self):
        a = Animal('test', 5)
        self.assertEqual(a.get_energy(), 5)
    
    def test_animal_say_method(self):
        a = Animal('test', 5)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput # redirect stdout.
        a.say()
        sys.stdout = sys.__stdout__
        self.assertEqual("Hello, i'm Animal and my name is test\n" , capturedOutput.getvalue())


class TestTiger(unittest.TestCase):

    def test_tiger_say_method(self):
        a = Tiger('test', 5)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput # redirect stdout.
        a.run()
        sys.stdout = sys.__stdout__
        self.assertEqual("My name is test and i can't run because my energy is low\n" , capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()