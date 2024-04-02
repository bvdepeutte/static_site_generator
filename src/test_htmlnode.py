import unittest
from htmlnode import (
    HTMLNode,
    LeafNode
)


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(None,"Visit our website",None,{"href":"www.emasphere.com","class":"reporting"})
        self.assertEqual(
            node.props_to_html(),
            ' href="www.emasphere.com" class="reporting"'
        )

class TestHTMLLeaf(unittest.TestCase):
    def test_non_formatted_to_html(self):
        leaf = LeafNode(None,"Not formatted text")
        self.assertEqual(leaf.to_html(),"Not formatted text")
    def test_p_tag_to_html(self):
        leaf = LeafNode("p","Paragraph text")
        self.assertEqual(leaf.to_html(),"<p>Paragraph text</p>")
    def test_a_tag_to_html(self):
        leaf = LeafNode("a","URL Link",{"href":"emasphere.com"})
        self.assertEqual(leaf.to_html(),'<a href="emasphere.com">URL Link</a>')
    def test_error_raised_to_html(self):
        leaf = LeafNode("a",None)
        with self.assertRaises(ValueError):
            leaf.to_html()

if __name__ == "__main__":
    unittest.main()
