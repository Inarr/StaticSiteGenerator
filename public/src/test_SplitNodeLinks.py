import unittest
from textnode import TextType, TextNode
from Extract_Markdown import *
from SpliNodeLinks import *

class TestSplitNodeLinks(unittest.TestCase):
  def test_split_images(self):
      node = TextNode(
          "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
          TextType.TEXT,
      )
      new_nodes = split_nodes_link([node])
      self.assertListEqual(
          [
              TextNode("This is text with an ", TextType.NORMAL),
              TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
              TextNode(" and another ", TextType.NORMAL),
              TextNode(
                  "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
              ),
          ],
          new_nodes,
      )

   def test_split_images_2(self):
      node = TextNode(
          "[image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
          TextType.TEXT,
      )
      new_nodes = split_nodes_link([node])
      self.assertListEqual(
          [
              TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
              TextNode(" and another ", TextType.NORMAL),
              TextNode(
                  "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
              ),
          ],
          new_nodes,
      )

   def test_split_images_2(self):
      node = TextNode(
          "and another",
          TextType.TEXT,
      )
      new_nodes = split_nodes_link([node])
      self.assertListEqual([TextNode(" and another ", TextType.NORMAL)],new_nodes,)


if __name__ == "__main__":
    unittest.main()
