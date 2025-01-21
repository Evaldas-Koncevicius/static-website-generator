import unittest, pytest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_texttype_dif(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_text_dif(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node!", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_url_dif(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "http://git.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "http://git.org")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        #tests normal text, no tags
        node = TextNode("Just a plain text", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == None
        assert html_node.value == "Just a plain text"
        assert html_node.props == None

        #tests bold text and tag
        node = TextNode("Just a bold text", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "b"
        assert html_node.value == "Just a bold text"
        assert html_node.props == None

        #tests italic text and tag
        node = TextNode("Just an italic text", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "i"
        assert html_node.value == "Just an italic text"
        assert html_node.props == None

        #tests code text and tag
        node = TextNode("Just a code text", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "code"
        assert html_node.value == "Just a code text"
        assert html_node.props == None

        #tests link tag, text and prop dictionary
        node = TextNode("Just a link text", TextType.LINK, "www.test.com")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "a"
        assert html_node.value == "Just a link text"
        assert html_node.props == {"href": "www.test.com"}
        
        #tests img tag, if value is empty string and props dictionary
        node = TextNode("Just an img text", TextType.IMAGE, "www.test.com")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "www.test.com", "alt": "Just an img text"}

        #tests exception when text type is wrong
        with pytest.raises(Exception):
            node = TextNode("Just a plain text", TextType.TEST_TYPE)
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()