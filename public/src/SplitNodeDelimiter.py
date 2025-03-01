from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  master_list=[] 
  for node in old_nodes:
    new_list=[]
    if node.text.count(delimiter) % 2 != 0:
      raise Exception('Invalid Markdown Syntax')
    if node.text_type != TextType.NORMAL:
      new_list.append(node)
    else:
      # Splitting Text according to the Delimiter
      temp_list = node.text.split(delimiter)
      # If the first string was blocked, the TextTye is every odd position in temp_list
      if node.text.find(delimiter) == 0:
        for i in range(len(temp_list)):
          if i%2 == 0:
            new_list.append(TextNode(temp_list[i], text_type))
          else:
            new_list.append(TextNode(temp_list[i], TextType.NORMAL))
      else: # Delimiter in every even position
         for i in range(len(temp_list)):
          if i%2 != 0:
            new_list.append(TextNode(temp_list[i], text_type))
          else:
            new_list.append(TextNode(temp_list[i], TextType.NORMAL))
    master_list.append(new_list)
  return master_list
      
        
    
