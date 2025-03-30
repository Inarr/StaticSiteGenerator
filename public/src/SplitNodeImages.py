from textnode import TextType, TextNode
from Extract_Markdown import *


def split_nodes_image(old_nodes):
    #print(f"\nProcessing Images:\n {old_nodes}")
    #print('*******')
    finalList=[]
    for item in old_nodes:
        resultList=[]
        images = extract_markdown_images(item.text)
        #print('****')
        #print(f"Extracted images from '{item.text}': {images}")
        #print('****')
        newText = item.text
        if images:
            for image in images:
                tempList = newText.split(f'![{image[0]}]({image[1]})',1)
                #print('***')
                #print(f'The tempList is:\n{tempList}')
                #print('***')
                if tempList[0]:
                    resultList.append(TextNode(tempList[0], TextType.NORMAL))
                resultList.append(TextNode(image[0], TextType.IMAGE, url=image[1]))
                #newText = tempList[1]
                newText = tempList[1] if len(tempList) > 1 else None
        '''
        elif item:
            resultList.append(TextNode(item.text, item.text_type))
        '''
        if newText:  # Append remaining text (e.g., links)
            resultList.append(TextNode(newText, item.text_type))
        finalList.extend(resultList)
    #print(f'** The finalList is: **\n {finalList}')
    return finalList





