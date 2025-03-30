from textnode import TextType, TextNode
from SplitNodeDelimiter import *
from SplitNodeImages import *
from SplitNodeLinks import *

def text_to_textnodes(text_original):
  text = TextNode(text_original,TextType.NORMAL)
  #print('*********')
  #print('Debug test start')
  #print('Original text:\nThis is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')
  tempList1 = split_nodes_delimiter([text],'**', TextType.BOLD)
  tempList1 = [node for sublist in tempList1 for node in sublist]
  #print(f'Result after splitting BOLD:\n{tempList1}')
  tempList2 = split_nodes_delimiter(tempList1,'_', TextType.ITALIC)
  tempList2 = [node for sublist in tempList2 for node in sublist]
  #print(f'Result after splitting ITALIC:\n{tempList2}')
  tempList3 = split_nodes_delimiter(tempList2,'`', TextType.CODE)
  tempList3 = [node for sublist in tempList3 for node in sublist]
  #print(f'Result after splitting CODE:\n{tempList3}')
  tempList4 = split_nodes_image(tempList3)
  #print(f'Result after splitting IMAGES:\n{tempList4}')
  #print(f'Result after splitting LINKS:\n{split_nodes_link(tempList4)}')
  #print('Test End\n***********')
  return split_nodes_link(tempList4)
