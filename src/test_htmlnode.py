import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<test>", "test", "ch_test", {"k_test": "v_test"})
        node2 = HTMLNode("<test>", "test", "ch_test", {"k_test": "v_test"})
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_text_dif(self):
        node = HTMLNode("<test>", "test", "ch_test", {"k_test": "v_test"})
        node2 = HTMLNode("<test>", "test1", "ch_test1", {"k_test": "v_test"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()