import unittest
from text_to_textnodes import * 

class Testtext_to_textnodes(unittest.TestCase):
   def test_eq(self):
    text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
     
    result = text_to_textnodes(text)  # Get actual result
    #print(f'Actual Output:\n{result}')

    self.assertEqual(text_to_textnodes(text), [
    TextNode("This is ", TextType.NORMAL),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.NORMAL),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.NORMAL),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.NORMAL),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.NORMAL),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])


if __name__ == "__main__":
    unittest.main()
