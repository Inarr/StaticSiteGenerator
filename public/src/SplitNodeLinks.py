from textnode import TextType, TextNode
from Extract_Markdown import *


def split_nodes_link(old_nodes):
    #print(f"\nProcessing Links:\n {old_nodes}")
    #print('******')
    finalList=[]
    for item in old_nodes:
        if item.text_type != TextType.NORMAL:
            finalList.append(item)
            continue
        resultList=[]
        images = extract_markdown_links(item.text)
        #print('****')
        #print(f"Extracted Links from '{item.text}': {images}")
        #print('****')
        newText = item.text
        if images:
            for image in images:
                tempList = newText.split(f'[{image[0]}]({image[1]})',1)
                if tempList[0]:
                    resultList.append(TextNode(tempList[0], TextType.NORMAL))
                resultList.append(TextNode(image[0], TextType.LINK, image[1]))
                #newText = tempList[1]
                newText = tempList[1] if len(tempList) > 1 else None
        '''
        elif item.text:
            #resultList.append(TextNode(item, TextType.NORMAL))
            resultList.append(TextNode(item.text, item.text_type))
        '''
        if newText:  # Append remaining text (e.g., links)
            resultList.append(TextNode(newText, item.text_type))
        finalList.extend(resultList)
    return finalList
