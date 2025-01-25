class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
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

