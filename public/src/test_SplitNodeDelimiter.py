import unittest

from SplitNodeDelimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
  def test_eq_code(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
])
    def test_exceptions(self):
      node = TextNode("This is text with a `code block word", TextType.TEXT)
      #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
      self.assertRaises(Exception,split_nodes_delimiter, node,"'",TextType.CODE)

    def test_eq_bold(self):
    node = TextNode("This is text with a **bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" word", TextType.TEXT),])
