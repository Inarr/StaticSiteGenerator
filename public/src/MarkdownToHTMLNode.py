from markdown_to_blocks import markdown_to_blocks
from BlockType import *

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(mrkdown)
  block_type_dict = {}
  for block in blocks:
    block_type_dict[block] = block_to_block_type(block)

# string of text and returns a list of HTMLNodes
def text_to_children(text):
  text_nodes = text_to_textnodes(text)  # You will need to implement this helper
  html_nodes = []

  for node in text_nodes:
    html_node = HTMLNode.text_node_to_html_node(node)
    html_nodes.append(html_node)

  return html_nodes


# Converts text into a list of TextNodes
'''
text = 'This is *italic*, **bold**, and `code`'
text_nodes = [
    TextNode("This is ", TextType.NORMAL),
    TextNode("italic", TextType.ITALIC),
    TextNode(", ", TextType.NORMAL),
    TextNode("bold", TextType.BOLD),
    TextNode(", and ", TextType.NORMAL),
    TextNode("code", TextType.CODE),
]
'''
def text_to_textnode(text):
  
    
    
