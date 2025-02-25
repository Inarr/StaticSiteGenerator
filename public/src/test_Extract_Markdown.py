import unittest
from Extract_Markdown import *

class TestExtract_Markdown(unittest.TestCase):
   def test_eq_image(self):
     text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
     result = extract_markdown_images(text)
      self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], result)

  def test_eq_link(self):
     text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
     result = extract_markdown_links(text)
      self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], result)


if __name__ == "__main__":
    unittest.main()
