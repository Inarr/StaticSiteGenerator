def markdown_to_blocks(markdown):
  '''
  tempBlocks = markdown.strip().strip('\n').split('\n\n')
  resultList = []
  for item in tempBlocks:
    if item:
      resultList.append(item)
      '''
  tempBlocks = markdown.strip().replace('\r\n', '\n').split('\n\n')
  resultList = [item.strip() for item in tempBlocks if item.strip()]
  return resultList
