import unittest

from SplitNodeDelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_eq_code(self):
      node = TextNode("This is text with a `code block` word", TextType.NORMAL)
      new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
      self.assertEqual(new_nodes, [[
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.NORMAL),
  ]])
    def test_exceptions(self):
      node = TextNode("This is text with a `code block word", TextType.NORMAL)
      #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
      self.assertRaises(Exception,split_nodes_delimiter, [node],"`",TextType.CODE)

    def test_eq_bold(self):
      node = TextNode("This is text with a **bold** word", TextType.NORMAL)
      new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
      self.assertEqual(new_nodes, [[
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" word", TextType.NORMAL),]])

if __name__ == "__main__":
    unittest.main()

