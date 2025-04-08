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
      if block[i] == ' ':
        return BlockType.HEADING
      elif i == 6:
        return BlockType.PARAGRAPH
        
    # Check for Code  
    if block[:2] == block[-2:] and block[:2] == '```':
      return BlockType.CODE

    # Check for Quote
    if block[0] == '>':
      for line in block.split('\n'):
        if line[0] != '>':
          return BlockType.PARAGRAPH
          break
        return BlockType.QUOTE

      # Check for Unordered List
       if block[0] == '- ':
        for line in block.split('\n'):
          if line[0] != '- ':
            return BlockType.PARAGRAPH
            break
        return BlockType.UNORDERED_LIST
        
      # Check for Ordered List
        if block[0] == '1. ':
          order = 1
          for line in block.split('\n'):
            if line[:3] != order + '. ':
              return BlockType.PARAGRAPH
              break
            order +=1
        return BlockType.UNORDERED_LIST


        
      
  
