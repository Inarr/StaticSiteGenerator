import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        #print(f'node is {node.text_type}')
        #print(f'node2 is {node2.text_type}')
        self.assertEqual(node, node2)

    def test_notEq(self):
        node = TextNode("This is a text node", TextType.LINKS)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2) 

    def test_isURLnone(self):
        node = TextNode("This is a text node", TextType.LINKS)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
