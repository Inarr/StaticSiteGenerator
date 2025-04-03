def markdown_to_blocks(markdown):
  tempBlocks = markdown.strip().strip('\n').split('\n\n')
  resultList = []
  for item in tempBlocks:
    if item:
      resultList.append(item)
  return resultList
