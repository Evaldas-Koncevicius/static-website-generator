from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT= "code"
    LINK = "link"
    IMAGE = "image"

    #For Test only!
    TEST_TYPE = "test"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        return False
    
    def __repr__(self):
        return  f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(tag = None, value = text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode(tag = "b", value = text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode(tag = "i", value = text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode(tag = "code", value = text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag = "a", value = text_node.text, props = {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(
            tag = "img", 
            value = "", 
            props = {"src": text_node.url, "alt": text_node.text}
        ) 
    else:
        raise Exception ("Wrong text type!")