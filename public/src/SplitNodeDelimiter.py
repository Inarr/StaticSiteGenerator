from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_list=[]
  match delimiter:
    case '**':
      block = TextType.BOLD
    case '*':
      block = TextType.ITALIC
    case '`':
      block = TextType.CODE
  for node in old_nodes:
    if node.text_type != TextType.NORMAL:
      new_list.append(node)
    if node.text.count(delimiter) % 2 != 0:
      raise Exception('Invalid Markdown Syntax')
    
