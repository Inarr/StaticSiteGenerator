from enum import Enum

class BlockType(Enum):
  PARAGRAPH = 'paragraph'
  HEADING = 'heading'
  CODE = 'code'
  QUOTE = 'quote'
  UNORDERED_LIST = 'unordered_list'
  ORDERED_LIST = 'ordered_list'

def block_to_block_type(block):
  # Check for Heading
  if block[0] =='*':
    for i in range(1,7):
      if block[i] == ' ' and block[i-1] == '*':
        return BlockType.HEADING
      elif i == 6:
        return BlockType.PARAGRAPH
        
    # Check for Code  
  if block[:3] == block[-3:] and block[:3] == '```':
    return BlockType.CODE
  elif block[:3] == '```':
    return BlockType.PARAGRAPH


    # Check for Quote
  if block[0] == '>':
    for line in block.split('\n'):
      if line[0] != '>':
        return BlockType.PARAGRAPH
        break
    return BlockType.QUOTE

      # Check for Unordered List
  if block[:2] == '- ':
    #print('*** Checking for Unordered List ***')
    #print(block[:1])
    lines = block.split('\n')
    #print(lines)
    for line in lines:
      #print(line)
      if line[:2] != '- ':
        #print('IF Entered')
        return BlockType.PARAGRAPH
        break
    return BlockType.UNORDERED_LIST
        
      # Check for Ordered List
  if block[:3] == '1. ':
    order = 1
    for line in block.split('\n'):
      if line[:3] != str(order) + '. ':
        return BlockType.PARAGRAPH
        break
      order +=1
    return BlockType.ORDERED_LIST


        
      
  
