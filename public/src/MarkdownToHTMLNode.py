from markdown_to_blocks import markdown_to_blocks
from BlockType import *
from text_to_textnode import text_to_textnodes
from htmlnode import *
from textnode import *

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  nodeList = []
  for block in blocks:
    block_type = block_to_block_type(block)
    match  block_type:
      case 'paragraph':
        children = text_to_children(block)
        nodeList.append(HTMLNode('<p>', None,children))
      case 'heading':
        children = text_to_children(block)
        asterixCount = 0
        for i in block:
          if i == '*':
            asterixCount +=1
          else:
            break
        nodeList.append(HTMLNode('<h' + asterixCount + '>', None,children))
      case 'code':
        CodeText = TextNode(block,TextType.CODE)
        nodeList.append(HTMLNode( '<pre><code>',HTMLNode.text_node_to_html_node(CodeText)))
      case 'quote':
        children = text_to_children(block)
        nodeList.append(HTMLNode('<blockquote>', None,children))
      case 'unordered_list':
        children = text_to_children(block)
        nodeList.append(HTMLNode('<ul>', None,HTMLNode('<li>',None,children)))
      case 'ordered_list':
        children = text_to_children(block)
        nodeList.append(HTMLNode('<ol>', None,HTMLNode('<li>',None,children)))
    return HTMLNode('<div>',None,nodeList)

# string of text and returns a list of HTMLNodes
def text_to_children(text):
  text_nodes = text_to_textnodes(text)  
  html_nodes = []

  for node in text_nodes:
    html_node = HTMLNode.text_node_to_html_node(node)
    html_nodes.append(html_node)

  return html_nodes



  
    
    
