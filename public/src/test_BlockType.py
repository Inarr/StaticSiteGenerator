import unittest

from BlockType import *

class TestBlockType(unittest.TestCase):
  def test_heading_1(self):
    block = '*** heading'
    self.assertEqual(block_to_block_type(block),BlockType.HEADING)

  def test_heading_2(self):
      block = '***0 heading'
      self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

  def test_heading_3(self):
    block = '******* heading'
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

   def test_code_1(self):
    block = '``` code ```'
    self.assertEqual(block_to_block_type(block),BlockType.CODE)

  def test_code_2(self):
    block = '``` code '
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

  def test_quote_1(self):
    block = '> quote 1\n\
    > quote 2'
    self.assertEqual(block_to_block_type(block),BlockType.QUOTE)

  def test_quote_2(self):
    block = '> quote 1\n\
    quote 2'
    self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
