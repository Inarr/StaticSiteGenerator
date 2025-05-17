from markdown_to_blocks import markdown_to_blocks
from BlockType import *
from text_to_textnodes import text_to_textnodes
from htmlnode import *
from textnode import *

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  nodeList = []
  for block in blocks:
    block_type = block_to_block_type(block)
    match  block_type:
      case BlockType.PARAGRAPH:
        children = text_to_children(block)
        #nodeList.append(HTMLNode('p', None,children))
        nodeList.append(ParentNode('p',children))
      case BlockType.HEADING:
        children = text_to_children(block)
        asterixCount = 0
        for i in block:
          if i == '*':
            asterixCount +=1
          else:
            break
        nodeList.append(HTMLNode(f'h{asterixCount}', None,children))
        #nodeList.append(ParentNode(f'h{asterixCount}',children))
        '''
      case BlockType.CODE:
        CodeText = TextNode(block,TextType.CODE)
        #nodeList.append(HTMLNode('pre',None,HTMLNode( 'code',HTMLNode.text_node_to_html_node(CodeText))))
        nodeList.append(HTMLNode('pre',None,LeafNode( 'code',HTMLNode.text_node_to_html_node(CodeText))))
        #nodeList.append(ParentNode('pre',None,HTMLNode( 'code',HTMLNode.text_node_to_html_node(CodeText))))
        '''
      case BlockType.CODE:
        code_text = TextNode(block, TextType.CODE)
        code_node = HTMLNode.text_node_to_html_node(code_text)  # Returns a LeafNode('code', block)
        nodeList.append(ParentNode('pre', [code_node]))

      case BlockType.QUOTE:
        children = text_to_children(block)
        #nodeList.append(HTMLNode('<blockquote>', None,children))
        nodeList.append(ParentNode('blockquote', children))
      case BlockType.UNORDERED_LIST:
        #children = text_to_children(block)
        list_items = []
        for item in block.split("\n"):
            clean_item = item.lstrip("-*1234567890. ").strip()
            list_items.append(HTMLNode("li", None, text_to_children(clean_item)))
        #nodeList.append(HTMLNode("ul", None, list_items))
        nodeList.append(ParentNode("ul", list_items))

      case BlockType.ORDERED_LIST:
        #children = text_to_children(block)
        list_items = []
        for item in block.split("\n"):
            clean_item = item.lstrip("-*1234567890. ").strip()
            list_items.append(HTMLNode("li", None, text_to_children(clean_item)))
        nodeList.append(HTMLNode("ol", None, list_items))

  #return HTMLNode('<div>',None,nodeList)
  return ParentNode('div', nodeList)

# string of text and returns a list of HTMLNodes
def text_to_children(text):
  text_nodes = text_to_textnodes(text)  
  html_nodes = []

  for node in text_nodes:
    html_node = HTMLNode.text_node_to_html_node(node)
    html_nodes.append(html_node)

  return html_nodes



  
    
    
