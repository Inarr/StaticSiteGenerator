from textnode import TextType, TextNode
from SplitNodeDelimiter import *
from SplitNodeImages import *
from SplitNodeLinks import *

def text_to_textnodes(text):
  tempList1 = split_nodes_delimiter([text],'**', TextType.BOLD)
  tempList2 = split_nodes_delimiter([tempList1],'_', TextType.ITALIC)
  tempList3 = split_nodes_delimiter([tempList2],'`', TextType.CODE)
  templist4 = split_nodes_image(tempList3)
  return split_nodes_link(templist4)
