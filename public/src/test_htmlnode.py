import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('p', 'This is a text', ['pic','para'], {'href': 'https://www.google.com', 'target':'_blank'})
        node2 = HTMLNode('p', 'This is a text', ['pic','para'], {'href': 'https://www.google.com', 'target':'_blank'})
        #node3 = HTMLNode('p', 'This is a text', ['pic','para'])
        self.assertEqual(node1, node2)

    def test_notEq(self):
        node1 = HTMLNode('p', 'This is a text', ['pic','para'], {'href': 'https://www.google.com', 'target':'_blank'})
        node2 = HTMLNode('p', 'This is a text', ['pic','para'])
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node1 = HTMLNode('', '', [], {"href": "https://www.google.com","target": "_blank",})
        node1.props_to_html()
        


if __name__ == "__main__":
    unittest.main()