from enum import Enum

class BlockType(Enum):
  PARAGRAPH = 'paragraph'
  HEADING = 'heading'
  CODE = 'code'
  QUOTE = 'quote'
  UNORDERED_LIST = 'unordered_list'
  ORDERED_LIST = 'ordered_list'

def block_to_block_type(block):
  if block[0] =='*':
    for i in range(1,7):
      if block[i] == ' ':
        return BlockType.HEADING
      elif i == 6:
        return BlockType.PARAGRAPH
    if block[:2] == block[-2:] and block[:2] == '```':
      return BlockType.CODE
        
      
  
