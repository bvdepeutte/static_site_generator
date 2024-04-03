from textnode import TextNode
from inline_markdown import text_to_textnodes
from htmlnode import HTMLNode
from blocks_markdown import markdown_to_blocks, block_to_block_type

with open("/home/bvdepeut/workspace/github.com/bvdepeutte/static_site_generator/src/block_test.txt", "r") as file:
    content = file.read()


def main():
    text = block_to_block_type("```Code```")
    print(text)
main()