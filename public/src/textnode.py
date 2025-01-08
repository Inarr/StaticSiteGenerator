from enum import Enum

class TextType(Enum):
    NORMAL = 'Normal Text'
    BOLD = 'Bold Text'
    ITALIC = 'Italic Text'
    CODE = 'Code Text'
    LINKS = 'Links'
    IMAGES = 'Images'

class TextNode:
    def __init__(self, text, text_type, url = 'None'):
        self.text = text
        self.text_type = text_type
        self.url = url

def __eq__(TextNode_1,TextNode_2):
    if TextNode_1.text != TextNode_2.text:
        return False
    if TextNode_1.text_type != TextNode_2.text_type:
        return False
    if TextNode_1.url != TextNode_2.url:
        return False
    return True

def __repr__(TextNode_1):
    return f'TextNode({TextNode_1.text}, {TextNode_1.text_type}, {TextNode_1.url})'
