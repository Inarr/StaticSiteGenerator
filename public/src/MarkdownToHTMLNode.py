from markdown_to_blocks import markdown_to_blocks
from BlockType import *

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(mrkdown)
  block_type_dict = {}
  for block in blocks:
    block_type_dict[block] = block_to_block_type(block)

# string of text and returns a list of HTMLNodes
def text_to_children(text):
  
    
    
