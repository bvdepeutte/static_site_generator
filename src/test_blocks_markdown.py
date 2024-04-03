from blocks_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)
import unittest


class TestInlineMarkdown(unittest.TestCase):
    with open("/home/bvdepeut/workspace/github.com/bvdepeutte/static_site_generator/src/block_test.txt", "r") as file:
        content = file.read()
    def test_markdown_to_blocks(self):
        self.assertListEqual(
            [
                'This is **bolded** paragraph',
                'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
                '* This is a list\n* with items'
            ]
        , markdown_to_blocks(self.content)
        )
    def test_block_to_block_type_heading(self):
        text = "#### Heading"
        self.assertEqual(block_type_heading, block_to_block_type(text))

    def test_block_to_block_type_not_heading(self):
        text = "####Heading"
        self.assertNotEqual(block_type_heading, block_to_block_type(text))

    def test_block_to_block_type_code(self):
        text = "```\ncode\n```"
        self.assertEqual(block_type_code, block_to_block_type(text))
    
    def test_block_to_block_type_not_code(self):
        text = "```Code``"
        self.assertNotEqual(block_type_code, block_to_block_type(text))

    def test_block_to_block_type_quote(self):
        text = ">Quote"
        self.assertEqual(block_type_quote, block_to_block_type(text))
    
    def test_block_to_block_type_not_quote(self):
        text = "$>Quote"
        self.assertNotEqual(block_type_quote, block_to_block_type(text))
    
    def test_block_to_block_type_unordered_list(self):
        text = "*UnorderedList"
        self.assertEqual(block_type_unordered_list, block_to_block_type(text))
    
    def test_block_to_block_type_not_unordered_list(self):
        text = "unordered_list"
        self.assertNotEqual(block_type_unordered_list, block_to_block_type(text))
    
    def test_block_to_block_type_unordered_list(self):
        text = "1. OrderedList"
        self.assertEqual(block_type_ordered_list, block_to_block_type(text))
    
    def test_block_to_block_type_not_unordered_list(self):
        text = "1 ordered_list"
        self.assertNotEqual(block_type_ordered_list, block_to_block_type(text))