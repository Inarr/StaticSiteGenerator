class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
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
    def __init__(self, tagl, valuel, propsl):
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
    def __init__(self, tagl, children1, propsl):
        super().__init__(tag = tagl, value = None, children = children1, props = propsl)
        if self.tag == None or self.children == None:
            raise ValueError('Parent must have a tag and children')

    def to_html(self):
        if self.tag == None:
            raise ValueError('Parent has no Tag')
        if self.children == None:
            raise ValueError('Parent is misisng children')
        for child in self.children:
            while child != None:
                child.to_html()
            return LeafNode(child).to_html()
        
            
    
        
        

