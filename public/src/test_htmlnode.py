import unittest
from htmlnode import *
from textnode import *

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

    def test_node_to_html_italic(self):
        node1 = TextNode('This is an Italic text', 'ITALIC')
        print('**** Debug Starts ***')
        print('text:', node1.text)
        print('text_type:', node1.text_type)
        print('***Debug End ***')
        self.assertEqual(LeafNode('i','This is an Italic text'), HTMLNode.text_node_to_html_node(node1))

    def test_node_to_html_link(self):
        node1 = TextNode('This is a link',TextType.LINK,{'href': 'link/sample'})
        '''
        print('**** Debug Starts ***')
        print('text:', node1.text)
        print('text_type:', node1.text_type)
        print('url:', node1.url)
        print(HTMLNode('a','This is a link', None, 'link/sample').tag)
        print(HTMLNode.text_node_to_html_node(node1).tag)
        print('***Debug End ***')
        '''
        
        print('*** Second Debug Starts ***')
        actual = HTMLNode.text_node_to_html_node(node1)
        expected = LeafNode('a', 'This is a link', {'href': 'link/sample'})

        print("Expected:", expected.tag, expected.value, expected.props)
        print("Actual:  ", actual.tag, actual.value, actual.props)

        self.assertEqual(expected, actual)
        print('*** Second Debug End ***')


        #self.assertEqual(HTMLNode('a','This is a link', None, 'link/sample'),HTMLNode.text_node_to_html_node(node1))
        self.assertEqual(
    LeafNode('a', 'This is a link', {'href': 'link/sample'}),
    HTMLNode.text_node_to_html_node(node1)
)


    def test_node_to_html_exception(self):
        node1 = TextNode('This is a wrong type','wrong')
        self.assertRaises(Exception,HTMLNode.text_node_to_html_node, node1)

class TestLeafNode(unittest.TestCase):
    def test_value(self):
        #node1 = LeafNode('a')
        self.assertRaises(ValueError, LeafNode, 'a',None,None)

    def test_p_output(self):
        node1 = LeafNode("p", "This is a paragraph of text.",None)
        node1.to_html()
        self.assertEqual(node1.to_html(), '<p>This is a paragraph of text.</p>')

    def test_a_output(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_p_output1(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        #print(node.to_html())
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')  

    def test_p_output2(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"), ParentNode('p',[LeafNode("b", "Bold text")] ),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        #print(node.to_html())
        self.assertEqual(node.to_html(), '<p><b>Bold text</b><p><b>Bold text</b></p>Normal text<i>italic text</i>Normal text</p>')  
    """
    def test_no_children(self):
        node = ParentNode('p')
        print(node.to_html()) 
        self.assertRaises(ValueError, ParentNode, 'a',None,None)
    """
    
    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [])  # Empty list should raise an error



if __name__ == "__main__":
    unittest.main()
