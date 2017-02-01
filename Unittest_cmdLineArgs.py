import unittest
import sys

from fileLineReading import *

class fileReading(unittest.TestCase):

    def test_fileLineprinting(self):
        s = "plugins where more information needs to be conveyed that doesn't fit into the categories of \"description\" or\n"
        self.assertEqual(s,filereading(sys.argv[1],2),"They are not same.")

    #def test_closing_the_file(self):
     #   print(self.assertTrue(fileclosed(sys.argv[1])))

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[1]])