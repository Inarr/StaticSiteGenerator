import unittest

from BlockType import *

class TestBlockType(unittest.TestCase):
  def test_heading_1(self):
    block = '### heading'
    self.assertEqual(block_to_block_type(block),BlockType.HEADING)

  def test_heading_2(self):
      block = '###0 heading'
      self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

  def test_heading_3(self):
    block = '####### heading'
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

  def test_code_1(self):
    block = '``` code ```'
    self.assertEqual(block_to_block_type(block),BlockType.CODE)

  def test_code_2(self):
    block = '``` code '
    #print('***')
    #print(block[:2])
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

  def test_quote_1(self):
    block = '> quote 1\n\
> quote 2'
    self.assertEqual(block_to_block_type(block),BlockType.QUOTE)

  def test_quote_2(self):
    block = '> quote 1\n\
    quote 2'
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

  def test_unordered_list_1(self):
    block = '- line 1\n\
- line 2'
    '''print('***')
    print(block[:2])
    print(block_to_block_type(block))'''
    self.assertEqual(block_to_block_type(block),BlockType.UNORDERED_LIST)  

  def test_unordered_list_2(self):
    block = '- line 1\n\
    line 2'
    '''print('****')
    print(f'The function returns: {block_to_block_type(block)}')
    print('***')'''
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH) 

  def test_ordered_list_1(self):
    block = '1. line 1\n\
2. line 2'
    self.assertEqual(block_to_block_type(block),BlockType.ORDERED_LIST)

  def test_ordered_list_2(self):
    block = '1. line 1\n\
    3. line 2'
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH) 

  def test_ordered_list_3(self):
    block = '1. line 1\n\
line 2'
    #print(block[:3])
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH) 


if __name__ == "__main__":
    unittest.main()
