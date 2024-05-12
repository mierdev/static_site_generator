import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
  def setUp(self):
     # setup common scenarios here
     self.node_0 = TextNode("Boots is the BEST wizard bear", "text")
     self.node_1 = TextNode("Boots is the BEST wizard bear", "text")
     self.node_2 = TextNode("Boots is the BEST wizard bear", "bold")
     self.node_3 = TextNode("Boots is a dog?", "text")
     self.node_4 = TextNode("Boots is the BEST wizard bear", "bold", "https://www.boot.dev")
     self.node_5 = TextNode("Boots is the BEST wizard bear", "bold", "https://www.boot.dev")


  def test_equal_true_text_texttype(self):
     self.assertEqual(self.node_0, self.node_1)

  def test_equal_false_text_texttype(self):
     self.assertNotEqual(self.node_0, self.node_2)
  
  def test_equal_false2_text_texttype(self):
     self.assertNotEqual(self.node_0, self.node_3)

  def test_equal_true_url(self):
     self.assertEqual(self.node_4, self.node_5)
  
  def test_equal_false_url(self):
     self.assertNotEqual(self.node_2, self.node_4)
  
  def test_equal_true_repr(self):
     format = f"TextNode(Boots is the BEST wizard bear, bold, https://www.boot.dev)"
     self.assertEqual(format, repr(self.node_4))
     

if __name__ == "__main__":
  unittest.main()