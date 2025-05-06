from textnode import *


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    #TextNode to HTMLNode Function
    '''
    @staticmethod
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case 'NORMAL':
                return LeafNode(None,text_node.text)
            case 'BOLD':
                return LeafNode('b',text_node.text) 
            case 'ITALIC':
                return LeafNode('i',text_node.text)
            case 'CODE':
                return HTMLNode('code',text_node.text)
            case 'LINK':
                return HTMLNode('a',text_node.text, None, f'href="{text_node.url}"')
            case 'IMAGE': 
                return HTMLNode('img','',None,f'src={text_node.url} alt={text_node.text}')
        raise Exception('Not proper TextNode Type')
    '''
    

    
    @staticmethod
    def text_node_to_html_node(text_node):
        print('****')
        print('Your text_type is:')
        print(text_node.text_type)
        print('****')
        match text_node.text_type:
            case TextType.NORMAL:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode('b', text_node.text)
            case TextType.ITALIC:
                return LeafNode('i', text_node.text)
            case TextType.CODE:
                return LeafNode('code', text_node.text)
            case TextType.LINK:
                return LeafNode('a', text_node.text, props=f'href="{text_node.url}"')
            case TextType.IMAGE:
                return LeafNode('img', '', props={"src": text_node.url, "alt": text_node.text})
        raise Exception('Not proper TextNode Type')
    
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        strinResult=''
        for item in self.props:
            strinResult +=' ' + item + '=' + self.props[item]
        return strinResult
    
    def __repr__(self):
        print(f'The tag is {self.tag}')
        print(f'The value is {self.value}')
        print(f'The children are {self.children}')
        print(f'The props are {self.props}')

class LeafNode(HTMLNode):
    def __init__(self, tagl, valuel, propsl = None):
        super().__init__(tag = tagl, value = valuel, children = None, props = propsl)
        if self.value == None:
            raise ValueError('Leaf must have a value')

    def to_html(self):
        '''
        if self.value == None:
            raise ValueError('Leaf must have a value')
            '''
        tagList = ['p','b','i']
        if self.tag == None:
            return self.value
        elif self.tag in tagList:
            return (f'<{self.tag}>{self.value}</{self.tag}>')
        elif self.tag == 'a':
            return (f'<a href="{self.props["href"]}">{self.value}</a>')
         

class ParentNode(HTMLNode):
    def __init__(self, tagl, children1, propsl = None):
        children1 = children1 if children1 is not None else []
        super().__init__(tag = tagl, value = None, children = children1, props = propsl)
        if self.tag == None or self.children == None or self.children == []:
            raise ValueError('Parent must have a tag and children')
    """
    def to_html(self):
        if self.tag == None:
            raise ValueError('Parent has no Tag')
        if self.children == None or self.children == []:
            raise ValueError('Parent is misisng children')
        for child in self.children:
            while child != None or child != []:
                child.to_html()
            return LeafNode(child).to_html()
    """
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent has no Tag")
        if not self.children:  # Check if children list is empty
            raise ValueError("Parent is missing children")

        # Generate HTML for all children
        children_html = "".join(child.to_html() for child in self.children)
        
        return f"<{self.tag}>{children_html}</{self.tag}>"

        
            
    
        
        

