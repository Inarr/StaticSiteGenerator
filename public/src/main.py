from textnode import TextNode,__repr__, TextType
#print('Hello World')
def main():
    textNodeObject = TextNode('This is a text node',TextType['BOLD'].value,'https://www.boot.dev')
    print(__repr__(textNodeObject))


main()