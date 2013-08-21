import unittest

import crawl

class CrawTest(unittest.TestCase):

    def test_get_article(self):
        a = crawl.get_article("http://archivists.metapress.com/content/j037j5v9q78x9012/?p=ee45d0b193e74ccfbc19f5ae183db4c4&pi=7")
        self.assertEqual(a["title"], "CSS Alabama Digital Collection: A Special Collections Digitization Project")
        self.assertEqual(a["author"], [{"name": "Andrea Watson"}, {"name": "P. Toby Graham"}])

if __name__ == "__main__":
    unittest.main()
