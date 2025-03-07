from textnode import TextType, TextNode
from Extract_Markdown import *

testNode = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and\
     another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.NORMAL,
)

def split_nodes_image(old_nodes):
    for item in old_nodes:
        


split_nodes_image([testNode])


