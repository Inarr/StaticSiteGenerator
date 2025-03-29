from textnode import TextType, TextNode
from Extract_Markdown import *


def split_nodes_link(old_nodes):
    finalList=[]
    for item in old_nodes:
        resultList=[]
        images = extract_markdown_links(item.text)
        newText = item.text
        if images:
            for image in images:
                tempList = newText.split(f'[{image[0]}]({image[1]})',1)
                if tempList[0]:
                    resultList.append(TextNode(tempList[0], TextType.NORMAL))
                resultList.append(TextNode(image[0], TextType.LINK, image[1]))
                newText = tempList[1]
        elif item.text:
            #resultList.append(TextNode(item, TextType.NORMAL))
            resultList.append(TextNode(item.text, item.text_type))
        finalList.extend(resultList)
    return finalList
