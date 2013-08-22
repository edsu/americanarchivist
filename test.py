import unittest

import crawl

class CrawTest(unittest.TestCase):

    def test_get_article(self):
        a = crawl.get_article("http://archivists.metapress.com/content/j037j5v9q78x9012/?p=ee45d0b193e74ccfbc19f5ae183db4c4&pi=7")
        self.assertEqual(a["title"], "CSS Alabama Digital Collection: A Special Collections Digitization Project")
        self.assertEqual(a["author"], [{"name": "Andrea Watson"}, {"name": "P. Toby Graham"}])

    def test_front_matter(self):
        a = crawl.get_article("http://archivists.metapress.com/content/u20x3p0328787725/?p=9a5beca3d39340ebbcca95ec454020dc&pi=0")
        self.assertEqual(len(a['author']), 0)

    def test_pdf(self):
        a = crawl.get_article("http://archivists.metapress.com/content/j707664h6778v1l1/?p=2f7d392ecc3e4d9299dcf622a929b1c6&pi=4")
        self.assertEqual(a['pdf'], 'http://archivists.metapress.com/content/j707664h6778v1l1/fulltext.pdf')


if __name__ == "__main__":
    unittest.main()
