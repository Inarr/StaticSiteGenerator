from enum import Enum

class TextType(Enum):
    NORMAL = 'Normal Text'
    BOLD = 'Bold Text'
    ITALIC = 'Italic Text'
    CODE = 'Code Text'
    LINKS = 'Links'
    IMAGES = 'Images'

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        #print('__eq__ is being executed')
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self, TextNode_1):
        return f'TextNode({TextNode_1.text}, {TextNode_1.text_type}, {TextNode_1.url})'
