from markdown_to_blocks import markdown_to_blocks
from BlockType import *
from text_to_textnode import text_to_textnodes

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(mrkdown)
  block_type_dict = {}
  for block in blocks:
    block_type_dict[block] = block_to_block_type(block)

# string of text and returns a list of HTMLNodes
def text_to_children(text):
  text_nodes = text_to_textnodes(text)  
  html_nodes = []

  for node in text_nodes:
    html_node = HTMLNode.text_node_to_html_node(node)
    html_nodes.append(html_node)

  return html_nodes



  
    
    
