import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node_1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node_2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node_3 = TextNode("Boring!", "cursive")
    node_4 = TextNode("Boring!", "whatever", None)
    self.assertEqual(node_1, node_2)
    self.assertNotEqual(node_1, node_3)
    self.assertNotEqual(node_3, node_4)
    self.assertIsNone(node_3.url, node_4.url)
    self.assertIsNotNone(node_1.url, node_2.url)

'''
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
'''


if __name__ == "__main__":
  unittest.main()